from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from common.utils.text import unique_slug

# Create your models here.

class Ascore(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='ascore'
    )
    score = models.IntegerField(
        default=1,
        editable=True,
        )
    max_number = models.IntegerField(
        default=5,
        editable=True,
        validators=[
            MaxValueValidator(8),
            MinValueValidator(5)
            ]
        )
    operation = models.CharField(max_length=30, default="anagramhunt", editable=True)
    end_time = models.DateTimeField(auto_now=True, editable=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=True, editable=False)
    
    def save(self, *args, **kwargs):
        #create the slug if the record doesn't already have one
        if not self.slug:
            value = 'anagramhunt' + str(self.score)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        #return reverse('reviews:detail', args=[str(self.pk)])
        return reverse('games:adetail', args=[self.slug])
        #return reverse('games:adetail', args=[str(self.pk)])
    
    def __str__(self):
        return self.slug
    
class Mscore(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='mscore'
    )
    score = models.IntegerField(
        default=1,
        editable=True,
        )
    max_number = models.IntegerField(
        default=30,
        editable=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
            ]
        )
    operation = models.CharField(max_length=30, default="operation", editable=True)
    end_time = models.DateTimeField(auto_now=True, editable=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=True, editable=False)
    
    def save(self, *args, **kwargs):
        #create the slug if the record doesn't already have one
        if not self.slug:
            value = self.operation + str(self.score)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        #return reverse('reviews:detail', args=[str(self.pk)])
        return reverse('games:mdetail', args=[self.slug])
        #return reverse('games:mdetail', args=[str(self.pk)])
    
    def __str__(self):
        return self.slug

class GameScore(models.Model):

    MATH = "MATH"
    ANAGRAM = "ANAGRAM"

    GAME_CHOICES = [
        {MATH, "Math Facts"},
        {ANAGRAM, "Anagram Hunt"}
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    score = models.IntegerField(default=1, editable=True)
    max_number = models.IntegerField(
        default=1,
        editable=True,
        )
    operation = models.CharField(max_length=30, editable=True)
    end_time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=True, editable=False)
    
    def save(self, *args, **kwargs):
        #create the slug if the record doesn't already have one
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)