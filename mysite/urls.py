from django.contrib import admin
from django.urls import path, include

import polls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'))
]
#Функция path() передает четыре аргумента, два обязательных: route и view, и два необязательных: kwargs и name. 
"""mysite URL Configuration
Функция include() позволяет ссылаться на другие URLconfs. Всякий раз, когда Django встречает include(), он отсекает любую часть URL-адреса, совпадающую с этой точкой, и отправляет оставшуюся строку во включенный URLconf для дальнейшей обработки.

Идея, стоящая за include(), состоит в том, чтобы упростить добавление и воспроизведение URL-адресов. Так как опросы находятся в их собственном URLconf(polls/urls.py), их можно поместить в «/polls/», или в «/fun_polls/», или в «/content/polls/», или по любому другому корневому пути, и приложение все равно будет работать.

"""