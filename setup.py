#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import with_statement
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import lazyxml


with open('README.md') as fp:
    readme = fp.read()

with open('CHANGELOG') as fp:
    changelog = fp.read()

with open('LICENSE') as fp:
    license = fp.read()

setup(name='lazyxml',
      version=lazyxml.__version__,
      description='lazyxml: simple xml parse and build lib',
      long_description=readme + '\n\n' + changelog,
      author='Zonglong Fan',
      author_email='lazyboy.fan@gmail.com',
      maintainer='Zonglong Fan',
      maintainer_email='lazyboy.fan@gmail.com',
      url='https://github.com/heronotears',
      packages=['lazyxml'],
      license=license,
      platforms=['any'],
      )