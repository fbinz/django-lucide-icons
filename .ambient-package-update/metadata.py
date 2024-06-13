from ambient_package_update.metadata.author import PackageAuthor
from ambient_package_update.metadata.constants import DEV_DEPENDENCIES
from ambient_package_update.metadata.package import PackageMetadata
from ambient_package_update.metadata.readme import ReadmeContent
from ambient_package_update.metadata.ruff_ignored_inspection import (
    RuffIgnoredInspection,
)

METADATA = PackageMetadata(
    package_name="django-lucide-icons",
    authors=[
        PackageAuthor(
            name="Fabian Binz",
            email="fabian.binz@gmail.com",
        ),
    ],
    development_status="5 - Production/Stable",
    readme_content=ReadmeContent(
        tagline="Lucide Icons for Django",
        content="""
# Django Lucide Icons

This is a Django template tag that allows you to use [Lucide Icons](https://lucide.dev/) in your Django templates.

## Installation

To install the package, simply run:

```bash
pip install django-lucide-icons
```

Then add

```python
INSTALLED_APPS = [
    # ...
    "lucide_icons",
]
```

to your Django project's settings.py file.

## Usage

To use the template tag, add the following line to your Django project's settings.py file:

```python
LUCIDE_ICONS_DIR = "/path/to/your/icons/directory"
```

The LUCIDE_ICONS_DIR variable should be set to the directory where you want to store the Lucide icons.

Then, you can use the `lucide` template tag in your Django templates to display Lucide icons. For example, to display the "home" icon, you can use the following code:

```html
{% load lucide_tags %} {% lucide "home" %}

<!-- or using a class attribute -->
{% lucide "home" class="my-class" %}
```

The `lucide` template tag takes two arguments:

1. the name of the Lucide icon you want to display
2. an optional `class` attribute that you can use to add a class to the icon

It returns the SVG code of the icon as a string.

Since the plain SVG is rendered, it might make sense to wrap it in a "span" or "div" element to
size it properly.
Alternative approaches are welcome. Just submit an issue or a pull request.

## Changelog

### 0.2.0

- Added support for class attributes

### 0.1.0

- Initial release
""",
    ),
    dependencies=[],
    optional_dependencies={
        "dev": [
            *DEV_DEPENDENCIES,
        ],
        # you might add further extras here
    },
    ruff_ignore_list=[
        RuffIgnoredInspection(key="XYZ", comment="Reason why we need this exception"),
    ],
    company="Fabian Binz",
    has_migrations=False,
    supported_django_versions=["3.2", "4.0", "4.1"],
    supported_python_versions=["3.8", "3.9", "3.10"],
)
