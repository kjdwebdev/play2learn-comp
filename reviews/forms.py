from django.forms import ModelForm, Textarea
from .models import Review

# Create your views here.
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'stars', 'review' ]
        widgets = {
            'review': Textarea(
                attrs={'cols': 80, 'rows': 3, 'autofocus': True}
            )
        }
