#!/usr/bin/env python

from distutils.core import setup

setup(name='{{ cookiecutter.package_name }}',
      version='0.1dev',
      description='This is https://github.com/mozilla/{{ cookiecutter.package_name }}',
      author='{{ cookiecutter.project_author }}',
      author_email='',
      url='https://github.com/mozilla/{{ cookiecutter.package_name }}')
