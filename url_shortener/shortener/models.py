from django.db import models
import string
import random

class ShortenedURL(models.Model):
    original_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=10, unique=True)
    redirect_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_url} -> {self.original_url}"

    @staticmethod
    def generate_short_url(length=6):
        """Generates a random short URL of the specified length."""
        characters = string.ascii_letters + string.digits
        while True:
            short_url = ''.join(random.choices(characters, k=length))
            if not ShortenedURL.objects.filter(short_url=short_url).exists():
                return short_url
