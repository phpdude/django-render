#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django render',
	  version=".".join(map(str, __import__("render").__version__)),
	  description='Django templates rendering decorator',
	  author='Alexandr I. Shurigin',
	  author_email='ya@helldude.ru',
	  maintainer='Alexandr I. Shurigin',
	  maintainer_email='ya@helldude.ru',
	  url='http://github.com/coffin/coffin',
	  packages=find_packages(),
	  classifiers=[
		  "Framework :: Django",
		  "Intended Audience :: Developers",
		  "Intended Audience :: System Administrators",
		  "Operating System :: OS Independent",
		  "Topic :: Software Development"
	  ],
	  )
