Release type: patch

- Added Django 4.0 support
    - Added ELEVATE_TOKEN_LENGTH setting as `get_random_string` no longer has a
      default length
- Removed Django 3.1 from test matrix
- Removed Python 3.6 from test matrix
- No longer build wheel as universal - we don't support Python 2
