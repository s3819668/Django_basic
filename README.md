# Django

### 建立專案

```python
django-admin startproject HelloWorld
```

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled.png)

Terminal

```python

cd HelloWorld 
python manage.py runserver
```

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%201.png)

### HttpResponse

建立views.py

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%202.png)

```python
from django.http import HttpResponse
def Hello(request):
    return HttpResponse("Hello world")
```

將view.py加入urls.py

```python
**from django.urls import include, re_path
from . import views**
urlpatterns = [
    path('admin/', admin.site.urls),
    **re_path(r'^$',views.Hello)**
]
```

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%203.png)

---

# Template

新增templates資料夾

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%204.png)

templates下新增index.html

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%205.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{name}}</title>
</head>
<body>
		<h1>{{name}}</h1>
</body>
</html>
```

HelloWorld/setting.py

```html
import os
```

```html
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        **'DIRS': [os.path.join(BASE_DIR,"templates")],**
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

HelloWorld/views.py

```python
from django.shortcuts import render
def index(request):
    context={}
    context["name"]="Salmon"
    return render(request,"index.html",context)
```

HelloWorld/urls.py

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    **re_path('index/',views.index)**
]
```

[http://127.0.0.1:8000/index/](http://127.0.0.1:8000/index/)

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%206.png)

新增statics資料夾

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%207.png)

HelloWorld/setting.py

```python
STATIC_URL = 'static/'
**STATICFILE_DIRS=[
    os.path.join(BASE_DIR,"statics")
]**
```

statics新增css images js plugins 資料夾

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%208.png)

下載bootstrap  >Compiled CSS and JS 解壓縮放到 plugins下

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%209.png)

選擇要得樣式>檢查>copy html to tmplates/index.html    <body></body>

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2010.png)

[http://127.0.0.1:8000/index/](http://127.0.0.1:8000/index/) 

沒有看到bootstrap 效果只有吃到html

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2011.png)

[https://studygyaan.com/django/how-to-integrate-bootstrap-4-template-in-django](https://studygyaan.com/django/how-to-integrate-bootstrap-4-template-in-django) bootstrap路徑失敗看這篇

HelloWorld/setting.py

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'statics'),
)
**STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')**
```

Template/index.html 第一行加入  及引入local CDN

```html
**{% load static %}**
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{name}}</title>

    **<link href="{% static 'plugins/bootstrap-5.2.3-dist/css/bootstrap.css' %}" rel="stylesheet">**
</head>
<body>
		<h1>{{name}}</h1>
</body>
```

---

# Html 繼承

templates下新增base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Base</title>
</head>
<body>
    {{name}}
    {%block mainBody%}
    {%endblock mainBody%}
</body>
</html>
```

刪除templates/index.html的內容 並修改為

```html
{%extends "base.html"%}
{%block mainBody%}
<h1>繼承者</h1>
{%endblock mainBody%}
```

刷新 [http://127.0.0.1:8000/index/](http://127.0.0.1:8000/index/)

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2012.png)

templates新增index2.html

```html
{%extends "base.html"%}
{%block mainBody%}
<h1>2號繼承者</h1>
{%endblock mainBody%}
```

HelloWorld/view.py 新增

```python
def index1(request):
    context={}
    context["name"]="TORO"
    return render(request,"index1.html",context)
```

HelloWorld/urls.py新增

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('index/',views.index)**,**
    **re_path('index1/',views.index1)**
]
```

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2013.png)

---

HelloWorld/views.py 新增資料結構測試

```python
def index(request):
    context={}
    context["name"]="Salmon"

    **skill_list=["python","mysql","js"]
    context["skill_list"]=skill_list

    skill_dict={"python":"familar","mysql":"medium","js":"beinger"}
    context["skill_dict"]=skill_dict

    age="24"
    context["age"]=age**
		**empty=[]
    context["empty"]=empty**
    return render(request,"index.html",context)
```

templates/index.html 測試資料結構呼叫

```
{%extends "base.html"%}
{%block mainBody%}
<h1>繼承者</h1>
**{{name}}{{age}}<br>
skill:{{skill_list.0}},{{skill_list.1}},{{skill_list.2}}<br>
python:{{skill_dict.python}},mysql:{{skill_dict.mysql}},js:{{skill_dict.js}}
{#註解註解#}

{% if age > 30  %}
老人
{% elif age > 20  %}
年輕人
{% else  %}
小屁孩
{% endif %}

{% for i in skill_list %}
{{i}}
{% endfor %}
<br>

{% for k,v in skill_dict.items %}
{{k}}:{{v}}
{% endfor %}

{% for i in empty %}
{% empty %}
<p>空</p>
{% endfor %}**

{%endblock mainBody%}
```

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2014.png)

---

# 自定義tag

template新增my_tags.py

```python
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def mul(v1,v2,v3):
    return v1*v2*v3

@register.simple_tag
def my_input(v1,v2):
    temp_html='''
    <div>
        <span id=%s></span>
        <input type="text" id="%s">
    </div>'''%(v1,v2)
    return mark_safe(temp_html)
```

HelloWorld/setting.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            **'libraries':{
             'my_tags':'templates.my_tags'
            }**
        },
    },
]
```

template/index.html

最上面載入tag

```html
{% load my_tags %}
```

```html
<p>自定義標籤 {% mul 11 22 33 %}</p>
{% my_input "username_input" "UserName" %}
```

---

# header 繼承

templates新增header.html

base.html 的head刪除改為 `{% include "header.html" %}`

```html
<!DOCTYPE html>
<html lang="en">
    **{% include "header.html" %}**
