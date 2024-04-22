from django.shortcuts import render, redirect, get_object_or_404
from .models import Rat   # Add this import
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm
from django.contrib.auth.decorators import login_required

def index(request):
    active_workouts = Workout.objects.filter(description='some_description')
    return render(request, 'workout_app/index.html', {'active_workouts': active_workouts})

def home(request):
    return render(request, 'workout_app/user_list.html')
def stub(request):
 return render(request, 'workout_app/stub.html')


from django.db import IntegrityError
def create_exercise(request, workout_id):
    # Retrieve the workout object based on the workout_id
    workout = get_object_or_404(Workout, pk=workout_id)

    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            # Save the exercise data to the database
            exercise = form.save(commit=False)
            exercise.workout = workout  # Associate the exercise with the selected workout
            exercise.save()
            return redirect('view_exercises', workout_id=workout_id)
    else:
        form = ExerciseForm()

    return render(request, 'workout_app/create_exercise.html', {'form': form, 'workout_id': workout_id})



def update_workout(request, rat_id):
    # Retrieve the workout object based on the provided rat_id
    workout = get_object_or_404(Workout, user_id=rat_id)
    
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_detail', user_id=rat_id)
    else:
        form = WorkoutForm(instance=workout)
    
    context = {
        'form': form,
        'workout': workout,
    }
    return render(request, 'workout_app/update_workout.html', context)

def delete_workout(request, rat_id):
    workout = get_object_or_404(Workout, user_id=rat_id)
    if request.method == 'POST':
        workout.delete()
        return redirect('view_workouts')
    return render(request, 'workout_app/delete_workout.html', {'workout': workout})


def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    return render(request, 'workout_app/exercise_detail.html', {'exercise': exercise})

def update_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('workout_detail', workout_id=exercise.workout.id)
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'workout_app/update_exercise.html', {'form': form})

def delete_exercise(request, exercise_id):
    # Retrieve the exercise object
    exercise = get_object_or_404(Exercise, pk=exercise_id)

    # Assuming 'workout_id' is a field in the Exercise model
    workout_id = exercise.workout_id

    context = {
        'exercise': exercise,
        'workout_id': workout_id,
    }

    return render(request, 'workout_app/delete_exercise.html', context)

def user_detail(request, user_id):
    user = get_object_or_404(Rat, pk=user_id)
    return render(request, 'workout_app/user_detail.html', {'user': user})

def user_list(request):
    users = Rat.objects.all()  # Retrieve all users from the database
    return render(request, 'workout_app/user_list.html', {'users': users})






from .forms import WorkoutForm

def create_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to the home page after creating the workout
    else:
        form = WorkoutForm()
    return render(request, 'workout_app/create_workout.html', {'form': form})

def view_workouts(request):
    workouts = Workout.objects.all()
    return render(request, 'workout_app/view_workouts.html', {'workouts': workouts})


def view_exercises(request, workout_id):
    # Retrieve the workout object based on the workout_id
    workout = get_object_or_404(Workout, pk=workout_id)
    
    # Retrieve exercises associated with the selected workout
    exercises = Exercise.objects.filter(workout=workout)
    
    return render(request, 'workout_app/view_exercises.html', {'exercises': exercises, 'workout_id': workout_id})




from django.core.exceptions import ObjectDoesNotExist
from .models import Workout
def workout_detail(request, rat_id):
    try:
        # Retrieve the rat object based on the rat_id
        rat = get_object_or_404(Rat, pk=rat_id)
        # Filter workouts associated with the retrieved rat
        workouts = rat.workouts.all()
    except Rat.DoesNotExist:
        # Handle the case where the rat with the provided ID does not exist
        raise ("Rat does not exist")
    
    # Prepare the context dictionary with data
    context = {
        'rat': rat,
        'workouts': workouts,
    }
    
    # Render the template with the provided context
    return render(request, 'workout_app/workout_detail.html', context)


from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'workout_app/register.html', {'form': form})

# views.py (continued)

from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'workout_app/login.html', {'form': form})
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a desired page after logout
    return redirect('user_list')
@login_required
def my_workouts(request):
    user = request.user
    try:
        rat = user.rat
        workouts = rat.workouts.all()
    except Rat.DoesNotExist:
        workouts = None
    return render(request, 'workout_app/myWorkouts.html', {'workouts': workouts})


@login_required
def user_home(request):
    return render(request, 'workout_app/user_list.html')