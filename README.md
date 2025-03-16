#🖼️ Picture Blog Project (English Version)
##✨ About the Project
Picture Blog Project is a platform for blogging with a focus on images. Users can create posts, organize them by tags and categories, and like the content they enjoy. The project is built on SQLite, and the interface is designed with Bootstrap for ease of use.

##🔥 The main idea of the project is to make blogging intuitive and content interaction as convenient as possible. The flexible system of tags and categories allows users to easily structure their content, and likes help highlight the most popular posts. It’s an excellent tool for personal use as well as for creating interest-based communities.

##🚀 Quick Start
##📦 Installing Dependencies
Before launching, make sure you have Python 3.x and PostgreSQL installed. Then run:

bash
Копировать
Редактировать
pip install -r requirements.txt
🔧 Database Setup
Create a database in PostgreSQL and configure the settings in settings.py:

python
Копировать
Редактировать
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Apply migrations:

bash
Копировать
Редактировать
python manage.py migrate
##🔑 Admin Access
Create a superuser:

bash
Копировать
Редактировать
python manage.py createsuperuser
Or use the default credentials:
##📌 Username: admin
##🔑 Password: admin

##▶️ Run the Server
bash
Копировать
Редактировать
python manage.py runserver
The blog will be available at: http://127.0.0.1:8000

##🔥 Features
✔ Create and edit posts
✔ Upload images
✔ Tagging and categorization system
✔ Likes and content interaction
✔ Responsive interface (Bootstrap)
✔ Django Admin for blog management

###🌍 Deploying to a Server
For testing, you can use ngrok:

bash
Копировать
Редактировать
ngrok http 8000
Copy the generated address and add it to ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS in settings.py.

##💡 Contact
If you have any questions or ideas, feel free to reach out! 🎨

#🖼️ Picture Blog Project (Ukrainian Version)
##✨ Про проєкт
Picture Blog Project — це платформа для ведення блогу з акцентом на зображення. Користувачі можуть створювати пости, сортувати їх за тегами та категоріями, а також ставити лайки на цікавий контент. Проєкт побудований на SQLite, а інтерфейс розроблений із використанням Bootstrap для зручності користувачів.

##🔥 Основна ідея проєкту — зробити ведення блогу інтуїтивно зрозумілим, а взаємодію з контентом максимально зручною. Гнучка система тегів і категорій дозволяє користувачам легко структуризувати свій контент, а лайки допомагають знаходити найпопулярніші публікації. Це чудовий інструмент як для особистого використання, так і для створення спільнот за інтересами.

🚀 Швидкий старт
📦 Встановлення залежностей
Перед запуском переконайтесь, що у вас встановлені Python 3.x та PostgreSQL. Потім виконайте:

bash
Копировать
Редактировать
pip install -r requirements.txt
🔧 Налаштування бази даних
Створіть базу даних у PostgreSQL та вкажіть налаштування в settings.py:

python
Копировать
Редактировать
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Застосуйте міграції:

bash
Копировать
Редактировать
python manage.py migrate
##🔑 Адмін-доступ
Створіть суперкористувача:

bash
Копировать
Редактировать
python manage.py createsuperuser
Або використовуйте стандартні дані:
##📌 Логін: admin
##🔑 Пароль: admin

###▶️ Запуск сервера
bash
Копировать
Редактировать
python manage.py runserver
Блог буде доступний за адресою: http://127.0.0.1:8000

🔥 Можливості
✔ Створення та редагування постів
✔ Завантаження зображень
✔ Система тегів та категорій
✔ Лайки та взаємодія з контентом
✔ Адаптивний інтерфейс (Bootstrap)
✔ Адмін-панель Django для управління блогом

🌍 Розгортання на сервері
Для тестування можна використовувати ngrok:

bash
Копировать
Редактировать
ngrok http 8000
Скопіюйте згенеровану адресу та додайте її в ALLOWED_HOSTS і CSRF_TRUSTED_ORIGINS у settings.py.

💡 Контакти
Якщо у вас є питання або ідеї, не соромтесь звертатися! 🎨

# 🖼️ Picture Blog Project

## ✨ О проекте

**Picture Blog Project** — это платформа для ведения блога с акцентом на **изображения**. Здесь можно создавать посты, сортировать их по **тегам и разделам**, а также **ставить лайки** на понравившийся контент. Проект построен на **SQLite**, использует **Bootstrap** для удобного интерфейса.

🔥 **Главная идея проекта** — сделать ведение блога интуитивно понятным, а взаимодействие с контентом — максимально удобным. Благодаря гибкой системе тегов и разделов, пользователи могут легко структурировать свой контент, а лайки позволяют находить самые популярные публикации. Это отличный инструмент как для личного использования, так и для создания **сообщества по интересам**.

## 🚀 Быстрый старт

### 📦 Установка зависимостей
Перед запуском убедитесь, что у вас установлены **Python 3.x** и **PostgreSQL**. Затем выполните:
```bash
pip install -r requirements.txt
```

### 🔧 Настройка базы данных
Создайте базу в **PostgreSQL** и пропишите настройки в `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Запустите миграции:
```bash
python manage.py migrate
```

### 🔑 Админ-доступ
Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

Или используйте стандартные данные:
📌 **Логин:** `admin`
🔑 **Пароль:** `admin`

### ▶️ Запуск сервера
```bash
python manage.py runserver
```
После этого блог будет доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🔥 Возможности

✔ **Создание и редактирование постов**  
✔ **Загрузка изображений**  
✔ **Система тегов и разделов**  
✔ **Лайки и взаимодействие с контентом**  
✔ **Bootstrap-интерфейс**  
✔ **Django Admin для управления блогом**  

## 🌍 Развёртывание на сервере

Для тестирования можно использовать **ngrok**:
```bash
ngrok http 8000
```
Скопируйте сгенерированный адрес и добавьте его в `ALLOWED_HOSTS` и `CSRF_TRUSTED_ORIGINS` в `settings.py`.

## 💡 Контакты
Если у вас есть вопросы или идеи — пишите, будем рады обсудить! 🎨

