from django.contrib import admin
from polls.models import Question, Choice

# admin.site.register(Question)



class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
# Это конкретное изменение приводит к тому, что «Дата публикации» предшествует
# полю «Вопрос». Настройка двух полей не впечатляет, но для административных
# форм с десятками полей выбор интуитивно понятного порядка является
# важной деталью удобства использования:
    # fields = ['pub_date', 'question_text']

# Добавление заголовков набора полей (первый элемент кортежа):

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']  # добавляет боковую панель «FILTER»
    search_fields = ['question_text'] # окно поиска в поле 'question_text'
    # https://django.fun/docs/django/ru/3.2/intro/tutorial07/
    #! добавление полей на странице question

admin.site.register(Question, QuestionAdmin)
#! Добавление своего приложения в админку
# admin.site.register(Choice)  # регистрация отдельно Choice в админке
