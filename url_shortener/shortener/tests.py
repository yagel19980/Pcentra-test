from django.test import TestCase
from django.urls import reverse
from .models import ShortenedURL

class URLShortenerTestCase(TestCase):

    def test_create_short_url(self):
        response = self.client.post(reverse('create_short_url'), data={'url': 'https://example.com'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('short_url', response.json())

    def test_redirect_short_url(self):
        shortened_url = ShortenedURL.objects.create(original_url='https://example.com', short_url='abc123')
        response = self.client.get(f'/s/{shortened_url.short_url}/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, shortened_url.original_url)

    def test_non_existing_short_url(self):
        response = self.client.get('/s/nonexisting/')
        self.assertEqual(response.status_code, 404)
