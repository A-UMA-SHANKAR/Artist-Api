from django.apps import AppConfig


class ArtistAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artist_app'

    def ready(self):
        import artist_app.signals
