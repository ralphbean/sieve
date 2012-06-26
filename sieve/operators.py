from lxml import etree
import sieve.xml_compare as c
import sys
import six


def assert_eq_xml(xml1, xml2, message=None, wrapped=False):
    if not message:
        buf = six.StringIO()
        reporter = lambda x: buf.write(x + '\n')
        result = eq_xml(xml1, xml2, reporter=reporter, wrapped=wrapped)
        if not result:
            reason = buf.getvalue()
            assert result, reason
    else:
        assert eq_xml(xml1, xml2), message


def assert_in_xml(needle, haystack, message=None, wrapped=False):
    if not message:
        buf = six.StringIO()
        reporter = lambda x: buf.write(x + '\n')
        result = in_xml(needle, haystack, reporter=reporter, wrapped=wrapped)
        if not result:
            reason = buf.getvalue()
            assert result, reason
    else:
        assert in_xml(needle, haystack), message


def eq_xml(xml1, xml2, reporter=None, wrapped=False):
    wrapper = lambda x: x.strip()
    if wrapped:
        wrapper = lambda x: "<wrap>" + x + "</wrap>"

    tree1 = etree.fromstring(wrapper(xml1))
    tree2 = etree.fromstring(wrapper(xml2))
    return c.xml_compare(tree1, tree2, reporter)


def in_xml(needle, haystack, reporter=None, wrapped=False):
    wrapper = lambda x: x.strip()
    if wrapped:
        wrapper = lambda x: "<wrap>" + x + "</wrap>"

    tree1 = etree.fromstring(wrapper(needle))
    tree2 = etree.fromstring(wrapper(haystack))
    return c.xml_contains(tree1, tree2, reporter)
