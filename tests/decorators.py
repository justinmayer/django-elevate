from .base import BaseTestCase

from django.http import HttpResponse
from elevate.decorators import elevate_required


@elevate_required
def foo(request):
    return HttpResponse()


class ElevateRequiredTestCase(BaseTestCase):
    def test_is_elevated(self):
        self.request.is_elevated = lambda: True
        response = foo(self.request)
        self.assertEqual(response.status_code, 200)

    def test_is_not_elevated(self):
        self.request.is_elevated = lambda: False
        response = foo(self.request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/elevate/?next=/foo')
