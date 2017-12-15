Getting Started
===============

Installation
~~~~~~~~~~~~

First, install the ``django-elevate`` library with `pip <https://pypi.python.org/pypi/pip>`_.

.. code-block:: console

    $ pip install django-elevate

Next, we need to add the ``elevate`` application to our ``INSTALLED_APPS``. Installing the application
will automatically register the ``user_logged_in`` and ``user_logged_out`` signals that are needed.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'elevate',
    )

Now we need to add Elevate’s middleware to the ``MIDDLEWARE`` setting:

.. code-block:: python

    MIDDLEWARE = (
        # ...
        'elevate.middleware.ElevateMiddleware',
    )

.. note::

    ``elevate.middleware.ElevateMiddleware`` **must** be installed after
    ``django.contrib.session.middleware.SessionMiddleware``.

Proceed to the :doc:`/config/index` documentation.
