from django import forms

from . import CSS_QUASAR_111, CSS_QUASAR_114, JS_QUASAR_111, JS_QUASAR_114


class Quasar_111_Mixin(object):

    @property
    def media(self):
        css = {
            'all': (CSS_QUASAR_111,)
        }
        js = [JS_QUASAR_111]
        return super().media + forms.Media(js=js, css=css)


class Quasar_114_Mixin(object):

    @property
    def media(self):
        css = {
            'all': (CSS_QUASAR_114,)
        }
        js = [JS_QUASAR_114]
        return super().media + forms.Media(js=js, css=css)


class QuasarMixin(Quasar_114_Mixin):
    pass
