from django.urls import path
#from .views import HomePageView, AboutUsView, LoginView, ContactView, GamesView
from .views import HomePageView, AboutUsView
#from games.views import AnagramHuntScoresListView, MathFactsScoresListView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us', AboutUsView.as_view(), name='about-us'),
    #path('anagram-scores', AnagramHuntScoresListView.as_view(), name='anagram-scores'),
    #path('math-scores', MathFactsScoresListView.as_view(), name='math-scores'),
    #path('games', GamesView.as_view(), name='games'),
]
