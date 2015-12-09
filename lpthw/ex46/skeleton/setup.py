# -*- coding: utf-8 -*-

try:
	from setuptools import setup 
except ImportError:
	from distutils.core import setup

config = {
	'description': 'XXXXXXXX',
	'author': 'Artifex Trinity',
	'url': '........',
	'download_url': '.........',
	'author_email': 'artifex4847@outlook.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'ex46'
}

setup(**config)