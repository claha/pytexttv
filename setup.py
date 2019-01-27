"""Setup script for pytexttv."""
from setuptools import setup, find_packages

setup(
    name='pytexttv',
    version='0.0.1',
    author='Claes Hallstrom',
    author_email='hallstrom.claes@gmail.com',
    description='Retrieve pages from text tv',
    license='Apache License 2.0',
    url='https://github.com/claha/pytexttv',
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
