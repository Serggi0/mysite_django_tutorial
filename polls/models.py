import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone

'''
В нашем приложении для опроса мы создадим две модели: Question и Choice.
Question содержит вопрос и дату публикации.
Choice содержит два поля: текст выбора и подсчет голосов.
Каждый Choice связан с Question.
'''

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently',
    )  # использование декоратора display() для панели админки
    # https://django.fun/docs/django/ru/3.2/intro/tutorial07/

    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

