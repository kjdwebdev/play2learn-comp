from django.forms import ModelForm, Textarea
from .models import Ascore, Mscore

class AscoreForm(ModelForm):
    class Meta:
        model = Ascore
        fields = ['user', 'score', 'max_number', 'operation' ]

class MscoreForm(ModelForm):
    class Meta:
        model = Mscore
        fields = ['user', 'score', 'max_number', 'operation' ]