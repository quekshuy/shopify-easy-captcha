from recaptcha.client import captcha

from django.views.generic.base import View
from django.conf import settings
from django.utils import simplejson as json


class CaptchaAPIView(View):

    def get_recaptcha_response(
                            self, 
                            challenge_field, 
                            response_field, 
                            remote_addr, 
                            private_key):

        return captcha.submit(
                challenge_field,
                response_field,
                private_key,
                remote_addr
                )


    def post(self, request):

        challenge_field, response_field = \
                request.POST.get('recaptcha_challenge_field'),\
                request.POST.get('recaptcha_response_field')

        remote_addr = request.META['REMOTE_ADDR']
        private_key = settings.RECAPTCHA_PRIVATE_KEY

        if None in (challenge_field, response_field):
            return HttpResponse(status=400)

        response = self.get_recaptcha_response(
                challenge_field, response_field, remote_addr,
                private_key
                )

        if response.is_valid:
            return HttpResponse(status=200)

        return HttpResponse(
                status=403, 
                content='Invalid CAPTCHA'
                )


class CaptchaAPIJSONPView(CaptchaAPIView):

    def get(self, request):

        challenge_field, response_field = \
                request.GET.get('recaptcha_challenge_field'),\
                request.GET.get('recaptcha_response_field')

        remote_addr = request.META['REMOTE_ADDR']
        private_key = settings.RECAPTCHA_PRIVATE_KEY

        callback = request.GET.get('callback')

        if None in (challenge_field, response_field, callback):
            return HttpResponse(status=400)

        response = self.get_recaptcha_response(
                challenge_field, response_field, remote_addr,
                private_key
                )

        if response.is_valid:
            return HttpResponse(
                    status=200,
                    content=''.join([callback, '(', \
                            json.dumps({
                                    'result': 'success'
                                }), ')'])
                            )
        return HttpResponse(
                status=403, 
                content='Invalid CAPTCHA'
                )

