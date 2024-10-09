import html

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, ListView, UpdateView
from .models import Ascore, Mscore
from .forms import AscoreForm, MscoreForm

#These are the actual games
class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

#These are for the scores    
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

class MscoreCreateView(CreateView):
    model = Mscore
    form_class = MscoreForm
    success_url = reverse_lazy('games:thanks')
  
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MscoreThanksView(TemplateView):
    template_name = 'games\thanks.html'

class MscoreDeleteView(DeleteView):
    model = Mscore
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

class AscoreDetailView(DetailView):
    model = Ascore
    template_name = 'games/ascore_detail.html'

class MscoreDetailView(DetailView):
    model = Mscore
    template_name = 'games/mscore_detail.html'

class AscoreListView(ListView):
    model = Ascore
    template_name = "games/ascore_list.html"

class AscoreUpdateView(UpdateView):
    model = Ascore
    template_name = "games/ascore_list.html"

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class MscoreListView(ListView):
    model = Mscore
    template_name = "games/mscore_list.html"

class MscoreUpdateView(UpdateView):
    model = Mscore
    template_name = "games/mscore_list.html"

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

#Leaderboards
class AleaderListView(ListView):
    model = Ascore
    template_name = 'games/aleader_list.html'
    ordering = ['-score']

    def get_queryset(self):
        qs = Ascore.objects.all().order_by('-score')
        #0=first one and it doesn't include 3
        return qs[0:3]

class MleaderListView(ListView):
    model = Ascore
    template_name = 'games/mleader_list.html'
    ordering = ['-score']

    def get_queryset(self):
        qs = Mscore.objects.all().order_by('-score')
        #0=first one and it doesn't include 3
        return qs[0:3]

#My Scores
class MyascoreListView(ListView):
    model = Ascore
    template_name = 'games/myascore_list.html'

    def get_queryset(self):
        qs = Ascore.objects.all()
        return qs.filter(user=self.request.user)

class MymscoreListView(ListView):
    model = Ascore
    template_name = 'games/mymscore_list.html'

    def get_queryset(self):
        qs = Mscore.objects.all()
        return qs.filter(user=self.request.user)