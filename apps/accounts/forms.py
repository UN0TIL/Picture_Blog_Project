from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField

from .models import Profile

class UserUpdateForm(forms.ModelForm):
    '''
    Форма обновления пользователя
    '''
    username = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control mb-1'})))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control mb-1"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control mb-1'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-1'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-1'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        '''
        Проверка email на уникальность
        '''
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email должен быть уникальным')
        return email

class ProfileUpdateForm(forms.ModelForm):
    '''
    Форма обновления данных профиля пользователя
    '''
    slug = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-1'}))
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control mb-1'}))
    bio = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control mb-1'}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control mb-1'}))


    class Meta:
        model = Profile
        fields = ('slug', 'birth_date', 'bio', 'avatar')


class UserRegistrationForm(UserCreationForm):
    '''
    Переопределенная форма регисрации пользователей
    '''

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def clean_email(self):
        '''
        Проверка email на уникальность
        :return:
        '''
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Такой email уже используеться в системе')
        return email

    def __init__(self, *args, **kwargs):
        '''
        Обновление стилей формы регистрации
        :param args:
        :param kwargs:
        '''

        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Придумайте свой логин'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Введите свой email'})
        self.fields['first_name'].widget.attrs.update({"placeholder": "Ваше имя"})
        self.fields['last_name'].widget.attrs.update({"placeholder": "Ваша фамилия"})
        self.fields['password1'].widget.attrs.update({"placeholder": "Придумайте свой пароль"})
        self.fields['password2'].widget.attrs.update({"placeholder": "Повторите придуманный пароль"})
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})


class UserLoginForm(AuthenticationForm):
    '''
    Форма авторизации на сайте
    '''

    recaptcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username', 'password', 'recaptcha']

    def __init__(self, *args, **kwargs):
        '''
        Обновление стилей формы авторизации
        :param args:
        :param kwargs:
        '''
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Логин пользователя'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Пароль пользователя'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = 'Логин'
