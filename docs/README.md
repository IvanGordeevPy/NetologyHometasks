# **Django_Tutorial**

## **Алгоритм**
1. Настроить виртуальное окружение, создать проект Django, если не создан (инфа ниже), создание приложения `python manage.py startapp demo`
2. Настроить поля `USER` (postgres), `PASSWORD`(postgres), `ENGINE` (backends.sqlite3 или backends.postgresql) и `NAME` (имя будущей базы данных) переменной `DATABASES` в `settings.py` 
3. Описать классы в файле `models.py`, пример:
```
class OrderPosition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='positions')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions')
```
4. Зарегистрировать классы в `admin.py`, импортируя сами классы из модуля `.models` пример:
```
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'color',]
    list_filter = ['brand', 'model',]

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car',]

class OrderPositionInline(admin.TabularInline):
    model = OrderPosition
    extra = 3

@admin.register(Product)
class ProdictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['category']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [OrderPositionInline,]
```
5. Осуществить миграцию классов (создать описание базы данных):
*`python manage.py makemigrations`
*`python manage.py migrate`
6. Проверить, что 
7. Создать базу данных postgres: 
*`**createdb -U postgres demoorm`
*`pip install psycopg2-binary`
8. Для доступа к Django admnin создается суперпользователь:
`python manage.py createsuperuser`
9. Наполнить базу данных самими данными (`python manage.py loaddata school.json`)
10. Работа в файлах `views.py`, `urls.py` и папке `templates`
11. Запуск оболочки Django `python manage.py runserver`
12. Отладка (4 варианта описаны ниже в разделе Дебаг). Вызвать интерактивный интерпретатор: `python manage.py shell`

<details>
  <summary>Настройка проекта</summary>

## **Настройка проекта**
---
Должно существовать активированное виртуальное окружение Python. Как его установить:

1. Запустить VS Code от имени администратора, перейти в папку, где нужно будет установить виртуальное окружение. Перейти в каталог проекта в PowerShell, выполнить код ниже, появится папка env, содержащая файлы виртуального окружения

`py -m venv env`

2. Изменить политику, в PowerShell набрать (Хз, для чего это на самом деле)

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

3. Войти в папку окружения (env), выполнить команду

`env\Scripts\activate.ps1`

4. Впереди в PowerShell появится маркер окружения (env), но VS Code может о нем все еще ничего не знать. Нажать Ctrl+Shift + P, набрать Python: Select Interpreter
Указать нужный путь к python.exe в папке окружения env, это отобразится внизу в панели состояния. Профит! Теперь можно устанавливать модули только для конкретного проекта.

5. Если нужно будет выйти, то в PowerShell выполнить deactivate, в выборе интерпетатора вернуться на глобальный.

---
Установка библиотеки Django

`pip install Django`

Установка структуры Django

`django-admin startproject name .`, где name - имя проекта, оно же имя папки со структурой; "." - установка в корневой папке (той, которая выбрана в данный момент в терминале), вместо "." можно написать относительный путь папки, где хочется создать проект (при этом путь не должен содержать пробелы)

</details>

<details>
  <summary>Базовые команды</summary>

## **Базовые команды**
---
Перед запуском сервера требуется сохранить все изменения

`python manage.py runserver` - запустить сервер

`python manage.py startapp demo` - создать приложение (подсистему), где demo - имя приложения. После создания подсистемы обязательно в settings.py в списке INSTALLED_APPS вписывать путь до приложения относительно корня (регистрировать его). "Вход" в папку делается через точку, например "apps.demo"

`python manage.py shell` - интерактивный интерпретатор, выйти через `exit()`
</details>

<details>
  <summary>Дебаг</summary>

## **Дебаг**
---
Как дебажить:
**print-функции**
Django-проект — это Python приложение. Поэтому можно использовать возможности Python и использовать print’ы для дебага и отладки кода.

**Точки останова (они же breakpoints)**
Удобнее всего использовать в IDE Pycharm или VS Code.

**manage.py shell**
Чтобы ее запустить, требуется находится в корневой папке Django проекта в терминале Powershell
`python manage.py shell`
Запускает интерактивный интерпретатор в контексте Django- проекта.
`from django.urls import reverse` - импортировать функцию reverse
`reverse('demo')` - покажет URL путь до обработчика с именем demo (в urlpatterns должен быть третий аругмент с этим именем, либо можно обращаться через саму функцию, но не рекомендуется)

**Сообщения об ошибках Django**
Средство фреймворка. Если включен DEBUG-режим (по умолчанию во всех домашних работах именно так), то Django собирает и агрегирует информацию об ошибке.
</details>

<details>
  <summary>Дополнительная информация</summary>

## **Дополнительная информация**
---
Файл views.py - содержит обработчики (принимают запрос и отдают клиенту ответ)
Файл urls.py - содержит маршруты, которые будут вызывать сответствующие обработчики. Пустой путь задает обработчик, который будет вызван на главной странице

