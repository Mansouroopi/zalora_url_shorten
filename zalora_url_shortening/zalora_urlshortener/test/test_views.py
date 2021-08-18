from django.test import SimpleTestCase
from django.urls import reverse

from zalora_urlshortener.views import *

class ShortenerTestCase(SimpleTestCase):
   
    def test_home_page_status_code(self):
       response = self.client.get('/')
       self.assertEquals(response.status_code, 200)


    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)


    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'zalora_urlshortener/home.html')


    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Url shorten App</h1>')


    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')

    def test_post_redirect_url_view_404(self):
       response = self.client.get(reverse('redirect', args=('RANDOM',)))
       self.assertEqual(response.status_code, 404)
