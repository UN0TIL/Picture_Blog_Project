
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import  DetailView, UpdateView, CreateView
from django.db import transaction
from django.urls import reverse_lazy

from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm, UserLoginForm


# Create your views here.

class ProfileDetailView(DetailView):
    '''
    Представление для промотра профиля
    '''
    model = Profile
    context_object_name = 'profile'
    template_name = 'accounts/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Профиль пользователя {self.object.user.username}'
        return context

class ProfileUpdateView(UpdateView):
    '''
    Представление для редактирования профиля
    '''
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_edit.html'

    def get_object(self, queryset=None):
        '''
        В методе get_object() мы передаем текущего пользователя, чтобы не редактировать чужие профили.
        :param queryset:
        :return:
        '''
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        '''
        В контексте мы добавляем форму пользователя, где ссылаемся на текущего пользователя.
        :param kwargs:
        :return:
        '''
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование профиля {self.object.user.username}'
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        '''
        В методе form_valid() мы используем transaction.atomic, для корректного сохранения данных двух форм в нашей БД.
        :param form:
        :return:
        '''
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
            return super().form_valid(form)


    def get_success_url(self):
        '''
        В методе get_success_url() мы ссылаемся на наш профиль, т.е после сохранения мы переходим на страницу нашего профиля.
        :param self:
        :return:
        '''
        return reverse_lazy('profile_detail', kwargs={'slug': self.object.slug})

class UserRegisterView(CreateView, SuccessMessageMixin):
    '''
    Предоставление регистрации на сайте с формой регистрации
    '''
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/user_register.html'
    success_message = 'Вы успешно зарегестрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context


class UserLoginView(LoginView, SuccessMessageMixin):
    '''
    Авторизация на сайте
    '''
    form_class = UserLoginForm
    template_name = 'accounts/user_login.html'
    next_page = 'home'
    success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context


class UserLogoutView(LogoutView):
    '''
    Выход с сайте
    '''
    next_page = 'home'