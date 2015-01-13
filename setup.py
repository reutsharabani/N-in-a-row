__author__ = 'reut'

from setuptools import setup, find_packages
from codecs import open
from os import path
here = path.abspath(path.dirname(__file__))
# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()
    setup(
        name='sample',
        version='0.0.1',
        description='N-in-a-row Game',
        long_description='Simple implementation for the N-in-a-row (originally 4-in-a-row)'
                         ' classic game using tkinter GUI',
        url='https://github.com/reutsharabani/N-in-a-row',
        # Author details
        author='Reut Sharabani',
        author_email='reut.sharabani@gmail.com',
        # Choose your license
        license='MIT',
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Development Status :: 1 - Experimental',
            'Intended Audience :: Young nephews',
            'Topic :: Fun and Games:: Board Games',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7'
        ],
        # What does your project relate to?
        keywords='Simple and fun board game to play with younger members of family.',
        # You can just specify the packages manually here if your project is
        #  simple. Or you can use find_packages().
        packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
        install_requires=['']
)