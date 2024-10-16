from django.views.generic import TemplateView,ListView
from games.models import Ascore, Mscore
from games.forms import AscoreForm, MscoreForm
from games.views import (AleaderListView, MleaderListView, 
    AnagramHuntView, MathFactsView, 
    AscoreDetailView, MscoreDetailView, 
    AscoreListView, MscoreListView
)