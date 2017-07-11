# coding: utf-8

sources = {
"source1" : {"name": "00001.MTS", "props": {"fps": 23.976, "frames": 1000}},
"source2" : {"name": "00002.MTS", "props": { "fps": 23.976, "frames": 1500}},
"source3" : {"name": "00003.MTS", "props": { "fps": 23.976, "frames": 2000}},
"source4" : {"name": "00004.MTS", "props": { "fps": 23.976, "frames": 5000}},
"source5" : {"name": "00005.MTS", "props": { "fps": 23.976, "frames": 4300}},
"source6" : {"name": "00006.MTS", "props": { "fps": 23.976, "frames": 7000}},
"source7" : {"name": "00007.MTS", "props": { "fps": 23.976, "frames": 8000}},
}

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


def testSource ():
    srcs = []
    for i in range(1,8):
        name = "source" + str(i)
        srcs.append(Source(sources[name]))

    for i in range(len(srcs)):
        print (srcs[i])

    for i in range(len(srcs)):
        print (srcs[i].getDuration())



if __name__ == "__main__":

    testSource()
