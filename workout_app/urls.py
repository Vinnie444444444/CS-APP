from django.urls import path
from .views import home, index, stub, workout_detail, create_exercise, update_workout, delete_workout, \
    exercise_detail, update_exercise, delete_exercise, user_detail, user_list, login_view, logout_view, register_view, \
    create_workout, view_workouts, view_exercises, my_workouts,user_home
from . import views
urlpatterns = [
    path('', home, name='home'),
    path('index/', index, name='index'),
    path('login', views.stub, name="login"),
    path('logout', views.stub, name="logout"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('user_home/', user_home, name='user_home'),
    path('user_workout/<int:rat_id>/', views.workout_detail, name='workout_detail'),
    path('workout_detail/<int:rat_id>/', views.workout_detail, name='workout_detail'),
    path('create_exercise/<int:workout_id>/', create_exercise, name='create_exercise'),

    path('update_workout/<int:rat_id>/', update_workout, name='update_workout'),
    path('workout_detail/<int:workout_id>/', views.workout_detail, name='workout_detail'),

    path('delete_workout/<int:rat_id>/', delete_workout, name='delete_workout'),
    path('exercise_detail/<int:exercise_id>/', exercise_detail, name='exercise_detail'),
    path('update_exercise/<int:exercise_id>/', update_exercise, name='update_exercise'),
    path('delete_exercise/<int:exercise_id>/', delete_exercise, name='delete_exercise'),
    path('user_detail/<int:user_id>/', user_detail, name='user_detail'),
    path('user_list/', user_list, name='user_list'),
 
    path('create_workout/', create_workout, name='create_workout'),
    path('my_workouts/', my_workouts, name='my_workouts'),
    path('view_exercises/<int:workout_id>/', views.view_exercises, name='view_exercises'),
    path('view_workouts/', views.view_workouts, name='view_workouts'),
    path('user_workout/<int:workout_id>/', workout_detail, name='user_workout'),
]
