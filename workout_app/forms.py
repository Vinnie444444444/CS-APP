from django import forms
from .models import Exercise, Workout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        exclude = ['workout']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    class Meta:
        model = User