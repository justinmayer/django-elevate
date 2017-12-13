from .base import BaseTestCase
from django.http import HttpResponse
from django.views import generic
from elevate.mixins import ElevateMixin


class FooView(ElevateMixin, generic.View):
    def get(self, request):
        return HttpResponse()

foo = FooView.as_view()


class ElevateMixinTestCase(BaseTestCase):
    def test_is_elevated(self):
        self.request.is_elevated = lambda: True
        response = foo(self.request)
        self.assertEqual(response.status_code, 200)

    def test_is_not_elevated(self):
        self.request.is_elevated = lambda: False
        response = foo(self.request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/elevate/?next=/foo')
