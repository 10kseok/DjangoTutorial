from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/specifics/1/ , name이 detali.html에서 url 장고태그 써서 인식할 때 사용됨. url 바꾸려면 템플릿말고 여기서 바꾸면 됌.
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/1/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
