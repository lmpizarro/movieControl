
# coding: utf-8

take1 = {"dateTime":"Jun 1 2005 1:33PM", "scene": 1, "shot": 1, "take": 1}
take2 = {"dateTime":"Jun 1 2005 2:33PM", "scene": 1, "shot": 1, "take": 2}
take3 = {"dateTime":"Jun 1 2005 3:33PM", "scene": 1, "shot": 1, "take": 3}
take4 = {"dateTime":"Jun 1 2005 4:33PM", "scene": 1, "shot": 2, "take": 1}
take5 = {"dateTime":"Jun 1 2005 5:33PM", "scene": 1, "shot": 2, "take": 2}
take6 = {"dateTime":"Jun 1 2005 6:33PM", "scene": 1, "shot": 2, "take": 3}
take7 = {"dateTime":"Jun 1 2005 8:33PM", "scene": 1, "shot": 2, "take": 4}


class dbTakes (object):
    def __init__(self):
        self.db = []
        

    def insert(self, take):
        self.db.append(take)



import math
from  datetime import datetime

class TimeCode (object):
    def __init__(self, timeCode):
        self.timeCode = timeCode
        self.fields = self.timeCode.split(":")
        if len(self.fields) == 4:
            self.hour = int(self.fields[0])
            self.min = int(self.fields[1])
            self.second = int(self.fields[2])
            self.frame = int(self.fields[3])
    
    def __str__(self):
        format_ = ("HH: %s MM: %s SS: %s FF : %s")
        str_ = format_ % (self.hour, self.min, self.second, self.frame)
        return str_

    def toList (self):
        list_ = {"HH": self.hour, "MM": self.min, "SS": self.second, "FF": self.frame}
        return list_
    
    def toFrames (self, fps):
        frames = 0
        seconds = self.hour * 3600 + self.min * 60 + self.second
        frames = math.ceil(seconds * fps + self.frame)
        return (frames)
    
    def toTimeCode (self, frames, fps):
        self.hour = 0
        self.min = 0
        self.second = 0
        self.frame = 0
        
        seconds = frames / fps
        
        frs = seconds - int(seconds)
        
        seconds = int(seconds)
        frames = math.floor(frs * fps)
        
        if seconds > 3600:
            hours = math.floor(seconds/3600)
            mins = (seconds/3600 - hours) * 60
            
            scnds = (mins - math.floor(mins)) * 60
        
        self.hour = hours
        self.min = math.floor(mins)
        self.second = math.floor(scnds)
        self.frame = frames
        
        print (self)

class EditDecisionLine (object):
    '''
    In each line, the edit number comes first, followed the source reel name, 
    the channel(s) to record, the transition (Cut, dissolve, etc), transition 
    duration (if applicable), Source IN time code, Source OUT, Record IN, Record OUT.
    
    1) Edit_ 
    2) ReelName  
    3) Channel
    4) Trans
    5) Dur
    6) SourceIN   
    7) SourceOUT  
    8) RecordIN   
    9) RecordOUT
    
    '''
    def __init__(self, line):
        self.line = line
        fields = self.line.split()
        self.lenLine = len(fields)
        
        if self.lenLine >= 8:
            self.recordOut = fields[self.lenLine - 1]
            self.recordIn = fields[self.lenLine - 2]
            self.sourceOut = fields[self.lenLine - 3]
            self.sourceIn = fields[self.lenLine - 4]
            
            if self.lenLine == 9:
                self.dur = self.SourceIn = fields[self.lenLine - 5]
            else:
                self.dur = self.SourceIn = ""
                
                
            self.edit_ = fields[0]
            self.reelName = fields[1]
            self.channel = fields[2]
            self.trans =  fields[3]
            
    def __str__ (self):
        format1 = (" Edit: %s Reel Name: %s \n Channel: %s \n Trans: %s \n Dur: %s \n")
        format2 = (" SourceIn: %s \n SourceOut: %s \n RecordIn: %s \n RecordOut: %s \n")
        str_1 = format1%(self.edit_, self.reelName, self.channel, self.trans, self.dur)
        str_2 = format2%(self.sourceIn, self.sourceOut, self.recordIn, self.recordOut)
        return str_1 + str_2
    
    def toList (self):
        list_ = {"Edit": self.edit_, 
                 "ReelName": self.reelName,
                 "Channel": self.channel, 
                 "Trans": self.trans,
                 "Dur":  self.dur,
                 "SourceIn": self.sourceIn,  
                 "SourceOut": self.sourceOut,  
                 "RecordIn": self.recordIn, 
                 "RecordOut": self.recordOut} 
        
        return list_
            
    
class Project(object):
    def __init__(self):
        pass
    
    def addTake (self):
        pass

class MyApplication(object):
    def __init__(self, edLine):
        self.prj = EditDecisionLine(edLine)
        
        
    def run (self):
        print (self.prj)
        sourceIn = TimeCode(self.prj.toList()["SourceIn"])
        sourceOut = TimeCode(self.prj.toList()["SourceOut"])
        recordIn = TimeCode(self.prj.toList()["RecordIn"])
        recordOut = TimeCode(self.prj.toList()["RecordOut"])
        print ("Source In: ", sourceIn)
        print (sourceOut)
        print (recordIn)
        print (recordOut)
        
        fps = 25
        frames = sourceIn.toFrames(fps)
        
        print ("Source In Frames: ", frames)
        
        sourceIn.toTimeCode(frames, fps)
        
'''
https://stackoverflow.com/questions/466345/converting-string-into-datetime
'''
def dbTakeTest():
    dbT = dbTakes()

    dbT.insert(take1)
    dbT.insert(take2)
    dbT.insert(take3)
    dbT.insert(take4)
    dbT.insert(take5)
    dbT.insert(take6)
    dbT.insert(take7)

    for e in dbT.db:
        my_date = datetime.strptime(e["dateTime"], '%b %d %Y %I:%M%p')
        print (my_date)


if __name__ == "__main__":
    edLine = "001  Wildlife AA/V  C        01:02:08:24 01:02:11:24 00:00:01:12 00:00:04:12"
    app = MyApplication(edLine)
    app.run()
    dbTakeTest()


