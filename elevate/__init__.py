"""
elevate
~~~~

:copyright: (c) 2017-present by Justin Mayer.
:copyright: (c) 2014-2016 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('elevate').version
except Exception:  # pragma: no cover
    VERSION = 'unknown'
