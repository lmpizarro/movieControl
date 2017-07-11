

# coding: utf-8

'''
    1) dateTime
    2) scene
    3) shot
    4) take
    5) source

    #my_date = datetime.strptime(e["dateTime"], '%b %d %Y %I:%M%p')
    https://stackoverflow.com/questions/466345/converting-string-into-datetime
'''
take1 = {"dateTime":"Jun 1 2005 1:33PM", "scene": 1, "shot": 1, "take": 1,
"source": "00001.MTS"}
take2 = {"dateTime":"Jun 1 2005 2:33PM", "scene": 1, "shot": 1, "take": 2,
"source": "00002.MTS"}
take3 = {"dateTime":"Jun 1 2005 3:33PM", "scene": 1, "shot": 1, "take": 3,
"source": "00003.MTS"}
take4 = {"dateTime":"Jun 1 2005 4:33PM", "scene": 1, "shot": 2, "take": 1,
"source": "00004.MTS"}
take5 = {"dateTime":"Jun 1 2005 5:33PM", "scene": 1, "shot": 2, "take": 2,
"source": "00005.MTS"}
take6 = {"dateTime":"Jun 1 2005 6:33PM", "scene": 1, "shot": 2, "take": 3,
"source": "00006.MTS"}
take7 = {"dateTime":"Jun 1 2005 8:33PM", "scene": 1, "shot": 2, "take": 4,
"source": "00007.MTS"}


class Take(object):
    def __init__(self, take):
        self.take = take

    def __str__(self):
        format_1 = ("scene: %s shot: %s take: %s source: %s")
        format_2 = (" date time: %s \n")
        str_1 = \
        format_1%(self.take["scene"], self.take["shot"], self.take["take"], self.take["source"])
        str_2 = format_2 % (self.take["dateTime"])
        return (str_1 + str_2)

def takeTest():
    take = Take(take1)
    print (take)

    take = Take(take2)
    print (take)

class dbTakes (object):
    def __init__(self):
        self.db = []
        
    def insert(self, tk):
        self.db.append(tk)



'''
    1) dateTime
    2) scene
    3) shot
    4) take
    5) source
'''
def dbTakeTest():
    dbT = dbTakes()

    take = Take(take1)

    dbT.insert(take)

    take = Take(take2)
    dbT.insert(take)
    take = Take(take3)
    dbT.insert(take)
    take = Take(take4)
    dbT.insert(take)
    take = Take(take5)
    dbT.insert(take)
    take = Take(take6)
    dbT.insert(take)
    take = Take(take7)
    dbT.insert(take)

    for e in dbT.db:
        print (e)



if __name__ == "__main__":
    takeTest()
    dbTakeTest()
