import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from common.utils.email import send_email
from .forms import ContactForm

# Create your views here.
class ContactView(FormView):
    template_name = 'contact/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'dicampok@comcast.net'
        subject = 'Play2Learn Contact'
        content = f'''<p>Hey Manager!</p>
            <p>Contact message received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)

class ContactThanksView(TemplateView):
    template_name = 'contact/thanks.html'