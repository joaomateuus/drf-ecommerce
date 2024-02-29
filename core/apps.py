from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    
    def ready(self, *args, **kwargs) -> None:
        import core.signals
        super_ready = super().ready(*args, **kwargs)
        return super_ready
