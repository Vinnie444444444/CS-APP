from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Workout(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('workout_app.Rat', on_delete=models.CASCADE, related_name='workouts', default=1)


    def get_absolute_url(self):
        return reverse('Workout-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.PositiveIntegerField(default=None)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, default=None)

    def get_absolute_url(self):
         return reverse('Exercise-detail', args=[str(self.id)])
    def __str__(self):
        return self.name
        
class Rat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField("User email", max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('User-detail', args=[str(self.id)])

        
