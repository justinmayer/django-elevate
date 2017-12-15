"""
elevate.forms
~~~~~~~~~~~~~

:copyright: (c) 2017-present by Justin Mayer.
:copyright: (c) 2014-2016 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from django import forms
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _


class ElevateForm(forms.Form):
    """
    A simple password input form used by the default :func:`~elevate.views.elevate` view. """
    password = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput(attrs={'autofocus': True})
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ElevateForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        username = self.user.get_username()
        if auth.authenticate(username=username, password=self.data['password']):
            return self.data['password']
        raise forms.ValidationError(_('Incorrect password'))
