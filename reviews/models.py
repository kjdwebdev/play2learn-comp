from django.conf import settings
from django.db import models

GAMES = (
    (1, 'Anagram Hunt'),
    (2, 'Math Facts'),
)
STARS = (
    (1, 'Exceptional'),
    (2, 'Good'),
    (3, 'Satisfactory'),
    (4, 'Unsatisfactory'),
    (5, 'Unacceptable')
)
    
class Review(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='gamereview'
    )
    game = models.SmallIntegerField(choices=GAMES)
    stars = models.SmallIntegerField(choices=STARS)
    review = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField()

    def __str__(self):
        return self.review
