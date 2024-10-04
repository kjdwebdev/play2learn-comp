import html

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, ListView, UpdateView
from .models import AnagramHuntScores, MathFactsScores
from .forms import AnagramHuntScoresForm, MathFactsScoresForm

class AnagramHuntScoresCreateView(CreateView):
    model = AnagramHuntScores
    form_class = AnagramHuntScoresForm
  
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class MathFactsScoresCreateView(CreateView):
    model = MathFactsScores
    form_class = MathFactsScoresForm
  
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnagramHuntScoresDetailView(DetailView):
    model = AnagramHuntScores

class MathFactsScoresDetailView(DetailView):
    model = MathFactsScores


class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class MathFactsScoresView(ListView):
    model = MathFactsScores
    template_name = "games/math-facts-scores.html"

    def get_queryset(self):
      qs = MathFactsScores.objects.all()
      return qs()  

class AnagramHuntScoresView(ListView):
    model = AnagramHuntScores
    template_name = "games/anagram-hunt-scores.html"

    def get_queryset(self):
      qs = AnagramHuntScores.objects.all()
      return qs()