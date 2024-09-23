from django.urls import path
from .views import (
    ReviewCreateView, ReviewDeleteView, ReviewDetailView, ReviewListView, ReviewThanksView, QuoteListView, MyReviewsListView, ReviewUpdateView
)
app_name = 'reviews'
urlpatterns = [
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete'),
    path('<int:pk>/detail/', ReviewDetailView.as_view(), name='detail'),
    path('create/', ReviewCreateView.as_view(), name='create'),
    path('list/', ReviewListView.as_view(), name='list'),
    path('mylist/', MyReviewsListView.as_view(), name='mylist'),
    path('quotes/', QuoteListView.as_view(), name='quotes'),
    path('reviews/thanks/', ReviewThanksView.as_view(), name='thanks'),
    path('<int:pk>/update/', ReviewUpdateView.as_view(), name='update'),
]