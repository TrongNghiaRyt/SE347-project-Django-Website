from django.shortcuts import render
from .models import Question
from .models import *
from django.http import HttpResponse

# Libary for python
from itertools import chain
# Create your views here.

def a1(request):
    question = Question.objects.all()
    return render(request, 'a1Test.html', {'questions': question})

def test(request, eid):
    examination = exam.objects.get(name='A1')

    kn = QuestionType.objects.filter(exam_type=examination.id).get(kinds='KN')
    kn_question = Question.objects.filter(kind='KN').order_by('?')[:kn.number]

    qt =  QuestionType.objects.filter(exam_type=examination.id).get(kinds='QT')
    qt_question = Question.objects.filter(kind='QT').order_by('?')[:qt.number]

    vh = QuestionType.objects.filter(exam_type=examination.id).get(kinds='VH')
    vh_question = Question.objects.filter(kind='VH').order_by('?')[:vh.number]

    td = QuestionType.objects.filter(exam_type=examination.id).get(kinds='TD')
    td_question = Question.objects.filter(kind='TD').order_by('?')[:td.number]

    bb = QuestionType.objects.filter(exam_type=examination.id).get(kinds='BB')
    bb_question = Question.objects.filter(kind='BB').order_by('?')[:bb.number]

    sh = QuestionType.objects.filter(exam_type=examination.id).get(kinds='SH')
    sh_question = Question.objects.filter(kind='SH').order_by('?')[:sh.number]

    question = list(chain(kn_question, qt_question, vh_question, td_question, bb_question, sh_question))
    return render(request, 'a1Test.html', {'questions': question, 'exams': examination})

def result(request, exam_id):
    examination = exam.objects.get(id=exam_id)
    question_pass = 0

    _question = set()
    _answer = set()

    answer_list = request.POST.getlist('answer')
    for ans in answer_list:
        _ans = Answer.objects.get(id=ans)
        _answer.add(_ans)

        q = Question.objects.get(id=_ans.question_id)
        _question.add(q)

    ansList = list()
    corrList = list()

    for q in _question:
        correct = Answer.objects.filter(question_id=q.id).filter(correct=True)
        _ansList = list()
        _corrList = list()
        #get a list of correct answer from database
        for c in correct:
            corrList.append(c.id)
            _corrList.append(c.id)

        for aid in _answer:
            if aid.question_id == q.id:
                ansList.append(aid.id)
                _ansList.append(aid.id)

        if _ansList == _corrList:
            question_pass += 1
    
    #Get questions list
    id_list = request.POST.getlist('ques')
    question_list = list()
    for q in id_list:
        _q = Question.objects.get(id=q)
        question_list.append(_q)

    obj = {'point': question_pass, 'exam': examination, 'questions': question_list, 'ans': ansList, 'corr': corrList}
    #return render(request, 'a1Test.html', {'questions': _question)
    return render(request, 'a1Result.html', obj)