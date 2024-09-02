from django.urls import path
#from .views import HomePageView, AboutUsView, LoginView, ContactView, GamesView
from .views import HomePageView, AboutUsView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us', AboutUsView.as_view(), name='about-us'),
    #path('login', LoginView.as_view(), name='login'),
    #path('contact', ContactView.as_view(), name='contact'),
    #path('games', GamesView.as_view(), name='games'),
]
