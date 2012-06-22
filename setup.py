from setuptools import setup, find_packages
import sys
import os

try:
    import multiprocessing
    import logging
except:
    pass

version = '0.1'

setup(name='sieve',
      version=version,
      description="XML Comparison",
      long_description="""\
""",
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='',
      author='Ralph Bean',
      author_email='rbean@redhat.com',
      url='http://github.com/ralphbean/sieve',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'lxml',
      ],
      tests_require=[
          'nose',
      ],
      test_suite='nose.collector',
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
