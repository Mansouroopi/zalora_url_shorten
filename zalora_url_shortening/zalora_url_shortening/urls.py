"""zalora_url_shortening URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Shortener Urls
    path('admin/', admin.site.urls),
    path('', include('zalora_urlshortener.urls')),
    path('api/v1/shortener/',include('zalora_urlshortener.api.urls')),
    path('docs/', include_docs_urls(title='Zalora Url Shortener Api')),
]

