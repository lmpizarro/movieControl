import xml.etree.ElementTree as etree
import xmltodict

class Ixml(object):

    def __init__(self, xmlFile):
        self.xmlFile = xmlFile
        self.tree = etree.parse(self.xmlFile)
        self.root = self.tree.getroot()
        self.sng = "\n   "

        self.toDict()

        self.keys = []
        if "BWFXML" in self.dict_.keys(): 
            self.keys = self.dict_["BWFXML"].keys()

    def getLevel0(self, key):
        if key in self.keys:
            str_ = self.sng 
            str_ += self.dict_["BWFXML"][key] + self.sng
        return str_

    def getProject(self):
        return self.getLevel0("PROJECT")

    def getUbits(self):
        return self.getLevel0("UBITS")

    def getUser(self):
        return self.getLevel0("USER")


    def getIxml_Version(self):
        return self.getLevel0("IXML_VERSION")

    def getScene(self):
        return self.getLevel0("SCENE")

    def getTake(self):
        return self.getLevel0("TAKE")

    def getTape(self):
        return self.getLevel0("TAPE")

    def getCircled(self):
        return self.getLevel0("CIRCLED")

    def getNo_Good(self):
        return self.getLevel0("NO_GOOD")

    def getFalse_Start(self):
        return self.getLevel0("FALSE_START")

    def getWild_Track(self):
        return self.getLevel0("WILD_TRACK")

    def getFile_Uid(self):
        return self.getLevel0("FILE_UID")

    def getNote(self):
        return self.getLevel0("NOTE")

    def getLevel1(self, key):
        if key in self.keys:
            list_ = self.dict_["BWFXML"][key]

            str_ = self.sng 
            for k in list_.keys():
                str_ = str_ + ("%s: %s  %s")%(k, list_[k], self.sng)

        return str_

    def getSpeed(self):
        return self.getLevel1("SPEED")

    def getBext(self):
        return self.getLevel1("BEXT")

    def getHistory(self):
        return self.getLevel1("HISTORY")

    def getFile_Set(self):
        return self.getLevel1("FILE_SET")

    def getLevel2(self, key):
        if key in self.keys:
            list_ = self.dict_["BWFXML"][key]

            str_ = self.sng 
            for l in list_:
                sr = ""
                ks = l.keys()
                for k in  ks:
                    sr = sr + ("%s: %s ")%(k, l[k])
                str_ = str_ +  sr + self.sng 
            return str_ 


    def getTrack_List(self):
        return self.getLevel2("TRACK_LIST")

    def getSync_Point_List(self):
        return self.getLevel2("SYNC_POINT_LIST")

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

    def __str__(self):

        dict_ = self.getDict()

        str_ = ""

        functionList = {'IXML_VERSION': self.getIxml_Version, "PROJECT": self.getProject, \
            'SCENE': self.getScene, 'TAKE': self.getTake , 'TAPE': self.getTape, \
            'CIRCLED': self.getCircled, 'NO_GOOD': self.getNo_Good, \
            'FALSE_START': self.getFalse_Start, 'WILD_TRACK': self.getWild_Track, \
            'FILE_UID': self.getFile_Uid, 'UBITS': self.getUbits, \
            'SYNC_POINT_LIST': self.getSync_Point_List, 'NOTE': self.getNote, \
            'HISTORY': self.getHistory, 'FILE_SET' :self.getFile_Set, \
            'TRACK_LIST': self.getTrack_List, 'SPEED': self.getSpeed, \
            'BEXT: ': self.getBext, 'USER': self.getUser }

        str_ = ""

        for k in functionList.keys():
            str_ = str_ +  ("%s: %s \n")%(k, functionList[k]())

        return  (str_)



if __name__ == "__main__":
    fileName = 'testixml.xml'
    ixml = Ixml (fileName)

    dict_ = ixml.getDict()

    print(ixml)


