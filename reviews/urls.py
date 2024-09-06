from django.urls import path
from .views import (
    ReviewCreateView, ReviewListView, ReviewThanksView
)
app_name = 'reviews'
urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='create'),
    path('list/', ReviewListView.as_view(), name='list'),
    path('reviews/thanks/', ReviewThanksView.as_view(), name='thanks'),
]