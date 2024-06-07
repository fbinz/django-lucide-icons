import os
import os.path
import re
import urllib.request
import xml.etree.ElementTree as ET

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from ..apps import cache

register = template.Library()


@register.simple_tag
def lucide(name, **kwargs):
    if name in cache:
        if "class" in kwargs:
            return mark_safe(cache[name].format(**{"class": kwargs["class"]}))

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
                ET.register_namespace("temp", "http://www.w3.org/2000/svg")
                doc = ET.fromstring(response.read().decode("utf-8"))

                del doc.attrib["width"]
                del doc.attrib["height"]
                doc.attrib["class"] = "{class}"

                transformed = ET.tostring(doc, encoding="unicode")
                transformed = re.sub(":?temp:?", "", transformed)

                file.write(transformed)
                cache[name] = mark_safe(transformed)
            return cache[name]
