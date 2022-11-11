#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='QyPy',
    version='0.8.0',
    description='Allows filters iterable of dictionary by another dictionary',
    #long_description=open("README.md").read(),
    #long_description_content_type="text/markdown",
    long_description="Filters List of Dictionaries by a query dictionary",
    author='Mohamed El-Kalioby',
    author_email = 'mkalioby@mkalioby.com',
    url = 'https://github.com/mkalioby/QyPy/',
    download_url='https://github.com/mkalioby/QyPy/',
    license='MIT',
    packages=find_packages(),
    install_requires=[
       ],
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False, # because we're including static files
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
]
)
