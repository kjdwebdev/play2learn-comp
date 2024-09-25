from django.conf import settings
from django.db import models

from common.utils.text import unique_slug

GAMES = (
    (1, 'Anagram Hunt'),
    (2, 'Math Facts'),
)
STARS = (
    (5, 'Exceptional'),
    (4, 'Good'),
    (3, 'Satisfactory'),
    (2, 'Unsatisfactory'),
    (1, 'Unacceptable')
)
    
class Review(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='gamereview'
    )
    game = models.SmallIntegerField(choices=GAMES, editable=True)
    stars = models.SmallIntegerField(choices=STARS, editable=True)
    review = models.TextField(max_length=200, editable=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=True)
    slug = models.SlugField(
        max_length=50, unique=True, null=True, editable=False
    )

    def get_absolute_url(self):
        #return reverse('reviews:detail', args=[str(self.pk)])
        return reverse('reviews:detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        #create the slug if the record doesn't already have one
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.review
