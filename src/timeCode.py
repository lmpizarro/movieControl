import math
# coding: utf-8

class TimeCode (object):

    def __init__(self, fps, timeCode="00:00:00:00"):

        self.timeCode = timeCode
        self.fps = fps

        fields = self.timeCode.split(":")

        if len(fields) == 4:
            self.hour = int(fields[0])
            if self.hour > 23:
                print ("Error")

            self.min = int(fields[1])
            if self.min > 59:
                print ("Error")

            self.second = int(fields[2])
            if self.second > 59:
                print ("Error")

            self.frame = int(fields[3])
            if self.frame > self.fps:
                print ("Error")


        self.fps = fps

    def toList (self):
        list_ = {"HH": self.hour, "MM": self.min, "SS": self.second, "FF":\
                self.frame, "fps": self.fps}
        return list_
    
    def toFrames (self):
        frames = 0
        seconds = self.hour * 3600 + self.min * 60 + self.second
        frames = math.ceil(seconds * self.fps + self.frame)
        return (frames)
    
    def toTimeCode (self, frames):
        self.hour = 0
        self.min = 0
        self.second = 0
        self.frame = 0

        hours = 0
        mins = 0
        scnds = 0
        
        seconds = frames / self.fps
        
        frs = seconds - int(seconds)
        
        seconds = int(seconds)
        frames = math.floor(frs * self.fps)
        
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
        format_ = ("HH: %s MM: %s SS: %s FF : %s fps: %s")
        str_ = format_ % (self.hour, self.min, self.second, self.frame, self.fps)
        return (str_)


def testTimeCode ():
    fps = 24000/1001
    tc1 = TimeCode(fps, "01:01:32:23")
    frames = tc1.toFrames()
    print (tc1)
    print (frames)
    
    tc1.toTimeCode(frames)

    print (tc1)

    print(tc1.timeCode)


if __name__ == "__main__":
    testTimeCode()
