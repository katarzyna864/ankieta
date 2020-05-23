from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice
from .models import Question, Vote, User, Test
from datetime import date
from django.contrib import messages
import hashlib

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
    a = {}
    i = 0
    for obj in all_objects:
        if(obj.user_id.encode('ascii') == id):
            a[i] = 'found'
            i += 1
    return render(request, 'ankiety/useranswers.html', {'user': a})

def whetheranswered(request):
    id2 = request.POST['user_id2'].encode('ascii')
    all_objects = User.objects.all()
    a = {}
    i = 0
    for obj in all_objects:
        if(obj.username.encode('ascii') == id2):
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
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        a = request.POST['user_id'].encode('utf-8')
        id_hash = hashlib.sha256(a+d1.encode('ascii')+selected_choice.choice_text.encode('ascii')).hexdigest()
        # id_hash = hashlib.sha256(a).hexdigest()
        messages.info(request, 'Identyfikator Twojej odpowiedzi to: ' + id_hash)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'ankiety/detail.html', {
            'question': question,
            'error_message': "Nie wybrałeś odpowiedzi.",
        })
    else:
        b = Vote(user_id=id_hash, voted_choice=selected_choice, voted_question=question)
        b.save()

        c = User(username=a.decode())
        c.save()

        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('ankiety:results', args=(question.id,)))

