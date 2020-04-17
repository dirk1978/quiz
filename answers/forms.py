from django.forms import ModelForm
from .models import Result, Team

class ResultForm(ModelForm):
    class Meta:
        model = Result
        exclude = ['submitted','score', 'log']

class TeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = ['bingo_link']