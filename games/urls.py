from django.urls import path, include

from games.views import MathFactsView, AnagramHuntView, AscoreListView, AscoreDetailView, MathFactsScoresListView, MathFactsScoresDetailView
from pages.views import HomePageView

app_name = 'games'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    
    path('ascore/', AscoreListView.as_view(), name='ascore'),
    path('<slug>/adetail/', AscoreDetailView.as_view(), name='adetail'),
    path('math-scores/', MathFactsScoresListView.as_view(), name='math-scores'),
    path('<slug>/math-score-detail/', MathFactsScoresDetailView.as_view(), name='math-score-detail'),
]