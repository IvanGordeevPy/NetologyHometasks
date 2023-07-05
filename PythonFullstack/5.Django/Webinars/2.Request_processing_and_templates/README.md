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