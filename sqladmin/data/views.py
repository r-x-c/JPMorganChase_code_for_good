from django.shortcuts import render
from models import UserT, AnswerT, QuestionT

from httplib import HTTPResponse
from django.shortcuts import redirect


def pull_user_data(target_id):
    django_queryset = UserT(user_id=target_id)

    return django_queryset


def detail(request, question_id):
    return HTTPResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    print(question_id)
    django_queryset = QuestionT(question_id=question_id)
    print(question_id)
    response = "You're looking at the results of question %s. {}".format(django_queryset)
    print(django_queryset)
    print(question_id)
    return HTTPResponse(response)

def vote(request, question_id):
    return HTTPResponse("You're voting on question %s." % question_id)

def staticTest(request):
    #response = "Displaying test"
    return redirect("https://www.google.com")

# Create your views here.
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
