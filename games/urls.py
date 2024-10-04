from django.urls import path, include

from games.views import MathFactsView, AnagramHuntView, AnagramHuntScoresView, MathFactsScoresView
from pages.views import HomePageView

app_name = 'games'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('anagram-scores', AnagramHuntScoresView.as_view(), name='anagram-scores'),
    path('math-scores', MathFactsScoresView.as_view(), name='math-scores'),
]