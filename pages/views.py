from django.views.generic import TemplateView,ListView
from reviews.models import Review
from reviews.forms import ReviewForm

# Create your views here.
# Home Page
class HomePageView(ListView):
    model=Review
    template_name = 'pages/home.html'

    def get_queryset(self):
      qs = Review.objects.all()
      return qs.filter(featured=True)
    
# About Us
class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'
'''
# Games
class GamesView(TemplateView):
    template_name = 'pages/games.html'

# Login
class LoginView(TemplateView):
    template_name = 'pages/login.html'
'''
# Contact Us
class ContactView(TemplateView):
    template_name = 'pages/contact.html'

