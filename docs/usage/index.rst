Usage
=====

Once we have ``django-elevate`` :doc:`installed </getting-started/index>` and
:doc:`configured </config/index>`, we need to decide which views should be secured.

.. function:: elevate.decorators.elevate_required()

    The meat of ``django-elevate`` comes from decorating your views with ``@elevate_required`` much in the
    same way that ``@login_required`` works.

    Let's pretend that we have a page on our site that has sensitive information that we want to make
    extra sure that a user is allowed to see it:

    .. code-block:: python

        from elevate.decorators import elevate_required

        @login_required  # Make sure they're at least logged in
        @elevate_required  # On top of being logged in, are you in Elevate mode?
        def super_secret_stuff(request):
            return HttpResponse('your social security number')

    That's it! When a user visits this page and they don't have the correct permission, they'll be
    redirected to a page and prompted for their password. After entering their password, they'll be
    redirected back to this page to continue on what they were trying to do.

.. class:: elevate.mixins.ElevateMixin

    ``ElevateMixin`` provides an easy way to elevate a class-based view. Any view
    that inherits from this mixin is automatically wrapped by the
    ``@elevate_required`` decorator.

    This works well with the ``LoginRequiredMixin`` from
    `django-braces <https://django-braces.readthedocs.io/>`_:

    .. code-block:: python

        from django.views import generic
        from braces.views import LoginRequiredMixin
        from elevate.mixins import ElevateMixin

        class SuperSecretView(LoginRequiredMixin, ElevateMixin, generic.TemplateView):
            template_name = 'secret/super-secret.html'

.. method:: request.is_elevated()

Returns a boolean to indicate if the current request is in Elevate mode or not. This gets added on by
the :class:`~elevate.middleware.ElevateMiddleware`. This is an shortcut for calling
:func:`~elevate.utils.has_elevated_privileges` directly.

.. class:: elevate.middleware.ElevateMiddleware

    By default, you just need to add this to your ``MIDDLEWARE`` list.

    .. method:: has_elevated_privileges(self, request)

    Subclass and override :func:`~elevate.middleware.ElevatedMiddleware.has_elevated_privileges` if you'd like
    to override the default behavior of :func:`request.is_elevated() <request.is_elevated()>`.

    .. method:: process_request(self, request)

    Adds :func:`~request.is_elevated()` to the request.

    .. method:: process_response(self, request, response)

    Controls the behavior of setting and deleting the Elevate cookie for the browser.


.. module:: elevate.utils

.. function:: grant_elevated_privileges(request, max_age=ELEVATE_COOKIE_AGE)

    Assigns a random token to the user's session that allows them to have elevated permissions.

    .. code-block:: python

        from elevate.utils import grant_elevated_privileges
        token = grant_elevated_privileges(request)

.. function:: revoke_elevated_privileges(request)

    Revoke elevated privileges from a request explicitly

    .. code-block:: python

        from elevate.utils import revoke_elevated_privileges
        revoke_elevated_privileges(request)

.. function:: has_elevated_privileges(request)

    Check if a request is allowed to perform elevated actions.

    .. code-block:: python

        from elevate.utils import has_elevated_privileges
        has_elevate = has_elevated_privileges(request)
