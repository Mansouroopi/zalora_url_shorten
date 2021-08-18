from django import forms

from .models import Shortener

class ShortenerForm(forms.ModelForm):
    """
    Shortener Forms class zalora_urlshortener/forms.py
    """  
    long_url = forms.URLField(help_text="Enter Your URL to shorten", widget=forms.URLInput(
        attrs={"class": "form-control input form-control-lg", "placeholder": "Enter Your URL to shorten"}))
    
    class Meta:
        model = Shortener

        fields = ('long_url',)
