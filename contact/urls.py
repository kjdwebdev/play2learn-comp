from django.urls import path

from .views import ContactView, ContactThanksView

app_name = 'contact'
urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/thanks/', ContactThanksView.as_view(), name='thanks'),
]