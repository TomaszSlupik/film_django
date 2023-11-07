from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Film, Rating
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
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

    @action(detail=True, methods=['POST'])
    def rate_film(self, request, pk=None):
        print (request.user)
        resonse = {"message": 'Dostępny'}
        return Response (resonse, status=status.HTTP_200_OK)

# second
class RatingViewSet (viewsets.ModelViewSet):
    serializer_class = RatingSerializers
    queryset = Rating.objects.all()
