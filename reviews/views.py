from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .models import Review
from .forms import ReviewForm

# Create your views here.
class ReviewCreateView(SuccessMessageMixin, CreateView):
    model = Review
    form_class = ReviewForm
    success_message = 'Review Added'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)