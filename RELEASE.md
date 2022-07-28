Release type: patch

- Add Django 4.0 support
  - Add `ELEVATE_TOKEN_LENGTH` setting as `get_random_string` no longer has a default length
- Remove Django 3.1 from test matrix
- Remove Python 3.6 from test matrix
- No longer build wheel as universal as Python 2 is not supported
