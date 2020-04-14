from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Team, Round, Result
from .forms import ResultForm, TeamForm
from fuzzywuzzy import fuzz, process

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if fuzz.ratio(obj.question_1,obj.this_round.answer_1) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_1
            if obj.question_2 == obj.this_round.answer_2:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_2
            if obj.question_3 == obj.this_round.answer_3:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_3
            if obj.question_4 == obj.this_round.answer_4:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_4
            if obj.question_5 == obj.this_round.answer_5:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_5
            if obj.question_6 == obj.this_round.answer_6:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_6
            if obj.question_7 == obj.this_round.answer_7:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_7
            if obj.question_8 == obj.this_round.answer_8:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_8
            if obj.question_9 == obj.this_round.answer_9:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_9
            if obj.question_10 == obj.this_round.answer_10:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_10
            if obj.question_11 == obj.this_round.answer_11:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_11
            if obj.question_12 == obj.this_round.answer_12:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_12
            if obj.question_13 == obj.this_round.answer_13:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_13
            if obj.question_14 == obj.this_round.answer_14:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_14
            if obj.question_15 == obj.this_round.answer_15:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_15
            if obj.question_16 == obj.this_round.answer_16:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_16
            if obj.question_17 == obj.this_round.answer_17:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_17
            if obj.question_18 == obj.this_round.answer_18:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_18
            if obj.question_19 == obj.this_round.answer_19:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_19
            if obj.question_20 == obj.this_round.answer_20:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_20
            obj.save()
            return HttpResponseRedirect('/quiz/thanks/')
    result_form = ResultForm()
    context = {
        'result_form': result_form
    }
    return render(request, "answers/index.html", context)

def signup(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/quiz/signupthanks/')
    signup_form = TeamForm()
    context = {
        'signup_form': signup_form
    }
    return render(request, "answers/signup.html", context)

def signupthanks(request):
    return render(request, "answers/signupthanks.html")

def thanks(request):
    return render(request, "answers/thanks.html")