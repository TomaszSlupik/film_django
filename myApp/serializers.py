from rest_framework import serializers
from .models import Film, Rating

class FilmSerializers (serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ["title", "describe", "time", "kind_of_movie", "data_premiere"]

class RatingSerializers (serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["film", "user", "stars"]