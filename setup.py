#!/usr/bin/env python3

from setuptools import setup, find_packages, Extension

setup(
    name='launtix',
    version='0.1.0',
    packages=find_packages(exclude=['tests', 'examples']),
    url='https://github.com/yunfachi/launtix',
    license='MIT',
    author='yunfachi',
    author_email='yunfachi@gmail.com', 
    description='Utility for robux laundering'
) 