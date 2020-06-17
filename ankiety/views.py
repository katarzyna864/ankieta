from django.http import Http404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice
from .models import Question, Vote, User, User2, Vote2
from django.contrib import messages
import hashlib
import time
import random

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('ankiety/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def adminpanel(request):
    template = loader.get_template('ankiety/adminpanel.html')
    context = {}
    return HttpResponse(template.render(context, request))

def useranswers(request):
    id = request.POST['user_id'].encode('ascii')
    all_objects = Vote.objects.all()
    all_objects2 = Vote2.objects.all()
    a = {}
    i = 0
    for obj in all_objects:
        hash = hashlib.sha256(str(obj.date).encode('ascii') + str(obj.voted_choice_id).encode('ascii') +
                              str(obj.voted_question_id).encode('ascii') + str(obj.voted_answer).encode('utf-8')).hexdigest()
        if hash == id.decode('ascii'):
            a[i] = 'found'
            i += 1
    if a.get(0) != 'found':
        for obj in all_objects2:
            hash = hashlib.sha256(str(obj.date).encode('ascii') + str(obj.voted_choice_id).encode('ascii') +
                                  str(obj.voted_question_id).encode('ascii') + str(obj.voted_answer).encode(
                'utf-8')).hexdigest()
            if hash == id.decode('ascii'):
                a[i] = 'found'
                i += 1
    return render(request, 'ankiety/useranswers.html', {'user': a})

def whetheranswered(request):
    id2 = request.POST['user_id2'].encode('utf-8')
    qid = request.POST['qid'].encode('ascii')
    all_objects = User.objects.all()
    all_objects2 = User2.objects.all()
    a = {}
    i = 0
    for obj in all_objects:
        if(obj.username.encode('utf-8') == id2 and str(obj.question).encode('ascii') == qid):
            a[i] = 'found'
            i += 1
    if a.get(0) != 'found':
        for obj in all_objects2:
            if (obj.username.encode('utf-8') == id2 and str(obj.question).encode('ascii') == qid):
                a[i] = 'found'
                i += 1
    return render(request, 'ankiety/whetheranswered.html', {'user': a})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Pytanie nie istnieje")
    return render(request, 'ankiety/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'ankiety/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    date = time.asctime()
    datehash = hashlib.sha256(str(date).encode('ascii')).hexdigest()

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        username = request.POST['user_id'].encode('utf-8')

        id_hash = hashlib.sha256(str(datehash).encode('ascii') + str(selected_choice.id).encode('ascii') +
                                 str(selected_choice.question_id).encode('ascii') + str(selected_choice.choice_text).encode('utf-8')).hexdigest()
        messages.info(request, 'Identyfikator Twojej odpowiedzi to: ' + id_hash)

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'ankiety/detail.html', {
            'question': question,
            'error_message': "Nie wybrałeś odpowiedzi.",
        })
    else:
        rand = random.randint(0, 1)
        if rand == 1:
            vote_data = Vote(date=datehash, voted_choice=selected_choice, voted_question=question, voted_answer=selected_choice.choice_text)
            vote_data.save()
        else:
            vote_data = Vote2(date=datehash, voted_choice=selected_choice, voted_question=question, voted_answer=selected_choice.choice_text)
            vote_data.save()

        rand = random.randint(0, 1)
        if rand == 1:
            user_data = User(username=username.decode(), question=question.id)
            user_data.save()
        else:
            user_data = User2(username=username.decode(), question=question.id)
            user_data.save()

        return HttpResponseRedirect(reverse('ankiety:results', args=(question.id,)))

