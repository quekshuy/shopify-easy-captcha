from recaptcha.client import captcha

from django.views.generic.base import View
from django.conf import settings

class CaptchaAPIView(object):

    def post(self, request):

        challenge_field, response_field = \
                request.POST.get('recaptcha_challenge_field'),\
                request.POST.get('recaptcha_response_field')

        remote_addr = request.META['REMOTE_ADDR']
        private_key = settings.RECAPTCHA_PRIVATE_KEY

        if None in (challenge_field, response_field):
            return HttpResponse(status=400)

        response = captcha.submit(
                challenge_field,
                response_field,
                private_key,
                remote_addr
                )
        if response.is_valid:
            return HttpResponse(status=200)

        return HttpResponse(
                status=403, 
                content='Invalid CAPTCHA'
                )


