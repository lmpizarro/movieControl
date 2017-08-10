import xml.etree.ElementTree as etree
import xmltodict

class Ixml(object):
    def __init__(self, xmlFile):
        self.xmlFile = xmlFile
        self.tree = etree.parse(self.xmlFile)
        self.root = self.tree.getroot()

        self.toDict()


    def getProject(self):
        return self.dict_["BWFXML"]["PROJECT"]

    def getIxml_Version(self):
        return self.dict_["BWFXML"]["IXML_VERSION"]

    def getScene(self):
        return self.dict_["BWFXML"]["SCENE"]

    def getTake(self):
        return self.dict_["BWFXML"]["TAKE"]

    def getTape(self):
        return self.dict_["BWFXML"]["TAPE"]

    def getCircled(self):
        return self.dict_["BWFXML"]["CIRCLED"]

    def getNo_Good(self):
        return self.dict_["BWFXML"]["NO_GOOD"]

    def getFalse_Start(self):
        return self.dict_["BWFXML"]["FALSE_START"]

    def getWild_Track(self):
        return self.dict_["BWFXML"]["WILD_TRACK"]

    def getFile_Uid(self):
        return self.dict_["BWFXML"]["FILE_UID"]


    def to_dict(self):
        from json import loads, dumps
        return loads(dumps((xmltodict.parse(self.STR))))


    def toDict (self):

        dict_ = {}
        dict_[self.root.tag] = {}

        root = self.root

        for child in root:
            if len(child) > 0:
                dict_[root.tag][child.tag] = {} 

                if child.tag == "SPEED":
                    for c in child:
                        dict_[root.tag][child.tag][c.tag] = c.text 

                if child.tag == "BEXT":
                    for c in child:
                        dict_[root.tag][child.tag][c.tag] = c.text 

                if child.tag == "HISTORY":
                    for c in child:
                        dict_[root.tag][child.tag][c.tag] = c.text 

                if child.tag == "FILE_SET":
                    for c in child:
                        dict_[root.tag][child.tag][c.tag] = c.text 

                if child.tag == "TRACK_LIST":
                    dict_[root.tag][child.tag] = []
                    for c in child:
                        if len(c) > 0:
                            a = {}
                            for s in c:
                                a[s.tag] = s.text
                            dict_[root.tag][child.tag].append(a)

                if child.tag == "SYNC_POINT_LIST":
                    dict_[root.tag][child.tag] = []
                    for c in child:
                        if len(c) > 0:
                            a = {}
                            for s in c:
                                a[s.tag] = s.text
                            dict_[root.tag][child.tag].append(a)
    
            else:
               dict_[root.tag][child.tag] = child.text


        self.dict_ =  dict_ 
    
    def getDict(self):
        return self.dict_


if __name__ == "__main__":

    fileName = 'testixml.xml'
    ixml = Ixml (fileName)

    dict_ = ixml.getDict()

    print ("NO_GOOD: ", ixml.getNo_Good())
    print ("IXML_VERSION: ", ixml.getIxml_Version())
    print ("PROJECT: ", ixml.getProject())
    print ("SCENE: ", ixml.getScene())
    print ("TAKE: ", ixml.getTake())
    print ("TAPE: ",  ixml.getTape())
    print ("CIRCLED: ", ixml.getCircled())
    print ("NO_GOOD: ", ixml.getNo_Good())
    print ("FALSE_START: ", ixml.getFalse_Start())
    print ("WILD_TRACK: ", ixml.getWild_Track())
    print ("FILE_UID: ", ixml.getFile_Uid())

    for k in dict_["BWFXML"]["SPEED"]:
        print ("SPEED ", k, " " , dict_["BWFXML"]["SPEED"][k])

