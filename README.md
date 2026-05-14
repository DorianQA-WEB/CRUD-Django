# CRUD-проект на Django

Простой CRUD-проект для управления пользователями (Person) с использованием Django.

## Описание

Проект позволяет:
- Создавать, просматривать, редактировать и удалять записи пользователей.
- Использует встроенные средства Django: модели, формы, представления и шаблоны.

## Структура проекта

- `CRUD_DjangoProject/` — основной проект Django.
- `crud/` — приложение для управления данными.
  - `models.py` — модель `Person` (имя, возраст).
  - `forms.py` — форма `PersonForm` для работы с моделью.
  - `views.py` — функции-представления (`index`, `create`, `edit`, `delete`).
  - `urls.py` — маршруты приложения.
  - `templates/` — HTML-шаблоны.

## Форма PersonForm

Файл: `crud/forms.py`
python class PersonForm(ModelForm): name = CharField(label="Имя пользователя") age = IntegerField(label="Введите возраст")
class Meta:
    model = Person
    fields = ['name', 'age']

- Наследуется от `ModelForm`, привязана к модели `Person`.
- Поля:
  - `name` — текстовое поле с меткой "Имя пользователя".
  - `age` — числовое поле с меткой "Введите возраст".

## Требования

- Python 3.8+
- Django 4.0+ (в проекте используется 6.0.3)

## Установка и запуск

1. Клонируйте репозиторий:
   bash git clone https://github.com/DorianQA-WEB/CRUD-Django.git cd CRUDProjectDjango\

2. Создайте виртуальное окружение и активируйте его:
    bash python -m venv .venv source .venv/bin/activate # Linux/Mac
    или
    .venv\Scripts\activate # Windows

3. Установите зависимости (если есть requirements.txt):
    bash pip install -r requirements.txt

4. Выполните миграции:
    bash python manage.py makemigrations python manage.py migrate

5. Запустите сервер:
    bash python manage.py runserver

6. Перейдите в браузере по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)


   
   
   