<body>
<div class="container">
    <header class="d-flex justify-content-center py-3">
      <ul class="nav nav-pills">
        <li class="nav-item"><a href="#" class="nav-link active" aria-current="page">Home</a></li>
        <li class="nav-item"><a href="#" class="nav-link">Features</a></li>
        <li class="nav-item"><a href="#" class="nav-link">Pricing</a></li>
        <li class="nav-item"><a href="#" class="nav-link">FAQs</a></li>
        <li class="nav-item"><a href="#" class="nav-link">About</a></li>
      </ul>
    </header>
  </div>

    {{name}}
    {%block mainBody%}
    {%endblock mainBody%}
</body>
</html>
```

---

# 過濾器{{ var | fun}}

fun[ lower,upper,truncatewords:”<num>”]

templates/index.html

```html
**{% for k,v in skill_dict.items %}
{{k | upper}}:{{v | lower}}
{% endfor %}**
```

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2015.png)

## 自定義過濾器

建立tmplates/my_tags.py

```python
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def mul(v1,v2,v3):
    return v1*v2*v3

@register.simple_tag
def my_input(v1,v2):
    temp_html='''
    <div>
        <span id=%s></span>
        <input type="text" id="%s">
    </div>'''%(v1,v2)
    return mark_safe(temp_html)
**@register.filter
def my_filter(v1,v2):
    return v1*v2**
```

參考自定義tag [setting.py](http://setting.py) 

```html
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            **'libraries':{
             'my_tags':'templates.my_tags'
            }**
        },
    },
]
```

tmplates/index.html

如果沒有load過

```python
{% load my_tags %}

**<p>總分(學分*該科成績):{{score | my_filter:3}}</p>**
```

HelloWorld/view.py

```python
def index(request):
~

**score=80
context["score"]=score**

~
```

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2016.png)

---

# MySQL(by XAMPP)

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2017.png)

```python
pip install pymysql
```

HelloWorld/setting.py  修改Database

```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        **'ENGINE':'django.db.backends.mysql',
        'NAME':'django_basic',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':''**
    }
}
```

HelloWorld/__init__.py

```python
import pymysql
pymysql.install_as_MySQLdb()
```

cd到root目錄(可以跑manage.py那層)

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2018.png)

```python
django-admin startapp TestModel
```

TestModel/models.py

```python
from djangfo.db import models

class Test(models.Model):
    name=models.CharField(max_length=20) 

```

HelloWorld/setting.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    **'TestModel',**
]
```

建立預設表

command

```python
python manage.py migrate
```

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2019.png)

建立自定義遷移

```python
python manage.py makemigrations TestModel
```

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2020.png)

使用遷移建立新表

```python
python manage.py migrate TestModel
```

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2021.png)

---

## 新增

重複上面 TestModel/models.py

```python
from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=20)
    **age=models.IntegerField(default=0)**
```

command

```python
python manage.py makemigrations TestModel
python manage.py migrate TestModel
```

HelloWorld/新增testdb.py

```python
from django.http import HttpResponse
from TestModel.models import Test

def add(request):
    name=request.GET.get('name')
    age=request.GET.get('age')
    test=Test(name=name,age=age)
    test.save()
    return HttpResponse("success")
```

HelloWorld/url.py

```python
from django.contrib import admin
from django.urls import path

from django.urls import include, re_path
from . import views**,testdb**

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('index/',views.index),
    re_path('index1/',views.index1),
    **re_path(r'db/add$',testdb.add),**
]
```

[http://127.0.0.1:8000/db/add?name=simon&age=24](http://127.0.0.1:8000/db/add?name=simon&age=24)

嘗試新增幾個人

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2022.png)

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2023.png)

## 取得所有數據

HelloWorld/testdb

```python
from django.http import HttpResponse
from TestModel.models import Test

def add(request):
    name=request.GET.get('name')
    age=request.GET.get('age')
    test=Test(name=name,age=age)
    test.save()
    return HttpResponse("success")

**def get_all(request):
    arr=Test.objects.all()
    response=""
    for people in arr:
        response+=people.name +" "
    return HttpResponse("<p>"+response+"</p>")**
```

HelloWorld/urls.py

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('index/',views.index),
    re_path('index1/',views.index1),
    re_path(r'db/add$',testdb.add),
    **re_path(r'db/get',testdb.get_all),**
]
```

[http://127.0.0.1:8000/db/get](http://127.0.0.1:8000/db/get)

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2024.png)

---

## 更新

HelloWorld/testdb.py

```python
**def update(request):
    id = request.GET.get('id')
    test=Test.objects.get(id=id)
    test.name="NoName"
    test.save()
    return HttpResponse("update")**
```

HelloWorld/urls.py

```python
from django.contrib import admin
from django.urls import path

from django.urls import include, re_path
from . import views,testdb

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('index/',views.index),
    re_path('index1/',views.index1),
    re_path(r'db/add$',testdb.add),
    re_path(r'db/get',testdb.get_all),
    **re_path(r'db/update$',testdb.update),**
]
```

[http://127.0.0.1:8000/db/update?id=2](http://127.0.0.1:8000/db/update?id=2)

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2025.png)

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2026.png)

---

## 刪除

HelloWorld/testdb.py

```python
def delete(request):
    id=request.GET.get('id')
    test=Test.objects.get(id=id)
    test.delete()
    return HttpResponse("delete")
```

HelloWorld/urls.py

```python
from django.contrib import admin
from django.urls import path

from django.urls import include, re_path
from . import views,testdb

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('index/',views.index),
    re_path('index1/',views.index1),
    re_path(r'db/add$',testdb.add),
    re_path(r'db/get',testdb.get_all),
    re_path(r'db/update$',testdb.update),
    **re_path(r'db/delete$',testdb.delete),**
]
```

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2027.png)

![Untitled](Django%20b3428f2d2fae4dbca68b1494acb8106c/Untitled%2028.png)