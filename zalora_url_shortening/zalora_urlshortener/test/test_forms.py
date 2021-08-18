from django.test import TestCase

from zalora_urlshortener.forms import ShortenerForm

class ShortenerFormTest(TestCase):
    
    def test_long_url_field_label(self):
        form = ShortenerForm()
        self.assertTrue(form.fields['long_url'].label is None or form.fields['long_url'].label == 'long url')

    def test_long_url_field_help_text(self):
        form = ShortenerForm()
        self.assertEqual(form.fields['long_url'].help_text, 'Enter Your URL to shorten')
