#!/usr/bin/env python
"""
django-elevate
~~~~~~~~~~~~~~

:copyright: (c) 2017-present by Justin Mayer.
:copyright: (c) 2014-2016 by Matt Robenolt.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

install_requires = []

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-django',
    'flake8',
]


with open('README.rst') as f:
    long_description = f.read()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        import sys
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='django-elevate',
    version='1.0.1',
    author='Justin Mayer',
    author_email='entroP@gmail.com',
    url='https://github.com/justinmayer/django-elevate',
    description='Extra security for your sensitive pages',
    license='BSD',
    long_description=long_description,
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    extras_require={
        'tests': tests_require,
    },
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
)
