import html
import json
from django.http import JsonResponse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, ListView, UpdateView
from games.models import Ascore, Mscore, GameScore
from games.forms import AscoreForm, MscoreForm

#These are the actual games
class MathFactsView(TemplateView):
    model = GameScore
    template_name = "math-facts.html"

    def get_context_data(self, **kwargs):
        context = super(MathFactsView, self).get_context_data(**kwargs)
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')[0:3]
        return context

class AnagramHuntView(TemplateView):
    model = GameScore
    template_name = 'anagram-hunt.html'
    ordering = ['-score']

    def get_context_data(self, **kwargs):
        context = super(AnagramHuntView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')[0:3]
        return context

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
class GameScoresView(TemplateView):
    template_name="games/game-scores.html"

    def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')[0:3]
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')[0:3]
        return context

class AleaderList2View(ListView):
    model = Ascore
    template_name = 'aleader_list2.html'
    ordering = ['-score']

    def get_queryset(self):
        qs = Ascore.objects.all().order_by('-score')
        #0=first one and it doesn't include 3
        return qs[0:3]

#My Scores
class MyScoresView(TemplateView):
    template_name = 'games/myscores.html'

    def get_context_data(self, **kwargs):
        context = super(MyScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM', user=self.request.user).order_by('-score')[0:3]
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH', user=self.request.user).order_by('-score')[0:3]
        return context

def record_score(request):
    data = json.loads(request.body)

    game = data["game"]
    score = data["score"]
    max_number = data["max_number"]
    operation = data["operation"]
    #user_id=request.user.user_id
    user_id = data["user_id"]
    
    new_score = GameScore(game=game, score=score, max_number=max_number, operation=operation, user_id=user_id)
    #new_score = GameScore(game=game, score=score, max_number=max_number, operation=operation, user_id=request.user.user_id)
    new_score.save()

    response = {
        "success": True
    }

    return JsonResponse(response)



