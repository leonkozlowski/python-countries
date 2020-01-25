"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
     name='python-countries',
     version='1.0.0',
     description='Python bindings for REST Countries API',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/leonkozlowski/python-countries',
     author='Leon Kozlowski',
     author_email='leonkozlowski@gmail.com',
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires='>=3.6',
     keywords='REST Countries API',
     packages=find_packages(),
     install_requires=[
         'requests',
     ]
)
