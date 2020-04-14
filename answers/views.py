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
            if fuzz.ratio(obj.question_1, obj.this_round.answer_1) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_1
            if fuzz.ratio(obj.question_2, obj.this_round.answer_2) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_2
            if fuzz.ratio(obj.question_3, obj.this_round.answer_3) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_3
            if fuzz.ratio(obj.question_4, obj.this_round.answer_4) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_4
            if fuzz.ratio(obj.question_5, obj.this_round.answer_5) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_5
            if fuzz.ratio(obj.question_6, obj.this_round.answer_6) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_6
            if fuzz.ratio(obj.question_7, obj.this_round.answer_7) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_7
            if fuzz.ratio(obj.question_8, obj.this_round.answer_8) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_8
            if fuzz.ratio(obj.question_9, obj.this_round.answer_9) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_9
            if fuzz.ratio(obj.question_10, obj.this_round.answer_10) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_10
            if fuzz.ratio(obj.question_11, obj.this_round.answer_11) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_11
            if fuzz.ratio(obj.question_12, obj.this_round.answer_12) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_12
            if fuzz.ratio(obj.question_13, obj.this_round.answer_13) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_13
            if fuzz.ratio(obj.question_14, obj.this_round.answer_14) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_14
            if fuzz.ratio(obj.question_15, obj.this_round.answer_15) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_15
            if fuzz.ratio(obj.question_16, obj.this_round.answer_16) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_16
            if fuzz.ratio(obj.question_17, obj.this_round.answer_17) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_17
            if fuzz.ratio(obj.question_18, obj.this_round.answer_18) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_18
            if fuzz.ratio(obj.question_19, obj.this_round.answer_19) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_19
            if fuzz.ratio(obj.question_20, obj.this_round.answer_20) > 80:
                if obj.score == None: obj.score = 0
                obj.score += obj.this_round.score_20
            obj.save()
            return HttpResponseRedirect('thanks/')
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
            return HttpResponseRedirect('signupthanks/')
    signup_form = TeamForm()
    context = {
        'signup_form': signup_form
    }
    return render(request, "answers/signup.html", context)

def leaderboard(request):
    r1_results = Result.objects.filter(this_round__round_number=1).order_by('score')
    r2_results = Result.objects.filter(this_round__round_number=2).order_by('score')
    r3_results = Result.objects.filter(this_round__round_number=3).order_by('score')
    r4_results = Result.objects.filter(this_round__round_number=4).order_by('score')
    r5_results = Result.objects.filter(this_round__round_number=5).order_by('score')
    r6_results = Result.objects.filter(this_round__round_number=6).order_by('score')
    context = {
        'r1_results': r1_results,
        'r2_results': r2_results,
        'r3_results': r3_results,
        'r4_results': r4_results,
        'r5_results': r5_results,
        'r6_results': r6_results,
    }
    return render(request, "answers/leaderboard.html", context)

def signupthanks(request):
    message = "You are now signed up"
    return render(request, "answers/thanks.html")

def thanks(request):
    message = "Your answers have been submitted. Follow the link at the top of the page to submit more"
    return render(request, "answers/thanks.html")