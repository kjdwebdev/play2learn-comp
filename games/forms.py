from django.forms import ModelForm, Textarea
from .models import GameScore

class GameScoreForm(ModelForm):
    class Meta: GameScore
    fields = ['game', 'score', 'max_number', 'operation', 'user' ]