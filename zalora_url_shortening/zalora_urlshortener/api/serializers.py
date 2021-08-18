from rest_framework import serializers
from zalora_urlshortener.models import Shortener

class ShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = "__all__"