from django import forms
from .models import ContactPost


class ContactForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject')
    content = forms.CharField(label='Enter your content')
    # time = forms.DateTimeField()

    class Meta:
        model = ContactPost
        fields = ('email', 'subject', 'content', )
