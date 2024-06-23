## Usage

To use the template tag, add the following line to your Django project's settings.py file:

```python
LUCIDE_ICONS_DIR = "/path/to/your/icons/directory"
```

The LUCIDE_ICONS_DIR variable should be set to the directory where you want to store the Lucide icons.

Then, you can use the `lucide` template tag in your Django templates to display Lucide icons. For example, to display the "home" icon, you can use the following code:

```html
{% raw %}
{% load lucide_tags %} {% lucide "home" %}

<!-- or using a class attribute -->
{% lucide "home" class="my-class" %}
{% endraw %}
```

The `lucide` template tag takes two arguments:

1. the name of the Lucide icon you want to display
2. an optional `class` attribute that you can use to add a class to the icon

It returns the SVG code of the icon as a string.

Since the plain SVG is rendered, it might make sense to wrap it in a "span" or "div" element to
size it properly.
Alternative approaches are welcome. Just submit an issue or a pull request.