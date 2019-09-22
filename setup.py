#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='mkrepo',
    version='0.1.3',
    packages=find_packages(),
    description='Maintain deb and rpm repos on s3',
    author='Konstantin Nazarov',
    author_email='mail@kn.am',
    url='https://github.com/tarantool/mkrepo',
    keywords=['rpm', 'deb'],
    classifiers=[],
    scripts=['bin/mkrepo'],
    install_requires=['boto3==1.4.1', 'backports.lzma==0.0.14'],
)
