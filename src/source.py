# coding: utf-8

sources = {
"source1" : {"name": "00001.MTS", "props": { "num": 24000, "den": 1001, "frames": 1000}},
"source2" : {"name": "00002.MTS", "props": { "num": 24000, "den": 1001,  "frames": 1500}},
"source3" : {"name": "00003.MTS", "props": { "num": 24000, "den": 1001, "frames": 2000}},
"source4" : {"name": "00004.MTS", "props": { "num": 24000, "den": 1001, "frames": 5000}},
"source5" : {"name": "00005.MTS", "props": { "num": 24000, "den": 1001, "frames": 4300}},
"source6" : {"name": "00006.MTS", "props": { "num": 24000, "den": 1001, "frames": 7000}},
"source7" : {"name": "00007.MTS", "props": { "num": 24000, "den": 1001, "frames": 8000}},
}

import timeCode as tc

class Source (object):
    def __init__(self, s):
        self.source = s

    def __str__(self):
        format_ = ("name: %s fps: %f frames: %d")
        str_ = format_ % (self.source["name"], self.source["props"]["fps"],\
                self.source["props"]["frames"])
        return str_


    def getDuration (self):
        return (self.source["props"]["frames"] / self.source["props"]["fps"]) 


def testSource1 ():
    srcs = []
    for i in range(1,8):
        name = "source" + str(i)
        srcs.append(Source(sources[name]))

    for i in range(len(srcs)):
        print (srcs[i])

    for i in range(len(srcs)):
        print (srcs[i].getDuration())


def testSource():
    src = sources["source7"]
    num = src["props"]["num"]
    den = src["props"]["den"]

    fps = tc._Fps(num=num, den=den)

    frs = tc._Frames(fps, src["props"]["frames"])

    print (frs)

    print(frs.toTimeCode())

if __name__ == "__main__":
    testSource()
