sieve
=====

:Author: Ralph Bean <rbean@redhat.com>

XML Comparison Utils

.. comment: split here

Ripped from `FormEncode <http://pypi.python.org/pypi/FormEncode>`_ and `strainer
<http://pypi.python.org/pypi/strainer>`_ just to support Pythons 2 and 3.
Intended for use in your webapp test suites.

Build Status
------------

.. |master| image:: https://secure.travis-ci.org/ralphbean/sieve.png?branch=master
   :alt: Build Status - master branch
   :target: http://travis-ci.org/#!/ralphbean/sieve

.. |develop| image:: https://secure.travis-ci.org/ralphbean/sieve.png?branch=develop
   :alt: Build Status - develop branch
   :target: http://travis-ci.org/#!/ralphbean/sieve

+----------+-----------+
| Branch   | Status    |
+==========+===========+
| master   | |master|  |
+----------+-----------+
| develop  | |develop| |
+----------+-----------+


For Example
-----------

There are two main functions you might care to use: ``eq_xml``
and ``in_xml``::

    >>> from sieve.operators import eq_xml, in_xml
    >>> a = "<foo><bar>Value</bar></foo>"
    >>> b = """
    ... <foo>
    ...     <bar>
    ...         Value
    ...     </bar>
    ... </foo>
    ... """
    >>> eq_xml(a, b)
    True
    >>> c = "<html><body><foo><bar>Value</bar></foo></body></html"
    >>> in_xml(a, c)  # 'needle' in a 'haystack'
    True

There are also two sibling convenience functions: ``assert_eq_xml``
and ``assert_in_xml``.
