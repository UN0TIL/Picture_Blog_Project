from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
from apps.services.utils import unique_slugify


# Create your models here.

class PostManager(models.Manager):
    '''
    Кастомный менеджер для модели постов
    '''

    def get_queryset(self):
        '''
        Список постов (SQL опрос с фильтрацией по статусу опубликованно)
        :return:
        '''

        return super().get_queryset().select_related('author', 'category').filter(status='published')


class Post(models.Model):
    """
    Модель постов для блога
    """
    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик'),
    )

    title = models.CharField(max_length=255, verbose_name='Название записи')
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True)
    description = RichTextField(config_name='awesome_ckeditor', verbose_name='Краткое описание', max_length=500)
    text = RichTextField(verbose_name='Полный текст записи', config_name='awesome_ckeditor')
    thumbnail = models.ImageField(default='default.jpg',
        verbose_name='Изображение записи',
        blank=True,
        upload_to='images/thumbnails/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])
    status = models.CharField(max_length=10, choices=STATUS_OPTIONS, default='published', verbose_name='Статус записи')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_DEFAULT, related_name='author_posts', default=1)
    updater = models.ForeignKey(to=User, verbose_name='Обновил', on_delete=models.SET_NULL, null=True, related_name='updater_posts', blank=True)
    fixed = models.BooleanField(default=False, verbose_name='Прикреплено', help_text='булево значение, по умолчанию False')

    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')

    objects = models.Manager()
    custom = PostManager()

    tags = TaggableManager()

    def save(self, *args, **kwargs):
        '''
        При сохранении генерируемый slug проверяеться на уникальность
        '''
        self.slug = unique_slugify(self, self.title, self.slug)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'blog_posts'
        ordering = ['-create', '-fixed']
        indexes = [models.Index(fields=['-fixed', '-create', 'status'])]
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_sum_rating(self):
        return sum([rating.value for rating in self.ratings.all()])

    def get_absolute_url(self):
        '''
        Получаем прямую ссылку на статью
        '''
        return reverse('post_detail', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title


class Category(MPTTModel):
    '''
    Модель категорий с вложеностью
    '''
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(verbose_name='URL категории', max_length=255, blank=True)
    description = models.TextField(verbose_name='Описание категории', max_length=300)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, db_index=True, related_name='children', verbose_name='Родительская категория')

    class MPTTMeta:
        '''
        Сортировка по вложености
        '''
        order_insertion_by = ('title',)

    class Meta:
        '''
        Сортировка, название модели в админ панели, таблица с данными
        '''
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'app_categories'

    def __str__(self):
        '''
        Возвращение заголовка категории
        :return:
        '''
        return self.title

    def get_absolute_url(self):
        '''
        Получаем прямую ссылку на категорию
        '''
        return reverse('post_by_category', kwargs={'slug': self.slug})


class Comment(MPTTModel):
    '''
    Модель древовидных комментариев
    '''

    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик')
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Запись', related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', related_name='comments_author')
    content = models.TextField(verbose_name='Текст комментария', max_length=3000)
    time_create = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновления', auto_now=True)
    status = models.CharField(choices=STATUS_OPTIONS, default='published', verbose_name='Статус поста', max_length=10)
    parent = TreeForeignKey('self', verbose_name='Родительский коментарий', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MTTMeta:
        '''
        Сортировка по вложености
        '''
        order_insertion_by = ('-time_create',)

    class Meta:
        ordering = ['-time_create']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author}: {self.content}'


class Rating(models.Model):
    '''
    Модель рейтинга: Лайк - Дизлайк
    '''
    post = models.ForeignKey(to=Post, verbose_name='Запись', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(to=User, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True)
    value = models.IntegerField(verbose_name='Значение', choices=[(1, 'Нравится'), (-1, 'Не нравится')])
    time_creator = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)
    ip_address = models.GenericIPAddressField(verbose_name='IP Адрес')

    class Meta:
        unique_together = ('post', 'ip_address')
        ordering = ('-time_creator',)
        indexes = [models.Index(fields=['-time_creator', 'value'])]
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return self.post.title