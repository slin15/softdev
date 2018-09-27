#Team GG -- Joyce Liao and Susan Lin
#SoftDev1 pd8
#K#06: StI/O: Divine your Destiny!
#2018-09-14

import random 
diction = {}

def convertToDict(filename):
    f = open(filename, 'r')
    text = f.read().split("\n")
    #turns the csv file into a list separated by commas
    for index in range (1, len(text)- 2):
        cat = text[index].rsplit(',', 1)
        #splits each string in text into title and percent
        title = cat[0].strip('"')
        #removes quotes from title 
        percent = float(cat[-1])
        #typecasts the percent into a float 
        diction[title] = percent
        #sets the value of the title key in diction to percent
    return diction 

def findLast():
    diff = 100.0
    for key in diction:
        diff -= diction[key]
        #subtracts percent of each occupation from total 
    return ("%.1f" % diff)
    #rounds the difference to the nearest tenth 

def randomOcc():
    randlist = []
    for key in diction:
        current = diction[key]
        #stores the percent of each title
        freq = int(current *10)
        #we are storing each title by percent (x10 to rid decimal) in a list
        for i in range (freq):
            randlist.append(key)
            #returns a randomly selected occupation
    return (random.choice(randlist))

