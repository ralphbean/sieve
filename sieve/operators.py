from lxml import etree
import sieve.xml_compare as c
import sys


def assert_eq_xml(xml1, xml2, msg=None, wrapped=False):
    if not message:
        buf = StringIO.StringIO()
        reporter = lambda x: buf.write(x + '\n')
        result = eq_xml(xml1, xml2)
        if not result:
            reason = buf.getvalue()
            assert result, reason
    else:
        assert eq_xml(xml1, xml2), msg


def eq_xml(xml1, xml2, reporter=None, wrapped=False):
    wrapper = lambda x: x.strip()
    if wrapped:
        wrapper = lambda x: "<wrap>" + x + "</wrap>"

    tree1 = etree.fromstring(wrapper(xml1))
    tree2 = etree.fromstring(wrapper(xml2))
    return c.xml_compare(tree1, tree2, reporter)
