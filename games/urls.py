from django.urls import path, include

from games.views import (MathFactsView, AnagramHuntView, 
    AscoreListView, AscoreDetailView, MscoreListView, MscoreDetailView,
    MyascoreListView, MymscoreListView
)
from pages.views import HomePageView

app_name = 'games'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    
    path('ascore/', AscoreListView.as_view(), name='ascore'),
    path('<slug>/adetail/', AscoreDetailView.as_view(), name='adetail'),
    path('myascore/', MyascoreListView.as_view(), name='myascore'),
    path('mscore/', MscoreListView.as_view(), name='mscore'),
    path('<slug>/mdetail/', MscoreDetailView.as_view(), name='mdetail'),
    path('mymscore/', MymscoreListView.as_view(), name='mymscore'),
]