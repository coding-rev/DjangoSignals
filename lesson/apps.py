from django.apps import AppConfig


class LessonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lesson'

    # Custom config for registering signals
    def ready(self):
        import lesson.signals.humanID_signal, lesson.signals.car_signal, lesson.signals.history_signal