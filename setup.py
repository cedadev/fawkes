'''Setup for making overall package
'''
__author__ = "Tommy Godfrey"
__copyright__ = "Copyright 2019 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
from setuptools import setup, find_packages

setup(
    name='fawkes-phoenix',
    version='0.1.0',
    description='Extensions to Birdhouse Phoenix',
    author='Tommy Godfrey',
    author_email='tommy.godfrey@stfc.ac.uk',
    url='https://github.com/cedadev/fawkes-phoenix/',
    long_description_content_type='text/markdown',
    license='BSD - See LICENSE file for details',
    packages=find_packages(),
    include_package_data = True,
    python_requires='>=3.0',
    # See:
    # https://www.python.org/dev/peps/pep-0301/#distutils-trove-classification
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ]
)
