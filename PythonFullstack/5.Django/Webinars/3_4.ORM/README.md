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

##**views.py**##
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