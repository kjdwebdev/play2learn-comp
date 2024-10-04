from django.forms import ModelForm, Textarea
from .models import AnagramHuntScores, MathFactsScores

class AnagramHuntScoresForm(ModelForm):
    class Meta:
        model = AnagramHuntScores
        fields = ['user', 'score', 'max_number', 'operation' ]

class MathFactsScoresForm(ModelForm):
    class Meta:
        model = MathFactsScores
        fields = ['user', 'score', 'max_number', 'operation' ]

