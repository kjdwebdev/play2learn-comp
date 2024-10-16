from django.urls import path, include

from games.views import (MathFactsView, AnagramHuntView, 
    AscoreListView, AscoreDetailView, MscoreListView, MscoreDetailView,
    MyascoreListView, MymscoreListView, AleaderListView, MleaderListView, AleaderList2View
)
from pages.views import HomePageView

app_name = 'games'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('aleader2/', AleaderList2View.as_view(), name='aleader2'),
    #anagrams
    path('ascore/', AscoreListView.as_view(), name='ascore'),
    path('<slug>/adetail/', AscoreDetailView.as_view(), name='adetail'),
    path('myascore/', MyascoreListView.as_view(), name='myascore'),
    path('aleader/', AleaderListView.as_view(), name='aleader'),
    #Math Facts
    path('mscore/', MscoreListView.as_view(), name='mscore'),
    path('<slug>/mdetail/', MscoreDetailView.as_view(), name='mdetail'),
    path('mymscore/', MymscoreListView.as_view(), name='mymscore'),
    path('mleader/', MleaderListView.as_view(), name='mleader'),
]