В Django придерживаемся паттерна MVC (model-view-controller), он переименован в MTV - не мешаем в одну кучу:
*Управление логикой при ответе - view
*Как будет выглядеть страница - template (model в MVC)
*Состояние приложения - model



[Документация Django](https://docs.djangoproject.com/en/4.2/)
[Учебник](https://developer.mozilla.org/ru/docs/Learn/Server-side/Django)
[Создание блога](https://tutorial.djangogirls.org/ru/)
[Типы данных для атрибутов моделей](https://docs.djangoproject.com/en/3.2/ref/models/fields/#model-field-types)

Для удобного мониторинга и отладки проекта можно установить специальную библиотеку - Django Debug Toolbar.

[Полное руководство по библиотеке](https://django-debug-toolbar.readthedocs.io/en/latest/index.html)

Чтобы запустить Django Debug Toolbar необходимо выполнить несколько действий:
установить библиотеку:
pip install django-debug-toolbar

Настроить переменную INSTALLED_APPS в settings.py: убедиться, что присутствует приложение django.contrib.staticfiles и добавить новое приложение debug_toolbar (обязательно добавить его после django.contrib.staticfiles):
```
INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    # ...
    'debug_toolbar',
]
Настроить переменную STATIC_URL в settings.py:
STATIC_URL = '/static/'
```
Убедиться, что в переменной TEMPLATES в settings.py параметр APP_DIRS установлен в значение True
Добавить в переменную MIDDLEWARE в settings.py в самое начало:
```
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]
```
Добавить переменную INTERNAL_IPS в settings.py:
```
INTERNAL_IPS = [
    '127.0.0.1',
]
```
Добавить маршрут в самый конец urlpatterns в файле urls.py:
```
import debug_toolbar
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    ...
    path('__debug__/', include(debug_toolbar.urls)),
] 
```
После выполнения всех действий при ответе сервера в браузере справа будет доступен инструмент Django Debug Toolbar.

[Пример настроенного проекта](https://github.com/jazzband/django-debug-toolbar/tree/main/example)
</details>

<details>
  <summary>Обработка запросов</summary>

## **Обработка запросов**
---
В `settings.py` можно добавлять свои собственные переменные и потом пользоваться ими в любом удобном месте.
Для получения значений из конфигурации, необходимо обращаться к полям в объекте settings:

[Django settings](https://docs.djangoproject.com/en/3.2/topics/settings/)
```
# именно так надо импортировать настройки
from django.conf import settings
from django.http import HttpResponse

def hello_view(request): 
    msg = f'Свяжитесь с админом {settings.CONTANCT_EMAIL}' 
    return HttpResponse('Всем привет! Я Django! ' + msg)
```

##**Работа с кодом**##
---
Работа в файлах views.py, urls.py, setting.py, demo.html

###**Get-запросы**###
Get - запросы передаются из браузера через `?name=Ivan&age=22`, где name, age - названия переменной, Ivan, 22 - значение переменной
Тогда в Django проекте в файле views.py следует написать код:
```
def hello(request):
    name = request.GET.get("name")
    age = int(request.GET.get("age", 20))
    print(age)
    return HttpResponse(f'Hello, {name}')
```
Метод .get безопасно возвращает значение переменной (если оно не будет передано в запросе, то ничего не сломается)
Второй параметр функции метода .get задает стандартное значение переменной

###**Конверторы**###
В `urlpatterns` можно использовать конверторы для параметров:
`path('sum/<int:op1>/<int:op2>/', sum),`, если op1 или op2 не будут целыми числами, то sum не будет вызван
[Стандартные конверторы](https://docs.djangoproject.com/en/3.2/topics/http/urls/#path-converters)
Можно создавать собственные конверторы, для этого нужно:
*Описать класс конвертера
*Зарегистрировать конвертер

Класс конвертера — это класс с определённым набором атрибутов и методов, описанных в документации (на мой взгляд, несколько странно, что разработчики не сделали базовый абстрактный класс). Сами требования:

Должен быть атрибут regex, описывающий регулярное выражение для быстрого поиска требуемой подпоследовательности. Чуть позже покажу, как он используется.
Реализовать метод def to_python(self, value: str) для конвертации из строки (ведь передаваемый маршрут — это всегда строка) в объект python, который в итоге будет передаваться в обработчик.
Реализовать метод def to_url(self, value) -> str для обратной конвертации из объекта python в строку (используется, когда вызываем django.urls.reverse или тег url).
Класс для конвертации даты будет выглядеть так:
```
class DateConverter:
   regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'

   def to_python(self, value: str) -> datetime:
       return datetime.strptime(value, '%Y-%m-%d')

   def to_url(self, value: datetime) -> str:
       return value.strftime('%Y-%m-%d')
```

Вынесем формат даты в атрибут для упрощения поддержки конвертера:
```
class DateConverter:
   regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
   format = '%Y-%m-%d'

   def to_python(self, value: str) -> datetime:
       return datetime.strptime(value, self.format)

   def to_url(self, value: datetime) -> str:
       return value.strftime(self.format)
```

По итогу описания класса можно зарегистрировать его как конвертер. Для этого в функции register_converter надо указать описанный класс и название конвертера, чтобы использовать его в маршрутах.
```
from django.urls import register_converter
register_converter(DateConverter, 'date')
```

Опишем маршруты в urls.py:
```
path('users/<int:id>/reports/<date:dt>/', user_report, name='user_report'),
path('teams/<int:id>/reports/<date:dt>/', team_report, name='team_report'),
```

Теперь гарантируется, что обработчики вызываются только в том случае, если конвертер отработает корректно, а это значит, что в обработчик придут параметры нужного типа:
```
def user_report(request, id: int, dt: datetime):
   больше никакой валидации в обработчиках
   сразу правильные типы и никак иначе
```

###**Контекст**###
В обработчиках файла views.py можно задавать контекст для использования в файле .html:
```
def django_hello(request):
    context = {
        'test': 5,
        'data': [1, 5, 8],
        'val': 'hello',
    }
    return render(request, 'demo.html', context)
    return HttpResponse()
```

###**Шаблоны**###
Шаблон итерации по объекту:
```
<ul>
{% student student_list %}
<li>{{ student.rating }}</li>
{% endfor %}
</ul>
```

Шаблон проверки условия:
```
{% user.is_authenticated %}
<p>Здравствуйте, {{ user.username }}!</p>
{% endif %}
```

Еще есть:
[Фильтры](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#built-in-filter-reference)
[Наследование](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#extends)
[Композиция](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#include)
[Собственные теги и фильтры](https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/)

###**Пагинация**###
`views.py`:
```
CONTENT = [str(i) for i in range(10000)]

def pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'pagi.html', context)
```

`pagi.html`:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% for e in page %}
<p>{{ e }}</p>
{% endfor %}

{% if page.has_previous %}
<a href="?page={{ page.previous_page_number }}">Назад</a>
{% endif %}
{% if page.has_next %}
<a href="?page={{ page.next_page_number }}">Вперед</a>
{% endif %}
</body>
</html>
```

И зарегестрировать в urls.py
</details>

<details>
  <summary>ORM (Работа с БД через код)</summary>

## **ORM (Работа с БД через код)**
---
Работа в models.py, settings.my, django-admin, admin.py

`models.py`:
```
class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

class Person(models.Model):
    name = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
```

Файл миграций описывает, какие операции нужно провести над базой данных, чтобы она соответствовала текущей структуре (в django-admin)
`python manage.py makemigrations`

Создается системный файл в папке `migrations`. Эти миграции требуется применить для создания базы данных:
`python manage.py migrate`

Выбор базы данных производится в файле `settings.py` в разделе DATABASES
Пример смены базы данных на Postgres:
`createdb -U postgres demoorm` - создание базы данных demoorm
`dropdb -Upostgres demoorm` - удаление базы ранных (почему такой тупой синтаксис?)
`pip install psycopg2-binary` - установка драйвера для postgres
Меняем в разделе DATABASES данные с:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
на (USER и PASSWORD могут отличаться):
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'demoorm',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}
```
После чего применяем миграции снова:
`python manage.py migrate`

Для доступа к Django admnin создается суперпользователь:
`python manage.py createsuperuser`

[Типы данных для атрибутов моделей](https://docs.djangoproject.com/en/3.2/ref/models/fields/#model-field-types)
Например, можно реализовать магический метод str, чтобы получить желаемое отображение объекта при выводе на экран:
```
class Car(models.Model):
    …

    def __str__(self):
        return f'{self.brand}, {self.model}: {self.color}'
```

## **views.py**
```
import random

from demo.models import Car
from django.http import HttpResponse
from django.shortcuts import render

def create_car(request):
    car = Car(
        brand=random.choice(['B1', 'B2', 'B3']), 
        model=random.choice(['M1', 'M2', 'M3']), 
        color=random.choice(['C1', 'C2', 'C3']))
    car.save()
    return HttpResponse(f'Все получилось! Новая машина: {car.brand}, {car.model}')

def list_car(request):
    car_objects = Car.objects.filter(brand__contains='2')
    cars = [f'{c.id}: {c.brand}, {c.model}: {c.color}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))

def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        Person.objects.create(name='P', car=car)
    return HttpResponse('Все получилось!')
```

В `filter` еще можно передавать, например startswith

В create_person еще можно создавать так:
Person(name='P', car=car).save()
</details>
