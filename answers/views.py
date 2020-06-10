from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .models import Team, Round, Result
from .forms import ResultForm, TeamForm
from quiz import settings
from fuzzywuzzy import fuzz, process

def markertron4000(question, answer, score, round_score, log):
    if len(answer) > 0:
        if fuzz.ratio(question.lower(), answer.lower()) > 75 or answer.lower() in question.lower():
            score += round_score
            log = log + question + ' matches ' + answer + '. Adding ' + str(round_score) + '\n'
        elif question.lower() in answer.lower() and len(question) > 1:
            score += round_score
            log = log + question + ' matches ' + answer + '. Adding ' + str(round_score) + '\n'
        else:
            log = log + question + ' does not match ' + answer + '\n'
    return score, log

def send_bingo_links(request):
    for team in Team.objects.all():
        send_mail(
                "Quiz Bingo Card Link",
                "Hello %s, please use this link for the bingo card for the quiz:\n\n%s" % (team.team_name, team.bingo_link),
                settings.EMAIL_FROM_ADDRESS,
                [team.team_email],
                fail_silently=True
            )
    return HttpResponseRedirect('/')

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
            if obj.this_team.team_email:
                message = "Here are your results for round %s : %s\nYour team name is %s\nScore: %s\n\nAnswers:\n%s" \
                    % (obj.this_round.round_number, obj.this_round.round_name, obj.this_team.team_name, obj.score, obj.log)
                send_mail(
                    "Quiz Results for Team: %s Round: %s" % (obj.this_team.team_name, obj.this_round.round_name),
                    message,
                    settings.EMAIL_FROM_ADDRESS,
                    [obj.this_team.team_email],
                    fail_silently=True
                )
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
            obj = form.save()
            if obj.team_email:
                message = "You are now registered for the quiz. Your team name is %s" % obj.team_name
                send_mail(
                    "Quiz Registration",
                    message,
                    settings.EMAIL_FROM_ADDRESS,
                    [obj.team_email],
                    fail_silently=True
                )
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
    r7_results = Result.objects.filter(this_round__round_number=7).order_by('-score')
    totals = []
    for team in Team.objects.all():
        total_score = 0.0
        for result in Result.objects.filter(this_team__team_name=team):
            total_score += result.score
        totals.append([team.team_name, total_score])
    context = {
        'r1_results': r1_results,
        'r2_results': r2_results,
        'r3_results': r3_results,
        'r4_results': r4_results,
        'r5_results': r5_results,
        'r6_results': r6_results,
        'r7_results': r7_results,
        'totals': totals
    }
    return render(request, "answers/leaderboard.html", context)

def signupthanks(request):
    message = "You are now signed up"
    return render(request, "answers/thanks.html", {'message': message})

def thanks(request):
    message = "Your answers have been submitted. Follow the link at the top of the page to submit more"
    return render(request, "answers/thanks.html", {'message': message})