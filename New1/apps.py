from django.apps import AppConfig


class New1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'New1'

    def ready(self):
        from . import signals

