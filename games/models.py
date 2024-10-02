from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class AnagramHuntScores(models.Model):
        user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        ),

        score = models.IntegerField(),

        max_number = models.IntegerField(
            default=5,
            validators=[
                MaxValueValidator(8),
                MinValueValidator(5)
            ]
        ),
        operation = models.CharField(max_length=30),
        end_time = models.DateTimeField(auto_now=True)
    

class MathFactsScores(models.Model):
        user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        ),

        score = models.IntegerField(),

        max_number = models.IntegerField(
            default=30,
            validators=[
                MaxValueValidator(100),
                MinValueValidator(1)
            ]
        ),
        operation = models.CharField(max_length=30),
        end_time = models.DateTimeField(auto_now=True)
    