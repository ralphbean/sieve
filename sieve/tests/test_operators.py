import lxml.etree
import sieve.operators as ops
from nose.tools import raises


@raises(AssertionError)
def test_assert_eq_xml():
    ops.assert_eq_xml("<foo></foo>", "<bar></bar>")

def test_eq_xml():
    b = "<foo><bar>Value</bar></foo>"
    c = """
<foo>
    <bar>
        Value
    </bar>
</foo>
"""
    ops.eq_xml(b, c)


def test_eq_html_wrapped():
    b = "<foo></foo><bar>Value</bar>"
    c = """
<foo>
</foo>
    <bar>
        Value
    </bar>
"""
    ops.eq_xml(b, c, wrapped=True)


@raises(lxml.etree.XMLSyntaxError)
def test_bad_xml():
    b = '<foo'
    ops.eq_xml(b, b)


@raises(lxml.etree.XMLSyntaxError)
def test_bad_xml_too():
    ops.eq_xml("<foo/>", '<foo')
