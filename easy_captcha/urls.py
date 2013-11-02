from django.conf.urls import patterns, include, url

from captcha_api.views import CaptchaAPIView, CaptchaAPIJSONPView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^captcha_api/verify$', CaptchaAPIView.as_view()),

    url(r'^captcha_api/jsonp_verify$', CaptchaAPIJSONPView.as_view()),

)
