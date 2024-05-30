import os
import os.path
import urllib.request

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from ..apps import cache

register = template.Library()


@register.simple_tag
def lucide(name):
    if name in cache:
        return cache[name]

    if settings.DEBUG:
        # write the icon to the file system during development
        with urllib.request.urlopen(
            f"https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/{name}.svg"
        ) as response:
            if response.status != 200:
                raise Exception(f"Icon {name} not found")

            # ensure that the directory exists
            os.makedirs(settings.LUCIDE_ICONS_DIR, exist_ok=True)

            with open(
                os.path.join(settings.LUCIDE_ICONS_DIR, name + ".svg"), "w"
            ) as file:
                # remove the width and height attributes
                transformed = (
                    response.read().replace('width="24"', "").replace('height="24"', "")
                )

                file.write(transformed)
                cache[name] = mark_safe(transformed)
            return cache[name]
