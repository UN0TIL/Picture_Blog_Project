from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from apps.services.utils import unique_slugify
from django.core.cache import cache

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, max_length=255, verbose_name='URL')
    avatar = models.ImageField(verbose_name="Аватар", upload_to="images/avatars/%Y/%m/%d", default="images/avatars/default.jpg", blank=True, validators=[FileExtensionValidator(["jpg", "png", 'jpeg'])])
    bio = models.TextField(max_length=500, blank=True, verbose_name='Информация о себе')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    class Meta:
        '''
        Сортировка, название страницы в базе данных
        '''
        ordering = ['user']
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):
        '''
        Сохранения полей модели при их отсутствии заполнения
        :param args:
        :param kwargs:
        :return:
        '''

        if not self.slug:
            self.slug = unique_slugify(self, self.user.username, self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        '''
        Возвращение строки
        :return:
        '''
        return  self.user.username

    def get_absolute_url(self):
        '''
        Ссылка на профиль
        :return:
        '''
        return reverse('profile_detail', kwargs={'slug': self.slug})


    def is_online(self):
        cache_key = f'last-seen-{self.user.id}'
        last_seen = cache.get(cache_key)

        if last_seen is not None:
            return True
        return False
