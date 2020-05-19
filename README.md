# django-quasar

## Example

Add the `django_quasar` application to `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
  ...
  'django_quasar',
  ...
)
```

In a ModelAdmin

```python
from django_quasar.mixins import QuasarMixin

@admin.register(Example)
class ExampleAdmin(QuasarMixin, admin.ModelAdmin):
    pass

```

In a template
```
{% load django_quasar %}

{% block extrahead %}
{{ block.super }}
{% quasar_css %}
{% quasar_js %}
{% endblock %}

```

## Check code in development

```
pipenv shell
pipenv install -r requirements-devel.txt
. scripts/pre-commit.sh
```

## Authors

[<img src="http://www.microdisseny.com/images/web/microdisseny-logo-small.png" width="226">](http://www.microdisseny.com/)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
