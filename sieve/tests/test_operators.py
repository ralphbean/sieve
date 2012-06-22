import lxml.etree
import sieve.operators as ops
from nose.tools import raises


def test_eq_xhtml():
    b = "<foo><bar>Value</bar></foo>"
    c = """
<foo>
    <bar>
        Value
    </bar>
</foo>
"""
    ops.eq_xhtml(b, c)


def test_eq_html_wrapped():
    b = "<foo></foo><bar>Value</bar>"
    c = """
<foo>
</foo>
    <bar>
        Value
    </bar>
"""
    ops.eq_xhtml(b, c, wrapped=True)


@raises(lxml.etree.XMLSyntaxError)
def test_bad_xhtml():
    b = '<foo'
    ops.eq_xhtml(b, b)


@raises(lxml.etree.XMLSyntaxError)
def test_bad_xhtml_too():
    ops.eq_xhtml("<foo/>", '<foo')
