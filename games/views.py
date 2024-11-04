import html
import json
from django.http import JsonResponse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, ListView, UpdateView
from games.models import GameScore
from games.forms import GameScoreForm


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

    def get_context_data(self, **kwargs):
        context = super(AnagramHuntView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')[0:3]
        return context

#These are for the scores    
class GameScoreCreateView(CreateView):
    model = GameScore
    form_class = GameScoreForm
    success_url = reverse_lazy('games:thanks')
  
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GameScoreThanksView(TemplateView):
    template_name = 'games\thanks.html'

class GameScoreDeleteView(DeleteView):
    model = GameScore
    success_url = reverse_lazy('games:thanks')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        return result
  
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GameScorecoreUpdateView(UpdateView):
    model = GameScore
    template_name = "games/gamescore_list.html"

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

class MathScoresView(TemplateView):
    template_name="games/math-scores.html"

    def get_context_data(self, **kwargs):
        context = super(MathScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context

class AnagramScoresView(TemplateView):
    template_name="games/anagram-scores.html"

    def get_context_data(self, **kwargs):
        context = super(AnagramScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context


#My Scores
class MyScoresView(TemplateView):
    template_name = 'games/myscores.html'

    def get_context_data(self, **kwargs):
        context = super(MyScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM', user=self.request.user).order_by('-score')[0:3]
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH', user=self.request.user).order_by('-score')[0:3]
        return context

class MyMscoresAllView(TemplateView):
    template_name = 'games/mymscores-all.html'

    def get_context_data(self, **kwargs):
        context = super(MyMscoresAllView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM', user=self.request.user).order_by('-end_time')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH', user=self.request.user).order_by('-end_time')
        return context

class MyAscoresAllView(TemplateView):
    template_name = 'games/myascores-all.html'

    def get_context_data(self, **kwargs):
        context = super(MyAscoresAllView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM', user=self.request.user).order_by('-end_time')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH', user=self.request.user).order_by('-end_time')
        return context

def record_score(request):
    data = json.loads(request.body)

    game = data["game"]
    score = data["score"]
    max_number = data["max_number"]
    operation = data["operation"]
    user_id = request.user.id
    
    new_score = GameScore(game=game, score=score, max_number=max_number, operation=operation, user_id=user_id)
    new_score.save()

    response = {
        "success": True
    }

    return JsonResponse(response)



