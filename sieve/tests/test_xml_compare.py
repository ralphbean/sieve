import sieve.xml_compare as c

def test_basic():
    xml1 = """    <?xml version='1.0' encoding='utf-8' standalone='yes'?>
        <Stats start="1275955200" end="1276041599"></Stats>"""
    xml2 = """     <?xml version='1.0' encoding='utf-8' standalone='yes'?>
        <Stats start="1275955200" end="1276041599"></Stats>"""
    xml3 = """ <?xml version='1.0' encoding='utf-8' standalone='yes'?>
        <Stats start="1275955200"></Stats>"""

    from lxml import etree
    tree1 = etree.fromstring(xml1.strip())
    tree2 = etree.fromstring(xml2.strip())
    tree3 = etree.fromstring(xml3.strip())

    import sys
    reporter = lambda x: sys.stdout.write(x + "\n")

    assert c.xml_compare(tree1,tree2,reporter)
    assert c.xml_compare(tree1,tree3,reporter) is False
