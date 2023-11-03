from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Film, Rating
from rest_framework import viewsets
from .serializers import FilmSerializers, RatingSerializers


class FilmView (View):

    def get (self, request):

        film = Film.objects.all()

        titleFilm = ""

        for oneFilm in film:
            titleFilm += f"<br>{oneFilm.title}"

        textFilm = '<h3>Lista filmów w bazie danych</h3>'
        content  = {textFilm + titleFilm}

        return HttpResponse(content)
    
# serializers
# first
class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerializers
    queryset = Film.objects.all()

# second
class RatingViewSet (viewsets.ModelViewSet):
    serializer_class = RatingSerializers
    queryset = Rating.objects.all()
