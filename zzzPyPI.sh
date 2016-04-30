#!/bin/bash


# install package locally
pip install -e .
# or:
# python setup.py develop


# install Twine and Wheek packages
pip install --upgrade twine wheel


# deploy package to PyPI
python setup.py sdist
python setup.py bdist_wheel --universal
python setup.py register
twine upload dist/*
# or:
# python setup.py sdist bdist_wheel upload
