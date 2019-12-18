"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
     name='python-countries',
     version='0.0.1',
     description='Python bindings for REST Countries API',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/leonkozlowski/python-countries',
     author='Leon Kozlowski',
     author_email='leonkozlowski@gmail.com',
     classifiers=[
         'Development Status :: 3 - Development',
         'Intended Audience :: Developers',
         'Topic :: Software Development :: RESTful API Wrapper',
         'Programming Language :: Python :: 3.6'
     ],
     keywords='REST Countries API',
     packages=find_packages(),
     install_requires=[
         'requests',
     ]
)