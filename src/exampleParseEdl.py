from edl import Parser

'''
   https://github.com/simonh10/python-edl
'''
parser = Parser('23.98')

format1 = ("Source File: %s Clip Name: %s \n")
format2 = ("src start tc: %s src end tc: %s rec start tc: %s rec end tc: %s \n")
format3 = ("event: %s reel: %s track: %s tr_code: %s\n")

with open('test_2398.edl') as f:
     edl = parser.parse(f)

     for event in edl.events:

        str_ = format3%(str(event.num), str(event.reel), str(event.track), str(event.tr_code))
        print (str_)

        str_ = format2%(str(event.src_start_tc), str(event.src_end_tc), \
                str(event.rec_start_tc), str(event.rec_end_tc))
        print (str_)

        str_ = format1%(str(event.source_file), str(event.clip_name))
        print (str_)

        print ("------------------------------------------")



