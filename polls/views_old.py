from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.template import loader
from django.urls import reverse
from polls.models import Question, Choice

'''
В нашем приложении для опроса будут следующие четыре представления:
- Главная страница вопросов - отображает последние несколько вопросов.
- Страница вопроса - отображает текст вопроса, без результатов,
но с формой для голосования.
- Страница результатов вопроса - отображает результаты
для конкретного вопроса.
- Голосования - обрабатывает голосование за определенный выбор
в конкретном вопросе.'''


def index(request):
    # # from django.http import Http404
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
'''
Функция render() принимает объект запроса в качестве первого аргумента,
имя шаблона в качестве второго аргумента и
словарь в качестве необязательного третьего аргумента.
Она возвращает объект HttpResponse данного шаблона.'''


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #! повторное отображение формы
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        #! Всегда возвращайте HttpResponseRedirect после успешной обработки
        #! с данными POST. Это предотвращает публикацию данных дважды, если
        #! пользователь нажимает кнопку "Назад"
'''
После того, как кто-то проголосовал в опросе, представление voice()
перенаправляет на страницу результатов для опроса. '''


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})
