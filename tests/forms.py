from django.forms import ValidationError

from elevate.forms import ElevateForm
from .base import BaseTestCase
from .models import EmailUser


class ElevateFormTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.login()

    def test_integration_empty(self):
        self.assertFalse(ElevateForm(self.request, self.user).is_valid())

    def test_integration_invalid_password(self):
        self.assertFalse(
            ElevateForm(self.request, self.user, {'password': 'lol'}).is_valid()
        )

    def test_integration_valid_password(self):
        self.assertTrue(
            ElevateForm(self.request, self.user, {'password': 'foo'}).is_valid()
        )

    def test_integration_secondary_auth_valid_password(self):
        self.assertTrue(
            ElevateForm(self.request, self.user, {'password': 'stub'}).is_valid()
        )

    def test_clean_password_invalid_password(self):
        with self.assertRaises(ValidationError):
            ElevateForm(self.request, self.user, {'password': 'lol'}).clean_password()

    def test_clean_password_valid_password(self):
        password = 'foo'
        self.assertEqual(
            ElevateForm(self.request, self.user, {'password': password}).clean_password(),
            password
        )

    def test_clean_password_secondary_auth_valid_password(self):
        password = 'stub'
        self.assertEqual(
            ElevateForm(self.request, self.user, {'password': password}).clean_password(),
            password
        )

    def test_integration_custom_user(self):
        self.login(EmailUser)
        self.assertTrue(
            ElevateForm(self.request, self.user, {'password': 'foo'}).is_valid()
        )
