#!/usr/bin/python

from setuptools import setup

def readme():
  with open('README.rst') as f:
    return f.read()

setup(name='word_tree',
      version='0.1',
      description='Dictionary optimised for progressive lookup',
      long_description=readme(),
      classifiers=[
        'Programming Language :: Python :: 2.7',
      ],
      keywords='dictionary word incremental lookup',
      url='http://github.com/OldIronHorse/word_tree',
      author='Simon Redding',
      author_email='s1m0n.r3dd1ng@gmail.com',
      license='GPL3',
      packages=['word_tree'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
