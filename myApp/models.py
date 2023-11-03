from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Film(models.Model):
    title = models.CharField(max_length=20)

    describe = models.TextField(max_length=150, null=True)
    
    time = models.IntegerField(null=True)

    KIND_OF_MOVIE = {
        ("Filmy akcji", "Filmy akcji"),
        ("Dramat", "Dramat"),
        ("Komedia", "Komedia"),
        ("Film dokumentalny", "Film dokumentalny"),
        ("Horror", "Horror"),
        ("Komedia romantyczna", "Komedia romantyczna"),
        ("Fantastyczny", "Fantastyczny"),
        ("Fantastyczno-naukowy", "Fantastyczno-naukowy")
    }

    kind_of_movie = models.CharField(max_length=50, 
                                     choices=KIND_OF_MOVIE, null=True)
    
    data_premiere = models.DateField(null=True)

    def __str__ (self):
        return self.title
    
class Rating(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


    class Meta:
        unique_together = (('film', 'user'),)
        index_together = (('film', 'user'),)

