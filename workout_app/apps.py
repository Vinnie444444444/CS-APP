from django.apps import AppConfig

class FitnessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workout_app'

class WorkoutAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workout_app'

    def ready(self):
        import workout_app.signals