from django.urls import path, include

from games.views import (MathFactsView, AnagramHuntView, 
    GameScoresView, record_score,
    MathScoresView, AnagramScoresView,                 
    MyScoresView, MyMscoresAllView, MyAscoresAllView
)

from pages.views import HomePageView

app_name = 'games'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('record-score/', record_score, name="record-score"),
    path('game-scores/', GameScoresView.as_view(), name="game-scores"),
    path('math-scores/', MathScoresView.as_view(), name="math-scores"),
    path('anagram-scores/', AnagramScoresView.as_view(), name="anagram-scores"),
    path('myscores/', MyScoresView.as_view(), name='myscores'),
    path('mymscores/', MyMscoresAllView.as_view(), name='mymscores'),
    path('myascores/', MyAscoresAllView.as_view(), name='myascores'),
]