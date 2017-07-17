import os
import subprocess
from glob import glob

from xml.dom import minidom

from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment

'''
https://docs.python.org/2/library/xml.dom.minidom.html
'''

def getText(nodelist):
    rc = []
    for node in nodelist:
       if node.nodeType == node.TEXT_NODE:
          rc.append(node.data)
    return ''.join(rc)

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    reparsed = reparsed.toprettyxml(indent="  ")
    '''
       https://stackoverflow.com/questions/1662351/problem-with-the-new-lines-when-i-use-toprettyxml
    '''
    reparsed = os.linesep.join([s for s in reparsed.splitlines() if s.strip()])
    return reparsed


def gen_out_core_xml(dir_):

    files = dir_ + "/" + "*.wav"

    result = [y for x in os.walk(dir_) for y in glob(os.path.join(x[0],\
        '*.wav'))]

    for e in result:
        p = subprocess.Popen (['bwfmetaedit', "--out-core-xml", e], stdout=subprocess.PIPE)
        d, err = p.communicate()

    result = [y for x in os.walk(dir_) for y in glob(os.path.join(x[0],\
        '*.xml'))]

    return result

'''
       https://stackoverflow.com/questions/27294416/is-there-any-way-to-change-the-element-node-name-in-minidom-python
'''

nodes4HN = \
    {"Originator" : "BWF_ORIGINATOR", "OriginationDate" : "BWF_ORIGINATION_DATE",\
     "OriginationTime" : "BWF_ORIGINATION_TIME", \
     "TimeReference_translated": "BWF_TIME_REFERENCE_TRANSLATED",\
     "TimeReference" : "BWF_TIME_REFERENCE", "BextVersion":"BWF_VERSION",\
     "CodingHistory":"BWF_CODING_HISTORY", "Core" : "BEXT" }

bexts = []

def change_node_names(r):
    '''
    change element node name
    '''
    xmldoc = minidom.parse(r)
    root = ET.fromstring(xmldoc.toxml())
    for k in nodes4HN.keys():
        core = root.find('.//' + k)
        core.tag = nodes4HN[k] 

    bext =  root.find('.//BEXT')

    return (bext)

'''
https://pymotw.com/2/xml/etree/ElementTree/create.html
'''
dataiXML = {"Project": "AnewMovie", "Scene": 21, "Take": 21, \
        "Tape": 10, "Circled" : True}

def geniXML(dataiXML, b):

        top = Element('BWFXML')

        comment = Comment('Generated for PyMOTW')
        top.append(comment)
        child = SubElement(top, 'IXML_VERSION')
        child.text = '1.52'

        child = SubElement(top, 'PROJECT')
        child.text =dataiXML["Project"] 

        child = SubElement(top, 'SCENE')
        child.text = str(dataiXML["Scene"])

        child = SubElement(top, 'TAKE')
        child.text = str(dataiXML["Take"])

        child = SubElement(top, 'TAPE')
        child.text = str(dataiXML["Tape"])

        child = SubElement(top, 'Circled')
        child.text = str(dataiXML["Circled"])


        top.append(b)

        return top

'''
http://lxml.de/
'''
def parse_with_ltree(result):
    for r in result:
        root = etree.parse(r)
        p = etree.tostring(root, pretty_print=True )
        print (root.get("Core"))
        print(p)


def test_with_ltree():
    dir_ = '../media'
    result = gen_out_core_xml(dir_)
    parse_with_ltree(result)


def print_tops(e):
        xml_string = prettify (e)
        print (xml_string)

def test_with_dom():
    dir_ = '../media'
    result = gen_out_core_xml(dir_)
    for r in result:
        b = change_node_names(r)
        bexts.append(b)

    for i,b  in enumerate(bexts):
        bexts[i] = geniXML(dataiXML, b)

    for e in bexts:
        print_tops(e)

if __name__ == "__main__":
    test_with_dom()

