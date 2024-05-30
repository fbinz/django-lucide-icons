import os
from glob import glob

from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.safestring import mark_safe

cache = {}


class LucideIconsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_lucide_icons"

    def ready(self) -> None:
        if not getattr(settings, "LUCIDE_ICONS_DIR", None):
            raise ImproperlyConfigured("LUCIDE_ICONS_DIR is not set")

        for file in glob(os.path.join(settings.LUCIDE_ICONS_DIR, "*.svg")):
            cache[file.split("/")[-1].split(".")[0]] = mark_safe(open(file).read())

        return super().ready()
