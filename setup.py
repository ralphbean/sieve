from setuptools import setup, find_packages
import sys
import os

try:
    import multiprocessing
    import logging
except:
    pass

def long_description():
    f = open("README.rst")
    content = f.read().strip()
    f.close()
    return content.split('split here', 1)[1]


setup(name='sieve',
      version='0.1.9',
      description="XML Comparison Utils",
      long_description=long_description(),
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: MIT License",
          "Topic :: Software Development :: Libraries",
          "Topic :: Software Development :: Testing",
          "Topic :: Text Processing :: Markup :: HTML",
          "Topic :: Text Processing :: Markup :: XML",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.2",
      ],
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
          'six',
          'markupsafe',
      ],
      tests_require=[
          'nose',
      ],
      test_suite='nose.collector',
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
