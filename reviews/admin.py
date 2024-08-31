from typing import Any
from django.contrib import admin
from .models import Review

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['user', 'game', 'stars', 'review','featured']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return ()