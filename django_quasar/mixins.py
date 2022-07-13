from django import forms

from . import CSS_QUASAR_111, JS_QUASAR_111, CSS_QUASAR_27, JS_QUASAR_27

class Quasar_111_Mixin(object):

    @property
    def media(self):
        css = {
            'all': (CSS_QUASAR_111,)
        }
        js = [JS_QUASAR_111]
        return super().media + forms.Media(js=js, css=css)

class Quasar_27_Mixin(object):

    @property
    def media(self):
        css = {
            'all': (CSS_QUASAR_27,)
        }
        js = [JS_QUASAR_27]
        return super().media + forms.Media(js=js, css=css)


class QuasarMixin(Quasar_27_Mixin):
    pass
