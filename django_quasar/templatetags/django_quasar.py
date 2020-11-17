from django import template
from django_quasar import CSS_QUASAR_111, CSS_QUASAR_114, JS_QUASAR_111, JS_QUASAR_114

register = template.Library()


@register.inclusion_tag('django_quasar/tags/quasar_css.html', takes_context=True)
def quasar_css_111(context):
    return {
        'css_file': CSS_QUASAR_111
    }


@register.inclusion_tag('django_quasar/tags/quasar_css.html', takes_context=True)
def quasar_css_114(context):
    return {
        'css_file': CSS_QUASAR_114
    }


@register.inclusion_tag('django_quasar/tags/quasar_css.html', takes_context=True)
def quasar_css(context):
    return quasar_css_114(context)


@register.inclusion_tag('django_quasar/tags/quasar_js.html', takes_context=True)
def quasar_js_19(context):
    return {
        'js_file': JS_QUASAR_111
    }


@register.inclusion_tag('django_quasar/tags/quasar_js.html', takes_context=True)
def quasar_js_114(context):
    return {
        'js_file': JS_QUASAR_114
    }


@register.inclusion_tag('django_quasar/tags/quasar_js.html', takes_context=True)
def quasar_js(context):
    return quasar_js_114(context)
