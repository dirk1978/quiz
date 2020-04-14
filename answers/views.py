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
            log = ''
            if fuzz.ratio(obj.question_1, obj.this_round.answer_1) > 80 or \
                obj.this_round.answer_1.lower() in obj.question_1.lower() or \
                obj.question_1.lower() in obj.this_round.answer_1.lower():
                if len(obj.question_1) > 5:
                    obj.score += obj.this_round.score_1
                    log = log + obj.question_1 + ' in ' + obj.this_round.answer_1 + '. Adding ' + \
                        str(obj.this_round.score_1) + '\n'
            if fuzz.ratio(obj.question_2, obj.this_round.answer_2) > 80 or \
                obj.this_round.answer_2.lower() in obj.question_2.lower() or \
                obj.question_2.lower() in obj.this_round.answer_2.lower():
                if len(obj.question_2) > 5:
                    obj.score += obj.this_round.score_2
                    log = log + obj.question_2 + ' in ' + obj.this_round.answer_2 + '. Adding ' + \
                        str(obj.this_round.score_2) + '\n'
            if fuzz.ratio(obj.question_3, obj.this_round.answer_3) > 80 or \
                obj.this_round.answer_3.lower() in obj.question_3.lower() or \
                obj.question_3.lower() in obj.this_round.answer_3.lower():
                if len(obj.question_3) > 5:
                    obj.score += obj.this_round.score_3
                    log = log + obj.question_3 + ' in ' + obj.this_round.answer_3 + '. Adding ' + \
                        str(obj.this_round.score_3) + '\n'
            if fuzz.ratio(obj.question_4, obj.this_round.answer_4) > 80 or \
                obj.this_round.answer_4.lower() in obj.question_4.lower() or \
                obj.question_4.lower() in obj.this_round.answer_4.lower():
                if len(obj.question_4) > 5:
                    obj.score += obj.this_round.score_4
                    log = log + obj.question_4 + ' in ' + obj.this_round.answer_4 + '. Adding ' + \
                        str(obj.this_round.score_4) + '\n'
            if fuzz.ratio(obj.question_5, obj.this_round.answer_5) > 80 or \
                obj.this_round.answer_5.lower() in obj.question_5.lower() or \
                obj.question_5.lower() in obj.this_round.answer_5.lower():
                if len(obj.question_5) > 5:
                    obj.score += obj.this_round.score_5
                    log = log + obj.question_5 + ' in ' + obj.this_round.answer_5 + '. Adding ' + \
                        str(obj.this_round.score_5) + '\n'
            if fuzz.ratio(obj.question_6, obj.this_round.answer_6) > 80 or \
                obj.this_round.answer_6.lower() in obj.question_6.lower() or \
                obj.question_6.lower() in obj.this_round.answer_6.lower():
                if len(obj.question_6) > 5:
                    obj.score += obj.this_round.score_6
                    log = log + obj.question_6 + ' in ' + obj.this_round.answer_6 + '. Adding ' + \
                        str(obj.this_round.score_6) + '\n'
            if fuzz.ratio(obj.question_7, obj.this_round.answer_7) > 80 or \
                obj.this_round.answer_7.lower() in obj.question_7.lower() or \
                obj.question_7.lower() in obj.this_round.answer_7.lower():
                if len(obj.question_7) > 5:
                    obj.score += obj.this_round.score_7
                    log = log + obj.question_7 + ' in ' + obj.this_round.answer_7 + '. Adding ' + \
                        str(obj.this_round.score_7) + '\n'
            if fuzz.ratio(obj.question_8, obj.this_round.answer_8) > 80 or \
                obj.this_round.answer_8.lower() in obj.question_8.lower() or \
                obj.question_8.lower() in obj.this_round.answer_8.lower():
                if len(obj.question_8) > 5:
                    obj.score += obj.this_round.score_8
                    log = log + obj.question_8 + ' in ' + obj.this_round.answer_8 + '. Adding ' + \
                        str(obj.this_round.score_8) + '\n'
            if fuzz.ratio(obj.question_9, obj.this_round.answer_9) > 80 or \
                obj.this_round.answer_9.lower() in obj.question_9.lower() or \
                obj.question_9.lower() in obj.this_round.answer_9.lower():
                if len(obj.question_9) > 5:
                    obj.score += obj.this_round.score_9
                    log = log + obj.question_9 + ' in ' + obj.this_round.answer_9 + '. Adding ' + \
                        str(obj.this_round.score_9) + '\n'
            if fuzz.ratio(obj.question_10, obj.this_round.answer_10) > 80 or \
                obj.this_round.answer_10.lower() in obj.question_10.lower() or \
                obj.question_10.lower() in obj.this_round.answer_10.lower():
                if len(obj.question_10) > 5:
                    obj.score += obj.this_round.score_10
                    log = log + obj.question_10 + ' in ' + obj.this_round.answer_10 + '. Adding ' + \
                        str(obj.this_round.score_10) + '\n'
            if fuzz.ratio(obj.question_11, obj.this_round.answer_11) > 80 or \
                obj.this_round.answer_11.lower() in obj.question_11.lower() or \
                obj.question_11.lower() in obj.this_round.answer_11.lower():
                if len(obj.question_11) > 5:
                    obj.score += obj.this_round.score_11
                    log = log + obj.question_11 + ' in ' + obj.this_round.answer_11 + '. Adding ' + \
                        str(obj.this_round.score_11) + '\n'
            if fuzz.ratio(obj.question_12, obj.this_round.answer_12) > 80 or \
                obj.this_round.answer_12.lower() in obj.question_12.lower() or \
                obj.question_12.lower() in obj.this_round.answer_12.lower():
                if len(obj.question_12) > 5:
                    obj.score += obj.this_round.score_12
                    log = log + obj.question_12 + ' in ' + obj.this_round.answer_12 + '. Adding ' + \
                        str(obj.this_round.score_12) + '\n'
            if fuzz.ratio(obj.question_13, obj.this_round.answer_13) > 80 or \
                obj.this_round.answer_13.lower() in obj.question_13.lower() or \
                obj.question_13.lower() in obj.this_round.answer_13.lower():
                if len(obj.question_13) > 5:
                    obj.score += obj.this_round.score_13
                    log = log + obj.question_13 + ' in ' + obj.this_round.answer_13 + '. Adding ' + \
                        str(obj.this_round.score_13) + '\n'
            if fuzz.ratio(obj.question_14, obj.this_round.answer_14) > 80 or \
                obj.this_round.answer_14.lower() in obj.question_14.lower() or \
                obj.question_14.lower() in obj.this_round.answer_14.lower():
                if len(obj.question_14) > 5:
                    obj.score += obj.this_round.score_14
                    log = log + obj.question_14 + ' in ' + obj.this_round.answer_14 + '. Adding ' + \
                        str(obj.this_round.score_14) + '\n'
            if fuzz.ratio(obj.question_15, obj.this_round.answer_15) > 80 or \
                obj.this_round.answer_15.lower() in obj.question_15.lower() or \
                obj.question_15.lower() in obj.this_round.answer_15.lower():
                if len(obj.question_15) > 5:
                    obj.score += obj.this_round.score_15
                    log = log + obj.question_15 + ' in ' + obj.this_round.answer_15 + '. Adding ' + \
                        str(obj.this_round.score_15) + '\n'
            if fuzz.ratio(obj.question_16, obj.this_round.answer_16) > 80 or \
                obj.this_round.answer_16.lower() in obj.question_16.lower() or \
                obj.question_16.lower() in obj.this_round.answer_16.lower():
                if len(obj.question_16) > 5:
                    obj.score += obj.this_round.score_16
                    log = log + obj.question_16 + ' in ' + obj.this_round.answer_16 + '. Adding ' + \
                        str(obj.this_round.score_16) + '\n'
            if fuzz.ratio(obj.question_17, obj.this_round.answer_17) > 80 or \
                obj.this_round.answer_17.lower() in obj.question_17.lower() or \
                obj.question_17.lower() in obj.this_round.answer_17.lower():
                if len(obj.question_17) > 5:
                    obj.score += obj.this_round.score_17
                    log = log + obj.question_17 + ' in ' + obj.this_round.answer_17 + '. Adding ' + \
                        str(obj.this_round.score_17) + '\n'
            if fuzz.ratio(obj.question_18, obj.this_round.answer_18) > 80 or \
                obj.this_round.answer_18.lower() in obj.question_18.lower() or \
                obj.question_18.lower() in obj.this_round.answer_18.lower():
                if len(obj.question_18) > 5:
                    obj.score += obj.this_round.score_18
                    log = log + obj.question_18 + ' in ' + obj.this_round.answer_18 + '. Adding ' + \
                        str(obj.this_round.score_18) + '\n'
            if fuzz.ratio(obj.question_19, obj.this_round.answer_19) > 80 or \
                obj.this_round.answer_19.lower() in obj.question_19.lower() or \
                obj.question_19.lower() in obj.this_round.answer_19.lower():
                if len(obj.question_19) > 5:
                    obj.score += obj.this_round.score_19
                    log = log + obj.question_19 + ' in ' + obj.this_round.answer_19 + '. Adding ' + \
                        str(obj.this_round.score_19) + '\n'
            if fuzz.ratio(obj.question_20, obj.this_round.answer_20) > 80 or \
                obj.this_round.answer_20.lower() in obj.question_20.lower() or \
                obj.question_20.lower() in obj.this_round.answer_20.lower():
                if len(obj.question_20) > 5:
                    obj.score += obj.this_round.score_20
                    log = log + obj.question_20 + ' in ' + obj.this_round.answer_20 + '. Adding ' + \
                        str(obj.this_round.score_20) + '\n'
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
    return render(request, "answers/thanks.html", {'message': message})

def thanks(request):
    message = "Your answers have been submitted. Follow the link at the top of the page to submit more"
    return render(request, "answers/thanks.html", {'message': message})