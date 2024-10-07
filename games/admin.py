from typing import Any
from django.contrib import admin
from .models import AnagramHuntScores, Ascore, MathFactsScores

# Register your models here.
@admin.register(AnagramHuntScores)
class AnagramHuntScoresAdmin(admin.ModelAdmin):
    model = AnagramHuntScores,
    list_display = ['id', 'user', 'score', 'max_number', 'operation', 'end_time']

@admin.register(Ascore)
class AnagramHuntScoresAdmin(admin.ModelAdmin):
    model = Ascore,
    list_display = ['id', 'user', 'score', 'max_number', 'operation', 'end_time']

@admin.register(MathFactsScores)                 
class MathFactsScoresAdmin(admin.ModelAdmin):
    model = MathFactsScores,
    list_display = ['id', 'user', 'score', 'max_number', 'operation', 'end_time']
