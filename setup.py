#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='leopards',
    version='1.0.0',
    description='Allows filtering & aggregation iterable of dictionary by another dictionary. Much faster than pandas',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    #long_description="Filters List of Dictionaries by a query dictionary",
    author='Mohamed El-Kalioby',
    author_email = 'mkalioby@mkalioby.com',
    url = 'https://github.com/mkalioby/leopards/',
    download_url='https://github.com/mkalioby/leopards/',
    license='MIT',
    packages=find_packages(),
    install_requires=[
       ],
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False, # because we're including static files
    classifiers=[
        #"Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
]
)
