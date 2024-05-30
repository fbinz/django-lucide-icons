from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class LucideIconsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_lucide_icons"

    def ready(self) -> None:
        if not getattr(settings, "LUCIDE_ICONS_DIR", None):
            raise ImproperlyConfigured("LUCIDE_ICONS_DIR is not set")

        return super().ready()
