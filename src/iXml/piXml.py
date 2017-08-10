import xml.etree.ElementTree as etree
import xmltodict


class Ixml(object):
    def __init__(self, xmlFile):
        self.xmlFile = xmlFile
        self.tree = etree.parse(self.xmlFile)
        self.root = self.tree.getroot()

        self.setProject()
        self.setIxml_Version()
        self.setScene()
        self.setTake()
        self.setTape()
        self.setCircled()
        self.setNo_Good()
        self.setFalse_Start()
        self.setWild_Track()
        self.STR = etree.tostring(self.root)

    def setProject(self):
        self.PROJECT = self.root.findall("PROJECT")[0].text

    def setIxml_Version(self):
        self.IXML_VERSION = self.root.findall("IXML_VERSION")[0].text

    def setScene(self):
        self.SCENE = self.root.findall("SCENE")[0].text

    def setTake(self):
        self.TAKE = self.root.findall("TAKE")[0].text


    def setTape(self):
        self.TAPE = self.root.findall("TAPE")[0].text

    def setCircled(self):
        self.CIRCLED = self.root.findall("CIRCLED")[0].text


    def setNo_Good(self):
        self.NO_GOOD = self.root.findall("NO_GOOD")[0].text

    def setFalse_Start(self):
        self.FALSE_START = self.root.findall("FALSE_START")[0].text

    def setWild_Track(self):
        self.WILD_TRACK = self.root.findall("WILD_TRACK")[0].text

    def to_dict(self):
        from json import loads, dumps
        return loads(dumps((xmltodict.parse(self.STR))))


    def getDict (self):
        dict_ = {}

        dict_["PROJECT"] = self.PROJECT
        dict_["IXML_VERSION"] = self.IXML_VERSION
        dict_["SCENE"] = self.SCENE
        dict_["TAKE"] = self.TAKE
        dict_["TAPE"] = self.TAPE
        dict_["CIRCLED"] = self.CIRCLED
        dict_["NO_GOOD"] = self.NO_GOOD
        dict_["FALSE_START"] = self.FALSE_START
        dict_["WILD_TRACK"] = self.WILD_TRACK

        return dict_


if __name__ == "__main__":

    fileName = 'testixml.xml'
    ixml = Ixml (fileName)

    #print ( ixml.to_dict())

    print (ixml.getDict())


    tree = etree.parse(fileName )
    root = tree.getroot()

    print (len(root))

    print ("..", root.tag)

    dict_ = {}
    dict_[root.tag] = {}


    for child in root:
        if len(child) > 0:
            for c in child:
                print(child.tag, c.tag, len(c))
        else:
           dict_[root.tag][child.tag] = child.text
           print(root.tag, child.tag, child.text)


    IXML_VERSION = root.findall("IXML_VERSION")[0].text
    PROJECT = root.findall("PROJECT")[0].text
    SCENE = root.findall("SCENE")[0].text

    print("PROJECT", PROJECT)
    print("IXML_VERSION", IXML_VERSION)
    print("SCENE", SCENE)


    print (dict_)

