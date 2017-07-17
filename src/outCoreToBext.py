'''
<?xml version="1.0" encoding="UTF-8"?>
<BWFXML>
    <BEXT>
        <BWF_DESCRIPTION>all the old stuff</BWF_DESCRIPTION>
        <BWF_ORIGINATOR>METACORDER</BWF_ORIGINATOR>               !!!
        <BWF_ORIGINATOR_REFERENCE>123456</BWF_ORIGINATOR_REFERENCE> 
        <BWF_ORIGINATION_DATE>2003-10-30</BWF_ORIGINATION_DATE>   !!!
        <BWF_ORIGINATION_TIME>03:27:17</BWF_ORIGINATION_TIME>     !!!
        <BWF_TIME_REFERENCE_LOW>123674376</BWF_TIME_REFERENCE_LOW>
        <BWF_TIME_REFERENCE_HIGH>0</BWF_TIME_REFERENCE_HIGH>      !!!
        <BWF_VERSION>1.0</BWF_VERSION>                            !!!
        <BWF_UMID>MTIPMX17654200508051445053840001</BWF_UMID>
        <BWF_RESERVED>00000000000000000000000000000000000000000</BWF_RESERVED>
        <BWF_CODING_HISTORY>some info</BWF_CODING_HISTORY>        !!!
    </BEXT>
</BWFXML>

<?xml version="1.0" encoding="UTF-8"?>
<conformance_point_document>
     <File name="../media/4CH000I-PatioChorroAgua.wav">
      <Core>
       <Originator>ZOOM Handy Recorder H4n</Originator>  
       <OriginationDate>2017-01-23</OriginationDate>
       <OriginationTime>14:23:36</OriginationTime>
       <TimeReference_translated>14:23:36.000</TimeReference_translated>
       <TimeReference>2285085600</TimeReference>
       <BextVersion>0</BextVersion>
       <CodingHistory>A=PCM,F=44100,W=24,M=stereo,T=ZOOM Handy Recorder H4n</CodingHistory>
      </Core>
   </File>
</conformance_point_document>
'''

import os
from glob import glob
import subprocess
from xml.dom import minidom

'''
https://docs.python.org/2/library/xml.dom.minidom.html
'''
def getText(nodelist):
    rc = []
    for node in nodelist:
       if node.nodeType == node.TEXT_NODE:
          rc.append(node.data)
    return ''.join(rc)

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


from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment

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



'''
       https://stackoverflow.com/questions/27294416/is-there-any-way-to-change-the-element-node-name-in-minidom-python
'''
nodes = \
    {"Originator" : "BWF_ORIGINATOR", "OriginationDate" : "BWF_ORIGINATION_DATE",\
     "OriginationTime" : "BWF_ORIGINATION_TIME", \
     "TimeReference_translated": "BWF_TIME_REFERENCE_TRANSLATED",\
     "TimeReference" : "BWF_TIME_REFERENCE", "BextVersion":"BWF_VERSION",\
     "CodingHistory":"BWF_CODING_HISTORY", "Core" : "BEXT" }


bexts = []
def change_node_names(result):
    '''
    change element node name
    '''
    for r in result:
        xmldoc = minidom.parse(r)
        root = ET.fromstring(xmldoc.toxml())
        for k in nodes.keys():
            core = root.find('.//' + k)
            core.tag = nodes[k] 

        bext =  root.find('.//BEXT')

        bexts.append(bext)

'''
https://pymotw.com/2/xml/etree/ElementTree/create.html
'''
def geniXML():
    top = Element('BWFXML')

    comment = Comment('Generated for PyMOTW')
    top.append(comment)
    child = SubElement(top, 'IXML_VERSION')
    child.text = '1.52'

    top.append(bexts[0])

    print (prettify(top))



def print_bexts():
    for e in bexts:
        xml_string = ET.tostring(e)
        print (xml_string)
        print()    

from io import StringIO, BytesIO
from lxml import etree

'''
http://lxml.de/
'''
def parse_with_ltree(result):
    for r in result:
        root = etree.parse(r)
        p = etree.tostring(root, pretty_print=True )
        print (root.get("Core"))
        print(p)

def test_with_dom():
    dir_ = '../media'
    result = gen_out_core_xml(dir_)
    change_node_names(result)
    #print_bexts()
    geniXML()

def test_with_ltree():
    dir_ = '../media'
    result = gen_out_core_xml(dir_)
    parse_with_ltree(result)


if __name__ == "__main__":
    test_with_dom()

