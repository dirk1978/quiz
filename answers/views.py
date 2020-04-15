from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Team, Round, Result
from .forms import ResultForm, TeamForm
from fuzzywuzzy import fuzz, process

def markertron4000(question, answer, score, round_score, log):
    if fuzz.ratio(question, answer) > 80 or answer.lower() in question.lower():
        score += round_score
        log = log + question + ' in ' + answer + '. Adding ' + str(round_score) + '\n'
    elif question.lower() in answer.lower():
        if len(question) > 5:
            score += round_score
            log = log + question + ' in ' + answer + '. Adding ' + str(round_score) + '\n'
    return score, log

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            log = ''
            (obj.score, log) = markertron4000(obj.question_1, obj.this_round.answer_1, obj.score, obj.this_round.score_1, log)
            (obj.score, log) = markertron4000(obj.question_2, obj.this_round.answer_2, obj.score, obj.this_round.score_2, log)
            (obj.score, log) = markertron4000(obj.question_3, obj.this_round.answer_3, obj.score, obj.this_round.score_3, log)
            (obj.score, log) = markertron4000(obj.question_4, obj.this_round.answer_4, obj.score, obj.this_round.score_4, log)
            (obj.score, log) = markertron4000(obj.question_5, obj.this_round.answer_5, obj.score, obj.this_round.score_5, log)
            (obj.score, log) = markertron4000(obj.question_6, obj.this_round.answer_6, obj.score, obj.this_round.score_6, log)
            (obj.score, log) = markertron4000(obj.question_7, obj.this_round.answer_7, obj.score, obj.this_round.score_7, log)
            (obj.score, log) = markertron4000(obj.question_8, obj.this_round.answer_8, obj.score, obj.this_round.score_8, log)
            (obj.score, log) = markertron4000(obj.question_9, obj.this_round.answer_9, obj.score, obj.this_round.score_9, log)
            (obj.score, log) = markertron4000(obj.question_10, obj.this_round.answer_10, obj.score, obj.this_round.score_10, log)
            (obj.score, log) = markertron4000(obj.question_11, obj.this_round.answer_11, obj.score, obj.this_round.score_11, log)
            (obj.score, log) = markertron4000(obj.question_12, obj.this_round.answer_12, obj.score, obj.this_round.score_12, log)
            (obj.score, log) = markertron4000(obj.question_13, obj.this_round.answer_13, obj.score, obj.this_round.score_13, log)
            (obj.score, log) = markertron4000(obj.question_14, obj.this_round.answer_14, obj.score, obj.this_round.score_14, log)
            (obj.score, log) = markertron4000(obj.question_15, obj.this_round.answer_15, obj.score, obj.this_round.score_15, log)
            (obj.score, log) = markertron4000(obj.question_16, obj.this_round.answer_16, obj.score, obj.this_round.score_16, log)
            (obj.score, log) = markertron4000(obj.question_17, obj.this_round.answer_17, obj.score, obj.this_round.score_17, log)
            (obj.score, log) = markertron4000(obj.question_18, obj.this_round.answer_18, obj.score, obj.this_round.score_18, log)
            (obj.score, log) = markertron4000(obj.question_19, obj.this_round.answer_19, obj.score, obj.this_round.score_19, log)
            (obj.score, log) = markertron4000(obj.question_20, obj.this_round.answer_20, obj.score, obj.this_round.score_20, log)
            obj.log = log
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
            return HttpResponseRedirect('../signupthanks/')
    signup_form = TeamForm()
    context = {
        'signup_form': signup_form
    }
    return render(request, "answers/signup.html", context)

def leaderboard(request):
    r1_results = Result.objects.filter(this_round__round_number=1).order_by('-score')
    r2_results = Result.objects.filter(this_round__round_number=2).order_by('-score')
    r3_results = Result.objects.filter(this_round__round_number=3).order_by('-score')
    r4_results = Result.objects.filter(this_round__round_number=4).order_by('-score')
    r5_results = Result.objects.filter(this_round__round_number=5).order_by('-score')
    r6_results = Result.objects.filter(this_round__round_number=6).order_by('-score')
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
    return render(request, "answers/thanks.html", {'message': message})

def thanks(request):
    message = "Your answers have been submitted. Follow the link at the top of the page to submit more"
    return render(request, "answers/thanks.html", {'message': message})