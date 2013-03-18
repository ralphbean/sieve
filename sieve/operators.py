from __future__ import absolute_import

from lxml import etree, html
import sieve.xml_compare as c
import markupsafe
import sys
import six


def _xml_from_string(string):
    try:
        return etree.fromstring(string)
    except etree.XMLSyntaxError:
        try:
            return html.fromstring(string)
        except etree.XMLSyntaxError:
            print("choked on: " + string)
            raise


def assert_eq_xml(xml1, xml2, message=None, wrapped=False):
    if not message:
        buf = six.StringIO()
        reporter = lambda x: buf.write(x + '\n')
        result = eq_xml(xml1, xml2, reporter=reporter, wrapped=wrapped)
        if not result:
            reporter("xml1 %s\n does not equal xml2\n %s" % (xml1, xml2))
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
            reporter("needle %s\n not in haystack\n %s" % (needle, haystack))
            reason = buf.getvalue()
            assert result, reason
    else:
        assert in_xml(needle, haystack), message


def eq_xml(xml1, xml2, reporter=None, wrapped=False):
    wrapper = lambda x: x.strip()
    if wrapped:
        wrapper = lambda x: "<wrap>" + x + "</wrap>"

    tree1 = _xml_from_string(wrapper(xml1))
    tree2 = _xml_from_string(wrapper(xml2))
    return c.xml_compare(tree1, tree2, reporter)


def in_xml(needle, haystack, reporter=None, wrapped=False):
    wrapper = lambda x: x.strip()
    if wrapped:
        wrapper = lambda x: "<wrap>" + x + "</wrap>"

    tree1 = _xml_from_string(wrapper(needle))
    tree2 = _xml_from_string(wrapper(haystack))
    return c.xml_contains(tree1, tree2, reporter)

