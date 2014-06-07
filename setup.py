# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
setup(
    name='text2image',
    version='0.1-dev',
    description='A library to convert large text strings to image files',
    long_description=open('README.md').read(),
    author='José M. Franco-Valiente',
    author_email='josemi_fv@hotmail.com',
    license=open('LICENSE').read(),
    platforms=["any"],
    packages=find_packages(),
    test_suite="text2image.tests",
    install_requires=[
        "pillow==2.4.0",
        "wsgiref==0.1.2"
    ]
)