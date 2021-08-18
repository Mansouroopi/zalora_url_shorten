from django.test import TestCase

from zalora_urlshortener.models import Shortener

class ShortenerModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Shortener.objects.create(long_url='https://www.zalora.com.my/all-products/?cmpgn_one=21cw33giftsets&csa=twoonecwthirtyfourgiftsets')

    def test_short_url_label(self):
        shortener = Shortener.objects.get(id=1)
        field_label = shortener._meta.get_field('short_url').verbose_name
        self.assertEqual(field_label, 'short url')

    def test_long_url_label(self):
        shortener = Shortener.objects.get(id=1)
        field_label = shortener._meta.get_field('long_url').verbose_name
        self.assertEqual(field_label, 'long url')

    def test_short_url_max_length(self):
        shortener = Shortener.objects.get(id=1)
        max_length = shortener._meta.get_field('short_url').max_length
        self.assertEqual(max_length, 15)

    def test_object_name_is_short_url_comma_first_created_at(self):
        shortener = Shortener.objects.get(id=1)
        expected_object_name = f'{shortener.short_url}, {shortener.created_at}'
        self.assertEqual(str(shortener), expected_object_name)

    # def test_get_absolute_url(self):
    #     author = Shortener.objects.get(id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEqual(author.get_absolute_url(), '/catalog/author/1')