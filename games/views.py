import html

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, ListView, UpdateView
from .models import Ascore, AnagramHuntScores, MathFactsScores
from .forms import AnagramHuntScoresForm, MathFactsScoresForm, AscoreForm

#These are the actual games
class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

#These are for the scores
class AnagramHuntScoresCreateView(CreateView):
    model = AnagramHuntScores
    form_class = AnagramHuntScoresForm
  
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AscoreCreateView(CreateView):
    model = Ascore
    form_class = AscoreForm
    success_url = reverse_lazy('games:thanks')
  
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AscoreThanksView(TemplateView):
    template_name = 'games\thanks.html'

class AscoreDeleteView(DeleteView):
    model = Ascore
    success_url = reverse_lazy('games:thanks')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        return result
  
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class MathFactsScoresCreateView(CreateView):
    model = MathFactsScores
    form_class = MathFactsScoresForm
  
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AnagramHuntScoresDetailView(DetailView):
    model = AnagramHuntScores

class AscoreDetailView(DetailView):
    model = Ascore
    template_name = 'games/ascore_detail.html'

class MathFactsScoresDetailView(DetailView):
    model = MathFactsScores

class AnagramHuntScoresListView(ListView):
    model = AnagramHuntScores
    template_name = "games/AnagramHuntScores_list.html"

class AscoreListView(ListView):
    model = Ascore
    template_name = "games/ascore_list.html"

class AscoreUpdateView(UpdateView):
    model = Ascore
    template_name = "games/ascore_list.html"

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class MathFactsScoresListView(ListView):
    model = MathFactsScores
    success_url = success_url = reverse_lazy('games:thanks')

#Leaderboards
