#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pssapi',
    version='1.0.0.dev1',
    description='Wrapper for the Pixel Starships API',
    long_description=long_description,
    author='Zukunftsmusik',
    author_email='',
    url='https://github.com/Zukunftsmusik/pssapi.py',
    license='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.9',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.9',
    install_requires=[
        'aiohttp==3.8.3',
        'jinja2==3.1.2',
        'pytz==2022.2.1',
        'strenum==0.4.8'
    ],
)
