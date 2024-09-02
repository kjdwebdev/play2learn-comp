from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import ContactForm

# Create your views here.
class ContactView(FormView):
    template_name = 'contact/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')

class ContactThanksView(TemplateView):
    template_name = 'contact/thanks.html'