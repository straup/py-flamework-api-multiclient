#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()

setup(
    name='flamework.api.multiclient',
    namespace_packages=['flamework', 'flamework.api', 'flamework.api.multiclient'],
    version='0.1',
    description='Python bindings for Flamework-derived APIs with support for multiple parallel requests (using grequests).',
    author='Aaron Straup Cope',
    url='https://github.com/straup/py-flamework-api-multiclient',
    install_requires=[
        'flamework.api',
        'grequests',
        ],
    dependency_links=[
        'https://github.com/straup/py-flamework-api/tarball/master#egg=flamework-api-0.2',
      ],
    packages=packages,
    scripts=[],
    download_url='https://github.com/straup/py-flamework-api-multiclient/releases/tag/v0.1',
    license='BSD')
