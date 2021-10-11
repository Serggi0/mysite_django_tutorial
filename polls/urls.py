from django.urls import path
from polls import views

app_name = 'polls' #! установка пространства имен приложения
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]
#! имя сопоставленного шаблона в строках пути второго и третьего шаблонов
#! изменилось с <question_id> на <pk>

