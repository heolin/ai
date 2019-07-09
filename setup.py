import os, codecs
from setuptools import setup, find_packages


setup(
    name='ai',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'sklearn',
        'numpy'
    ]
)

