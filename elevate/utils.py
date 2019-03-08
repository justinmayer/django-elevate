"""
elevate.utils
~~~~~~~~~~~~~

:copyright: (c) 2017-present by Justin Mayer.
:copyright: (c) 2014-2016 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from django.core.signing import BadSignature
from django.utils import http
from django.utils.crypto import get_random_string, constant_time_compare
import django

from elevate.settings import COOKIE_NAME, COOKIE_AGE, COOKIE_SALT


def grant_elevated_privileges(request, max_age=COOKIE_AGE):
    """
    Assigns a random token to the user's session
    that allows them to have elevated permissions
    """
    user = getattr(request, 'user', None)

    # If there's not a user on the request, just noop
    if user is None:
        return

    if not is_authenticated(user):
        raise ValueError('User needs to be logged in to be elevated')

    # Token doesn't need to be unique,
    # just needs to be unpredictable and match the cookie and the session
    token = get_random_string()
    request.session[COOKIE_NAME] = token
    request._elevate = True
    request._elevate_token = token
    request._elevate_max_age = max_age
    return token


def revoke_elevated_privileges(request):
    """
    Revoke elevated privileges from a request explicitly
    """
    request._elevate = False
    if COOKIE_NAME in request.session:
        del request.session[COOKIE_NAME]


def has_elevated_privileges(request):
    """
    Check if a request is allowed to perform Elevate actions
    """
    if getattr(request, '_elevate', None) is None:
        try:
            request._elevate = (
                is_authenticated(request.user) and
                constant_time_compare(
                    request.get_signed_cookie(COOKIE_NAME, salt=COOKIE_SALT, max_age=COOKIE_AGE),
                    request.session[COOKIE_NAME]
                )
            )
        except (KeyError, BadSignature):
            request._elevate = False
    return request._elevate


def is_authenticated(user):
    """
    Check if a user is authenticated

    In Django 1.10 User.is_authenticated was changed to a property and
    backwards compatible support for is_authenticated being callable was
    finally removed in Django 2.0. This function can be removed once support
    Django versions earlier than 1.10 are dropped.
    """
    if callable(user.is_authenticated):
        return user.is_authenticated()
    else:
        return user.is_authenticated


def is_safe_url(url, allowed_hosts, require_https=False):
    """
    Wrapper around is_safe_url for Django versions < 1.11
    """
    if django.VERSION >= (1, 11):
        return http.is_safe_url(url, allowed_hosts=allowed_hosts, require_https=require_https)
    else:
        return http.is_safe_url(url, allowed_hosts[0])
