from django.conf import settings

CSS_QUASAR_111 = 'js/quasar-1.11.3/quasar%s.css' % ('' if not settings.DEBUG else '.min')
JS_QUASAR_111 = 'js/quasar-1.11.3/quasar.umd%s.js' % ('' if not settings.DEBUG else '.min')
