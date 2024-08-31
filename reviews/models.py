from django.conf import settings
from django.db import models

GAMES = (
    (1, 'Anagram Hunt'),
    (2, 'Math Facts'),
)

class Review(models.Model):
    review = models.TextField(max_length=200)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='gamereview'
    )
    game = models.CharField(max_length=20, choices=GAMES)
    stars = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'game'], name='one_vote_per_user_per_game'
            )
        ]

    def __str__(self):
        return self.review
