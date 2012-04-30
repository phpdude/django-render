#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django-render',
    version=".".join(map(str, __import__("render").__version__)),
    description='Django templates rendering sugar',
    author='Alexandr I. Shurigin',
    author_email='ya@helldude.ru',
    maintainer='Alexandr I. Shurigin',
    maintainer_email='ya@helldude.ru',
    url='https://github.com/phpdude/django-render',
    packages=find_packages(),
    classifiers=[
        "Framework :: Django",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ], requires=['django', "coffin", "jinja2"],
)
