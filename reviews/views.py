import html
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView, ListView, UpdateView

from .models import Review
from .forms import ReviewForm

# Create your views here.
class ReviewCreateView(SuccessMessageMixin, CreateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews:thanks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewThanksView(TemplateView):
    template_name = 'reviews/thanks.html'

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:mylist')

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'

class QuoteListView(ListView):
    model = Review
    template_name = 'reviews/quote_list.html'

    def get_queryset(self):
      qs = Review.objects.all()
      return qs.filter(featured=True)

class MyReviewsListView(ListView):
    model = Review
    template_name = 'reviews/myreviews_list.html'

    def get_queryset(self):
      qs = Review.objects.all()
      return qs.filter(user=1)

class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'reviews/review_update.html'
   
