from .base import BaseTestCase

from django.http import HttpResponse

from elevate.settings import COOKIE_NAME
from elevate.middleware import ElevateMiddleware
from elevate.utils import (
    grant_elevated_privileges,
    revoke_elevated_privileges,
)


class ElevateMiddlewareTestCase(BaseTestCase):
    middleware = ElevateMiddleware()

    def assertSignedCookieEqual(self, v1, v2, reason=None):
        value, _, _ = v1.split(':')
        return self.assertEqual(value, v2, reason)

    def test_process_request_raises_without_session(self):
        del self.request.session
        with self.assertRaises(AssertionError):
            self.middleware.process_request(self.request)

    def test_process_request_adds_is_elevated(self):
        self.middleware.process_request(self.request)
        self.assertFalse(self.request.is_elevated())

    def test_process_response_noop(self):
        response = self.middleware.process_response(self.request, HttpResponse())
        self.assertEqual(len(response.cookies.items()), 0)

    def test_process_response_with_elevate_sets_cookie(self):
        self.login()
        self.middleware.process_request(self.request)
        grant_elevated_privileges(self.request)
        response = self.middleware.process_response(self.request, HttpResponse())
        morsels = list(response.cookies.items())
        self.assertEqual(len(morsels), 1)
        self.assertEqual(morsels[0][0], COOKIE_NAME)
        _, elevate = morsels[0]
        self.assertEqual(elevate.key, COOKIE_NAME)
        self.assertSignedCookieEqual(elevate.value, self.request._elevate_token)
        self.assertEqual(elevate['max-age'], self.request._elevate_max_age)
        self.assertTrue(elevate['httponly'])

        # Asserting that these are insecure together explicitly
        # since it's a big deal to not fuck up
        self.assertFalse(self.request.is_secure())
        self.assertFalse(elevate['secure'])  # insecure request

    def test_process_response_sets_secure_cookie(self):
        self.login()
        self.request.is_secure = lambda: True
        self.middleware.process_request(self.request)
        grant_elevated_privileges(self.request)
        response = self.middleware.process_response(self.request, HttpResponse())
        morsels = list(response.cookies.items())
        self.assertEqual(len(morsels), 1)
        self.assertEqual(morsels[0][0], COOKIE_NAME)
        _, elevate = morsels[0]
        self.assertTrue(self.request.is_secure())
        self.assertTrue(elevate['secure'])

    def test_process_response_elevate_revoked_removes_cookie(self):
        self.login()
        self.middleware.process_request(self.request)
        grant_elevated_privileges(self.request)
        self.request.COOKIES[COOKIE_NAME] = self.request._elevate_token
        revoke_elevated_privileges(self.request)
        response = self.middleware.process_response(self.request, HttpResponse())
        morsels = list(response.cookies.items())
        self.assertEqual(len(morsels), 1)
        self.assertEqual(morsels[0][0], COOKIE_NAME)
        _, elevate = morsels[0]

        # Deleting a cookie is just setting it's value to empty
        # and telling it to expire
        self.assertEqual(elevate.key, COOKIE_NAME)
        self.assertFalse(elevate.value)
        self.assertEqual(elevate['max-age'], 0)

    def test_process_response_elevate_revoked_without_cookie(self):
        self.login()
        self.middleware.process_request(self.request)
        grant_elevated_privileges(self.request)
        revoke_elevated_privileges(self.request)
        response = self.middleware.process_response(self.request, HttpResponse())
        morsels = list(response.cookies.items())
        self.assertEqual(len(morsels), 0)
