#!/usr/bin/env python

from setuptools import setup, find_packages
import bandcamp_get
import os

def read(*names):
    values = dict()
    extensions = ['.txt', '.md']
    for name in names:
        value = ''
        for extension in extensions:
            filename = name + extension
            if os.path.isfile(filename):
                value = open(name + extension).read()
                break
        values[name] = value
    return values

long_description = """
%(README)s

News
====

%(CHANGES)s

""" % read('README', 'CHANGES')

setup(
    name='bandcamp_get',
    version=bandcamp_get.__version__,
    description='automated music downloading via selenium',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    keywords='bandcamp-get bandcamp free music download guerrilla mail selenium webdriver downloader automated',
    author='Hunter Hammond',
    author_email='huntrar@gmail.com',
    maintainer='Hunter Hammond',
    maintainer_email='huntrar@gmail.com',
    url='https://github.com/huntrar/bandcamp-get',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bandcamp-get = bandcamp_get.bandcamp_get:command_line_runner',
        ]
    },
    install_requires=[
        'lxml',
        'requests'
    ]
)
