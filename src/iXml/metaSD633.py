esquel = {"BWFXML":
             {"PROJECT":"", "ROLL":"", "SCENE":"", "TAKE":"", "CIRCLED":"",
              "NOTES":"", "FILE_UID":"", 
              "SPEED":{"FILE_SAMPLE_RATE":""}}
             
             }


as_user_guide = {"PROJECT":"", "ROLL":"", "SCENE":"", "TAKE":"", "CIRCLED":"", \
                 "NOTES":"", "FILE_UID":"", "FILE_SAMPLE_RATE":"", \
                 "DIGITIZER_SAMPLE_RATE":"", "AUDIO_BITH_DEPTH":"", \
                 "TRACK_COUNT":"", "MASTER_SPEED":""}

class Sd633(object):
    def __init__(self):
        pass

import random
import datetime

class DeltaGen(object):
    def __init__(self, seconds_acum=0):
        self.seconds_acum = seconds_acum 

    def getNew(self):     
        self.seconds_acum += random.randint(45, 120)*60 + random.randint(0,59)

        return (self.seconds_acum)


class TimesCreation(object):

    def __init__(self, creation_date_base, creation_time_base, SR=48000):

        self.SR = SR
        self.deltaGen = DeltaGen()

        date_time = creation_date_base + " " + creation_time_base
        self.datetime_object = datetime.datetime.strptime (date_time, '%Y-%m-%d %H:%M:%S')
        '''
        Start Time Code 
        Stored as a sample count since midnight
        '''


    def times_defs(self, seconds_acum):
        tnit = self.datetime_object + datetime.timedelta(seconds=seconds_acum)
        tdur = random.randint(1, 5) * 60

        STC = tnit.time().second + tnit.hour * 3600 + tnit.minute * 60
        STC *= self.SR


        return {"CREATION_TIME": tnit.time(), "CREATION_DATE": tnit.date(), \
                "DURATION":tdur, "START_TIME_CODE":STC}


    def getTimes(self, N=8):
        num = 0
        while num <  N:

            yield (self.times_defs(self.deltaGen.getNew()))
            num +=1 


if __name__ == "__main__":
    '''
    2003-10-30 03:27:17
    '''
    creation_date_base = "2003-10-30"
    creation_time_base = "08:00:00"


    s = Sd633()
    tCrea = TimesCreation(creation_date_base, creation_time_base)

    times = tCrea.getTimes(2)
        
    for tt in times:
        print (tt["CREATION_DATE"], tt["CREATION_TIME"], tt["DURATION"],
                tt["START_TIME_CODE"])

