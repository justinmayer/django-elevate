django-elevate
==============

.. image:: https://travis-ci.org/justinmayer/django-elevate.svg?branch=master
   :target: https://travis-ci.org/justinmayer/django-elevate

.. image:: https://coveralls.io/repos/justinmayer/django-elevate/badge.png?branch=master
   :target: https://coveralls.io/r/justinmayer/django-elevate?branch=master

..

    | Elevate mode is an extra layer of security for your most sensitive pages.
    This is an implementation of GitHub's `Sudo Mode
    <https://github.com/blog/1513-introducing-github-sudo-mode>`_ for `Django
    <https://www.djangoproject.com/>`_.

What is this for?
~~~~~~~~~~~~~~~~~
``django-elevate`` provides an extra layer of security for after a user is already logged in. Views can
be decorated with ``@elevate_required``, and then a user
must re-enter their password to view that page. After verifying their password, that user has
elevated permissions for the duration of ``ELEVATE_COOKIE_AGE``. This duration is independent of the
normal session duration allowing short elevated permission durations, but retain long user sessions.

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pip install django-elevate

Compatibility
~~~~~~~~~~~~~
* Django 1.4-1.9
* Python 2.6-3.5
* pypy

Resources
~~~~~~~~~
* `Documentation <https://django-elevate.readthedocs.io/>`_
* `Security <https://django-elevate.readthedocs.io/en/latest/security/index.html>`_
* `Changelog <https://django-elevate.readthedocs.io/en/latest/changelog/index.html>`_
