from django.shortcuts import render
from a1test.models import *
# Create your views here.

def viewQuestion(request, kinds):
    if kinds != 'all':
        question = Question.objects.filter(kind=kinds)
    else:
        question = Question.objects.all()
        
    return render(request, 'question.html', {'questions': question})

def StudyHome(request):
    obj = exam.objects.all()
    return render(request, 'study.html', {'exams': obj})