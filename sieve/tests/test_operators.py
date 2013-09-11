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
    assert ops.eq_xml(b, c)


def test_eq_html_wrapped():
    b = "<foo></foo><bar>Value</bar>"
    c = """
<foo>
</foo>
    <bar>
        Value
    </bar>
"""
    assert ops.eq_xml(b, c, wrapped=True)


def test_in_html_valid():
    inputs = [
        (
            "<foo>bar</foo>",
            "<foo>bar</foo>"
        ),
        (
            "<foo>bar</foo>",
            "<body><foo>bar</foo></body>"
        ),
        (
            "<foo>bar</foo>",
            "<html><head>blah</head><body><foo>bar</foo></body></html>"
        ),
    ]
    for needle, haystack in inputs:
        def test1(n, h):
            assert ops.in_xml(n, h)

        def test2(n, h):
            ops.assert_in_xml(n, h)

        yield test1, needle, haystack
        yield test2, needle, haystack

def test_in_html_invalid():
    inputs = [
        (
            "<foo>bar</foo>",
            "<body><foo><baz/>bar</foo></body>"
        ),
        (
            "<foo>bar</foo>",
            "<body><foo></foo></body>"
        ),
        (
            "<foo>bar</foo>",
            "<html><head>blah</head><body><foo><baz/>bar</foo></body></html>"
        ),
    ]
    for needle, haystack in inputs:
        def test(n, h):
            assert not ops.in_xml(n, h)
        yield test, needle, haystack
