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
{% load lucide_tags %} 

{% lucide "home" %}
```

The `lucide` template tag takes a single argument, which is the name of the Lucide icon you want to display.
It returns the SVG code of the icon as a string.

Since the plain SVG is rendered, it might make sense to wrap it in a "span" or "div" element to
size it properly.
Alternative approaches are welcome. Just submit an issue or a pull request.
