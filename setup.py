from setuptools import setup

setup(name = 'scopus',
      version='0.1',
      description='Python API for Scopus',
      url='http://github.com/jkitchin/scopus',
      author='John Kitchin',
      author_email='jkitchin@andrew.cmu.edu',
      license='GPL',
      packages=['scopus'],
      scripts=[],
      test_suite = 'nose.collector',
      long_description='''Provides Python functions to retrieve data from the Scopus APIs.''',
      install_requires=[
          'nose'],)
