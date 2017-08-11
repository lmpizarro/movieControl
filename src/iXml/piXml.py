import xml.etree.ElementTree as etree
import xmltodict

class Ixml(object):
    def __init__(self, xmlFile):
        self.xmlFile = xmlFile
        self.tree = etree.parse(self.xmlFile)
        self.root = self.tree.getroot()

        self.toDict()

        self.keys = []
        if "BWFXML" in self.dict_.keys(): 
            self.keys = self.dict_["BWFXML"].keys()
            

    def getProject(self):
        if "PROJECT" in self.keys:
            return self.dict_["BWFXML"]["PROJECT"]

    def getIxml_Version(self):
        if "IXML_VERSION" in self.keys:
            return self.dict_["BWFXML"]["IXML_VERSION"]

    def getScene(self):
        if "SCENE" in self.keys:
            return self.dict_["BWFXML"]["SCENE"]

    def getTake(self):
        if "TAKE" in self.keys:
            return self.dict_["BWFXML"]["TAKE"]

    def getTape(self):
        if "TAPE" in self.keys:
            return self.dict_["BWFXML"]["TAPE"]

    def getCircled(self):
        if "CIRCLED" in self.keys:
            return self.dict_["BWFXML"]["CIRCLED"]

    def getNo_Good(self):
        if "NO_GOOD" in self.keys:
            return self.dict_["BWFXML"]["NO_GOOD"]

    def getFalse_Start(self):
        if "FALSE_START" in self.keys:
            return self.dict_["BWFXML"]["FALSE_START"]

    def getWild_Track(self):
        if "FALSE_START" in self.keys:
            return self.dict_["BWFXML"]["FALSE_START"]

    def getFile_Uid(self):
        if "FALSE_START" in self.keys:
            return self.dict_["BWFXML"]["FILE_UID"]

    def getNote(self):
        if "NOTE" in self.keys:
            return self.dict_["BWFXML"]["NOTE"]

    def getTrack_List(self):
        sng = "\n   "
        if "TRACK_LIST" in self.keys:
            list_ = self.dict_["BWFXML"]["TRACK_LIST"]

            str_ = sng 
            for l in list_:
                sr = ""
                ks = l.keys()
                for k in  ks:
                    sr = sr + ("%s: %s ")%(k, l[k])
                str_ = str_ +  sr + sng 
            return str_ 



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

    fileName = 'testixmlC.xml'
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
    print ("NOTE: ", ixml.getNote())
    print ("TRACK_LIST: ", ixml.getTrack_List())

    if "SPEED" in ixml.keys:
        for k in dict_["BWFXML"]["SPEED"]:
            print ("SPEED ", k, " " , dict_["BWFXML"]["SPEED"][k])

