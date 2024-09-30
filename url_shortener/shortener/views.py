from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import ShortenedURL
import json

def create_short_url(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        original_url = data.get('url')

        # Create a unique short URL
        short_url = ShortenedURL.generate_short_url()
        shortened_url = ShortenedURL.objects.create(original_url=original_url, short_url=short_url)

        response = {
            'short_url': f"http://localhost:8000/s/{shortened_url.short_url}"
        }
        return JsonResponse(response)

def redirect_short_url(request, short_url):
    # Get the original URL based on the short URL
    shortened_url = get_object_or_404(ShortenedURL, short_url=short_url)

    # Increment the redirect count
    shortened_url.redirect_count += 1
    shortened_url.save()

    # Redirect to the original URL
    return redirect(shortened_url.original_url)

def not_found_view(request, exception):
    return HttpResponse('Short URL not found', status=404)
