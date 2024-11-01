from typing import Any
from django.contrib import admin
from .models import Ascore, Mscore, GameScore

@admin.register(Ascore)
class AscoreAdmin(admin.ModelAdmin):
    model = Ascore,
    list_display = ['id', 'user', 'score', 'max_number', 'operation', 'end_time', 'slug']

@admin.register(Mscore)                 
class MscoreAdmin(admin.ModelAdmin):
    model = Mscore,
    list_display = ['id', 'user', 'score', 'max_number', 'operation', 'end_time', 'slug']

@admin.register(GameScore)                 
class MscoreAdmin(admin.ModelAdmin):
    model = GameScore,
    list_display = ['id', 'user','game','score', 'max_number', 'operation', 'end_time', 'slug']