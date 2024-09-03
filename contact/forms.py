from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '100', 'rows': '5'})
)