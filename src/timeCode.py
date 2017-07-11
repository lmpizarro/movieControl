import math
# coding: utf-8

class TimeCode (object):

    def __init__(self, timeCode):
        self.timeCode = timeCode
        self.toNums()

   
    def toNums (self):
        self.fields = self.timeCode.split(":")
        if len(self.fields) == 4:
            self.hour = int(self.fields[0])
            if self.hour > 23:
                print ("Error")

            self.min = int(self.fields[1])
            if self.min > 59:
                print ("Error")

            self.second = int(self.fields[2])
            if self.second > 59:
                print ("Error")

            self.frame = int(self.fields[3])

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

    def toCode (self):
        format_ = ("%s:%s:%s:%s")
        str_ = format_ % (str(self.hour).zfill(2), str(self.min).zfill(2),\
                str(self.second).zfill(2), str(self.frame).zfill(2))
        self.timeCode = (str_)
        

    def __str__(self):
        format_ = ("HH: %s MM: %s SS: %s FF : %s")
        str_ = format_ % (self.hour, self.min, self.second, self.frame)
        return (str_)


def testTimeCode ():
    fps = 24
    tc1 = TimeCode("01:01:32:23")
    frames = tc1.toFrames(fps)
    print (tc1)
    print (frames)
    
    tc1.toTimeCode(frames, fps)

    print (tc1)

    print(tc1.timeCode)


if __name__ == "__main__":
    testTimeCode()
