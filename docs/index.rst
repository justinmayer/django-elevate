Welcome to Elevate
==================

Elevate, also known as ``django-elevate``, is an implementation of GitHub's
`Sudo Mode`_ for `Django`_.

What is this for?
~~~~~~~~~~~~~~~~~
Elevate provides an extra layer of security beyond initial user authentication.
Views can be decorated with ``@elevate_required``, and then users must
re-authenticate to access that resource. This might be useful for deleting objects,
canceling subscriptions, and other sensitive operations. After re-authentication,
the user has elevated permissions for the duration of ``ELEVATE_COOKIE_AGE``.
This duration is independent of the normal session duration, allowing for short
elevated permission durations while still retaining long user sessions.

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pip install django-elevate

Compatibility
~~~~~~~~~~~~~
* Django 2.2 - 3.1
* Python 3.5 - 3.9
* pypy3

Contents
~~~~~~~~

.. toctree::
   :maxdepth: 2

   getting-started/index
   config/index
   usage/index
   contributing/index
   how/index
   security/index
   changelog/index


.. _Sudo Mode: https://github.com/blog/1513-introducing-github-sudo-mode
.. _Django: https://www.djangoproject.com/
