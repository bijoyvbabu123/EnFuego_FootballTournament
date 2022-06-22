from django.apps import AppConfig


class EnfuegoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'enfuego'

    def ready(self):
        import enfuego.signals