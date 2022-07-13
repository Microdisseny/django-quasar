from django.conf import settings

CSS_QUASAR_111 = 'js/quasar-1.11.3/quasar%s.css' % ('' if settings.DEBUG else '.min')
JS_QUASAR_111 = 'js/quasar-1.11.3/quasar.umd%s.js' % ('' if settings.DEBUG else '.min')

CSS_QUASAR_27 = 'js/quasar-2.7.5/quasar%s.css' % ('' if settings.DEBUG else '.prod')
JS_QUASAR_27 = 'js/quasar-2.7.5/quasar.umd%s.js' % ('' if settings.DEBUG else '.prod')
