from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Question
from django.template import loader

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # # context는 템플릿에서 쓰이는 변수명과 Python 객체를 연결하는 사전형 값
    # context = {
    #     'latest_question_list': latest_question_list,
    # }

    # 위 방법에서 단축된 형태
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context) # context는 optional

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")