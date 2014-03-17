#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

import {{cookiecutter.app_name}}
import sys


REQUIREMENTS = [i.strip() for i in open("requirements/prod.txt").readlines()
                        if not (i.startswith("http") or i.startswith('#') or i.startswith('git'))]

dependency_links = [i.strip() for i in open("requirements/prod.txt").readlines()
                            if (i.startswith("http") or i.startswith('git'))]

if (len(sys.argv) > 1 and sys.argv[1] == 'develop') or os.environ.get('{{cookiecutter.app_name}}_ENV') == 'dev':
    #add in the dev requirements
    REQUIREMENTS += [i.strip() for i in open("requirements/dev.txt").readlines()
                        if not (i.startswith("http") or i.startswith('-') or i.startswith('#'))]

classifiers = [
    "Development Status :: 3 - Alpha",
    "Environment :: Web Environment",
    "Framework :: Flask",
    "Intended Audience :: Developers",
    "License :: All rights reserved.",
    "Natural Language :: English",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: JavaScript",
    "Programming Language :: Python :: 2.7",
    'Programming Language :: Python',
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    'Topic :: Software Development :: Libraries :: Python Modules'
]

try:
    long_description = open('README.md').read()
except:
    long_description = {{cookiecutter.app_name}}.__description__

setup(name='{{cookiecutter.app_name}}',
      version={{cookiecutter.app_name}}.__version__,
      description={{cookiecutter.app_name}}.__description__,
      long_description=long_description,
      classifiers=classifiers,
      keywords='{{cookiecutter.app_name}} flask mongodb sqlalchemy',
      author={{cookiecutter.app_name}}.__author__,
      author_email={{cookiecutter.app_name}}.__email__,
      url='http://{{cookiecutter.app_name}}project.org',
      download_url="https://github.com/pythonhub/{{cookiecutter.app_name}}/tarball/master",
      license={{cookiecutter.app_name}}.__license__,
      packages=find_packages(exclude=('doc', 'docs',)),
      namespace_packages=['{{cookiecutter.app_name}}'],
      package_dir={'{{cookiecutter.app_name}}': '{{cookiecutter.app_name}}'},
      zip_safe=False,
      install_requires=REQUIREMENTS,
      dependency_links=dependency_links,
      #scripts=['{{cookiecutter.app_name}}/bin/{{cookiecutter.app_name}}-admin.py'],
      include_package_data=True,
      test_suite='nose.collector',
      entry_points={
        'console_scripts': [
         ]
      })

