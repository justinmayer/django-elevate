django-elevate
==============

.. image:: https://travis-ci.org/justinmayer/django-elevate.svg?branch=master
   :target: https://travis-ci.org/justinmayer/django-elevate

.. image:: https://coveralls.io/repos/github/justinmayer/django-elevate/badge.svg?branch=master
   :target: https://coveralls.io/github/justinmayer/django-elevate?branch=master

..

    | Elevate mode offers an extra layer of security for your most sensitive pages.
    | This is an implementation of GitHub's `Sudo Mode`_ for `Django`_.

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
* Django 1.8 - 2.0
* Python 2.7 - 3.6
* pypy

Resources
~~~~~~~~~
* `Documentation <https://django-elevate.readthedocs.io/>`_
* `Security <https://django-elevate.readthedocs.io/en/latest/security/index.html>`_
* `Changelog <https://django-elevate.readthedocs.io/en/latest/changelog/index.html>`_


.. _Sudo Mode: https://github.com/blog/1513-introducing-github-sudo-mode
.. _Django: https://www.djangoproject.com/
