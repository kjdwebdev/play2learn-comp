from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

from common.utils.text import unique_slug

# Create your models here.
class AnagramHuntScores(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    score = models.IntegerField(default=1, editable=True)
    max_number = models.IntegerField(
        default=5,
        editable=True,
        validators=[
            MaxValueValidator(8),
            MinValueValidator(5)
            ]
        )
    operation = models.CharField(max_length=30, editable=True)
    end_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=True, editable=False)
    
    def save(self, *args, **kwargs):
        #create the slug if the record doesn't already have one
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        #return reverse('reviews:detail', args=[str(self.pk)])
        return reverse('AnagramHuntScores:detail', args=[self.slug])
    
    def __str__(self):
        return str(self.score)

class MathFactsScores(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
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
    operation = models.CharField(max_length=30, editable=True)
    end_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=True, editable=False)
    
    def save(self, *args, **kwargs):
        #create the slug if the record doesn't already have one
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        #return reverse('reviews:detail', args=[str(self.pk)])
        return reverse('MathFactsSCores:detail', args=[self.slug])
    
    def __str__(self):
        return str(self.score)