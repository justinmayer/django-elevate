Configuration
=============

Settings
~~~~~~~~

By default, all of the settings are optional and define sane and secure defaults.

``ELEVATE_URL``
    The url or view name for the Elevate view. *Default: elevate.views.elevate*

``ELEVATE_REDIRECT_URL``
    Default url to be redirected to after elevating permissions. *Default: /*

``ELEVATE_REDIRECT_FIELD_NAME``
    The querystring argument to be used for redirection. *Default: next*

``ELEVATE_COOKIE_AGE``
    How long should Elevate mode be active for? Duration in seconds. *Default: 10800*

``ELEVATE_COOKIE_DOMAIN``
    The domain to bind the Elevate cookie to. *Default: current exact domain*.

``ELEVATE_COOKIE_HTTPONLY``
    Should the cookie only be accessible via http requests? *Default: True*

    .. note::
        If this is set to ``False``, any JavaScript files have the ability to access this cookie,
        so this should only be changed if you have a good reason to do so.

``ELEVATE_COOKIE_NAME``
    The name of the cookie to be used for Elevate mode. *Default: elevate*

``ELEVATE_COOKIE_PATH``
    Restrict the Elevate cookie to a specific path. *Default: /*

``ELEVATE_COOKIE_SECURE``
    Only transmit the Elevate cookie over https if True. *Default: matches current protocol*

    .. note::
        By default, we will match the protocol that made the request. So if your Elevate page is over
        https, we will set the ``secure`` flag on the cookie so it won't be transmitted over plain
        http. It is highly recommended that you only use ``django-elevate`` over https.

``ELEVATE_COOKIE_SALT``
    An extra salt to be added into the cookie signature. *Default: ''*

``ELEVATE_REDIRECT_TO_FIELD_NAME``
    The name of the session attribute used to preserve the redirect destination
    between the original page request and successful elevated login. *Default: elevate_redirect_to*

``ELEVATE_TOKEN_LENGTH``
    Length of the random string that is stored in the Elevate cookie. *Default: 12*

Set up URLs
~~~~~~~~~~~

We need to hook up one url to use ``django-elevate`` properly. At minimum, you need something like
the following:

.. code-block:: python

    from elevate.views import elevate as elevate_view

    (r'^elevate/$',  # Whatever path you want
        elevate_view,  # Required
        {'template_name': 'elevate/elevate.html'}  # Optionally change the template to be used
    )

Required Template
~~~~~~~~~~~~~~~~~

To get up and running, we last need to create a template for the Elevate page to render. By default,
the package will look for ``elevate/elevate.html`` but can easily be overwritten by setting the
``template_name`` when defining the url definition as seen above.

elevate/elevate.html
--------------------

This template gets rendered with the the following context:

``form``
    An instance of :class:`~elevate.forms.ElevateForm`.

``ELEVATE_REDIRECT_FIELD_NAME``
    The value of ``?next=/foo/``. If ``ELEVATE_REDIRECT_FIELD_NAME`` is ``name``, then expect to find
    ``{{ next }}`` in the context, with the value of ``/foo/``.


After configuring things, we can now :doc:`start securing pages </usage/index>`.
