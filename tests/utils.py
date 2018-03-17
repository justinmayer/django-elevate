from elevate.settings import COOKIE_NAME, COOKIE_AGE
from elevate.utils import (
    grant_elevated_privileges,
    revoke_elevated_privileges,
    has_elevated_privileges,
)

from django.core.signing import BadSignature

from .base import BaseTestCase


class GrantElevatedPrivilegesTestCase(BaseTestCase):
    def assertRequestHasToken(self, request, max_age):
        token = request.session[COOKIE_NAME]

        self.assertRegexpMatches(
            token, '^\w{12}$'
        )
        self.assertTrue(request._elevate)
        self.assertEqual(request._elevate_token, token)
        self.assertEqual(request._elevate_max_age, max_age)

    def test_grant_token_not_logged_in(self):
        with self.assertRaises(ValueError):
            grant_elevated_privileges(self.request)

    def test_grant_token_default_max_age(self):
        self.login()
        token = grant_elevated_privileges(self.request)
        self.assertIsNotNone(token)
        self.assertRequestHasToken(self.request, COOKIE_AGE)

    def test_grant_token_explicit_max_age(self):
        self.login()
        token = grant_elevated_privileges(self.request, 60)
        self.assertIsNotNone(token)
        self.assertRequestHasToken(self.request, 60)

    def test_without_user(self):
        delattr(self.request, 'user')
        token = grant_elevated_privileges(self.request)
        self.assertIsNone(token)


class RevokeElevatedPrivilegesTestCase(BaseTestCase):
    def assertRequestNotElevated(self, request):
        self.assertFalse(self.request._elevate)
        self.assertNotIn(COOKIE_NAME, self.request.session)

    def test_revoke_elevated_privileges_noop(self):
        revoke_elevated_privileges(self.request)
        self.assertRequestNotElevated(self.request)

    def test_revoke_elevated_privileges(self):
        self.login()
        grant_elevated_privileges(self.request)
        revoke_elevated_privileges(self.request)
        self.assertRequestNotElevated(self.request)


class HasElevatedPrivilegesTestCase(BaseTestCase):
    def test_untouched(self):
        self.assertFalse(has_elevated_privileges(self.request))

    def test_granted(self):
        self.login()
        grant_elevated_privileges(self.request)
        self.assertTrue(has_elevated_privileges(self.request))

    def test_revoked(self):
        self.login()
        grant_elevated_privileges(self.request)
        revoke_elevated_privileges(self.request)
        self.assertFalse(has_elevated_privileges(self.request))

    def test_cookie_and_token_match(self):
        self.login()

        def get_signed_cookie(key, salt='', max_age=None):
            return 'abc123'
        self.request.session[COOKIE_NAME] = 'abc123'
        self.request.get_signed_cookie = get_signed_cookie
        self.assertTrue(has_elevated_privileges(self.request))

    def test_cookie_and_token_mismatch(self):
        self.login()

        def get_signed_cookie(key, salt='', max_age=None):
            return 'nope'
        self.request.session[COOKIE_NAME] = 'abc123'
        self.assertFalse(has_elevated_privileges(self.request))

    def test_cookie_bad_signature(self):
        self.login()

        def get_signed_cookie(key, salt='', max_age=None):
            raise BadSignature
        self.request.session[COOKIE_NAME] = 'abc123'
        self.assertFalse(has_elevated_privileges(self.request))

    def test_missing_keys(self):
        self.login()
        self.assertFalse(has_elevated_privileges(self.request))
