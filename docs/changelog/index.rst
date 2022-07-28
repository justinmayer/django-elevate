Changelog
=========

2.0.3 - 2022-07-28
------------------

- Add Django 4.0 support
  - Add `ELEVATE_TOKEN_LENGTH` setting as `get_random_string` no longer has a default length
- Remove Django 3.1 from test matrix
- Remove Python 3.6 from test matrix
- No longer build wheel as universal as Python 2 is not supported

2.0.2 - 2021-06-02
------------------

Added `request` to the `authenticate()` call to prevent errors from authenication backends that require it.

2.0.1 - 2021-04-11
------------------

Add Django 3.2 support and remove Django 3.0 support

2.0.0 - 2020-10-25
------------------

- Drop support for Python 2 and Python 3.4
- Drop support for Django 1.8-2.1
- Add support for Python 3.8 and 3.9
- Add support for Django 3.0 and 3.1
- Removed code that was required to support older versions of Python and Django

1.0.1 - 2019-06-06
------------------

* Add support for Django 2.1 and 2.2
* Add Python 3.7, and drop Python 3.3, from test matrix

1.0.0 - 2018-06-25
------------------

* Add support for Django 2.0, 1.11, and 1.10
* Auto-focus input on password field
* Fork and rename project
