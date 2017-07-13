
# coding: utf-8

import timeCode as tc


class EditDecisionLine (object):
    '''
    In each line, the edit number comes first, followed the source reel name, 
    the channel(s) to record, the transition (Cut, dissolve, etc), transition 
    duration (if applicable), Source IN time code, Source OUT, Record IN, Record OUT.
    
    1) Edit_     3 chars
    2) ReelName  4 chars
    3) Channel   4 chars
    4) Trans     4 chars
    5) Dur
    6) SourceIN   
    7) SourceOUT  
    8) RecordIN   
    9) RecordOUT
                             11:11:11:11
    111-222--3333--4444-555-666666666666-777777777777-888888888888-999999999999

    transitions:

    1) Cut
    2) Disolve
    3) Wipes

    
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
            
   
class MyApplication(object):
    def __init__(self, edLine):
        self.line = EditDecisionLine(edLine)
        
        
    def run (self):
        fps = tc._Fps()

        sourceIn = tc._TimeCode(fps, self.line.toList()["SourceIn"])
        sourceOut = tc._TimeCode(fps, self.line.toList()["SourceOut"])
        recordIn = tc._TimeCode(fps, self.line.toList()["RecordIn"])
        recordOut = tc._TimeCode(fps, self.line.toList()["RecordOut"])
        print ("Source In: ", sourceIn)
        print (sourceOut)
        print (recordIn)
        print (recordOut)
        
        frames = sourceIn.toFrames()
        
        print ("Source In Frames: ", frames)
        
    
def myApplication ():
    edLine = "001  Wildlife AA/V  C        01:02:08:24 01:02:11:24 00:00:01:12 00:00:04:12"
    app = MyApplication(edLine)
    app.run()

from edl import Event
    
class testEdl (object):

    def __init__(self):
        e = Event([])
        e.comments.append("* FROM CLIP NAME: Jellyfish.jpg")
        e.comments.append("* TO CLIP NAME: BL")
        e.num = "001"
        e.reel = "wildlife"
        e.src_start_tc = "01:02:08:23"
        e.src_end_tc = "01:02:11:23"
        e.rec_start_tc = "00:00:01:23"
        e.rec_end_tc = "00:00:04:23"
        e.tr_code = "C"
        e.track = "V"

        print (e.to_string())
 
if __name__ == "__main__":
    ma = testEdl()
