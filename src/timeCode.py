import math
# coding: utf-8

class _Fps (object):
    def __init__(self, num = 24000, den = 1000):
        self.num = num
        self.den = den
        self.fps = num/den

        frac = self.fps - int(self.fps)

        if frac == 0:
            self.NDF = True
        else:
            self.NDF = False



    def __str__(self):
        format_ = ("num: %s den: %s fps: %s NDF: %s")
        str_ = format_ % (str(self.num), str(self.den),str(self.fps),\
                str(self.NDF))

        return (str_)

class _Frames (object):

    def __init__(self, Fps, frames = 0):
        self.Fps = Fps
        self.fps = self.Fps.fps
        self.frames = frames

    def __str__(self):
        format_ = ("%s %s")
        str_ = format_ % (self.fps, self.frames)
        return (str_)


    def toTimeCode (self):
        hours = 0
        mins = 0
        scnds = 0
        
        seconds = self.frames / self.fps
        
        frs = seconds - int(seconds)

        print(self.fps)

        seconds = int(seconds)
        frames = math.floor(frs * self.fps)
        
        if seconds > 59:
            mins = seconds / 60
            scnds = int((mins - int(mins))*60)
        else:
            scnds = int(seconds)

        if mins > 59:
            hours = mins / 60
            mins = int((hours - int(hours))*60)
            hours = int(hours)
        else:
            mins = int(mins)


        format1 = ("%s:%s:%s:%s")

        str_ = format1 % (str(hours).zfill(2), str(mins).zfill(2),\
                str(scnds).zfill(2), str(frames).zfill(2))

        return (_TimeCode(self.Fps, str_))
 
class _TimeCode (object):

    def __init__(self, Fps, timeCode="00:00:00:00"):

        self.Fps = Fps
        self.fps = self.Fps.fps
        self.timeCode = timeCode

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

    def toList (self):
        list_ = {"HH": self.hour, "MM": self.min, "SS": self.second, "FF":\
                self.frame, "fps": self.fps.fps}
        return list_
    
    def toFrames (self):
        frames = 0
        seconds = self.hour * 3600 + self.min * 60 + self.second
        frames = math.ceil(seconds * self.fps + self.frame)

        return (_Frames(self.Fps, frames))
    

    def toCode (self):
        format_ = ("%s:%s:%s:%s")
        str_ = format_ % (str(self.hour).zfill(2), str(self.min).zfill(2),\
                str(self.second).zfill(2), str(self.frame).zfill(2))
        self.timeCode = (str_)
        

    def __str__(self):
        format_ = ("HH: %s MM: %s SS: %s FF : %s fps: %s")
        str_ = format_ % (self.hour, self.min, self.second, self.frame,\
                self.fps)
        return (str_)


def testTimeCode ():
    fps = _Fps(24000, 1001)
    tc1 = _TimeCode(fps, "01:32:00:23")
    frames = tc1.toFrames()
    print ("test ", frames)
    print ("test ", tc1)

    fr = _Frames(fps, frames.frames)

    print("test",fr)

    print("test", fr.toTimeCode())

   
def testFrames ():
    fps = _Fps (24000,  1001)
    fr = _Frames(fps, 240*6)
    print (fr.toTimeCode())

    print (fps)


if __name__ == "__main__":
    testFrames()
