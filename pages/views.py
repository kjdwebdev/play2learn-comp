from django.views.generic import TemplateView

# Create your views here.
# Home Page
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

# About Us
class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

# Games
class GamesView(TemplateView):
    template_name = 'pages/games.html'

# Login
class LoginView(TemplateView):
    template_name = 'pages/login.html'

# Contact Us
class ContactView(TemplateView):
    template_name = 'pages/contact.html'