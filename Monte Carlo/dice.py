'''
Monte Carlo simulation to estimate the frequency 
of the different types of rolls of 5 5-sided dice
'''
__author__ = "Casey Bladow"
import random

class Roll:
    def __init__(self):
        self.__die = [0]*5              # what is the face value of each die
        self.__count = [0]*6            # how many of each face value
        self.__categoryCount = dict()   # how many occurances of each category
        self.__categoryCount['straight'] = 0
        self.__categoryCount['5ofakind'] = 0
        self.__categoryCount['4ofakind'] = 0
        self.__categoryCount['fullhouse'] = 0
        self.__categoryCount['3ofakind'] = 0
        self.__categoryCount['2pair'] = 0
        self.__categoryCount['pair'] = 0
        self.__categoryCount['unknown'] = 0    # this should remain 0 - SAFE GUARD

    def toss(self):
        self.__count = [0]*6            # zero the counters
        for d in range(len(self.__die)):
            roll = random.randint(1,5)
            self.__die[d] = roll        # save the face value
            self.__count[roll] += 1     # increment the count for that face value

    def __str__(self):
        self.__die.sort()
        return "%d %d %d %d %d" %(self.__die[0],self.__die[1],self.__die[2],self.__die[3],self.__die[4])

    def evaluate(self):
        '''
        what category of roll is this?
        increment the appropriate counter and return the category
        '''

        # you may want to add some code here
        # Create the counts list
        counts = [0] * 7
        for value in self.__die:
            counts[value] = counts[value] + 1

        #This should remain 0 - SAFE GUARD
        category = 'unknown'
        
        # replace False in the following statements with appropriate conditions
        if 5 in counts:
            category = '5ofakind'
        elif 4 in counts:
            category = '4ofakind'
        elif (3 in counts) and (2 in counts):
            category = 'fullhouse'
        elif 3 in counts:
            category = '3ofakind'
        elif not (2 in counts) and (counts[1] == 0 or counts[6] == 0):
            category = 'straight'
        elif counts.count(2) == 2:
            category = '2pair'
        else:
            category = 'pair'

        self.__categoryCount[category] += 1
        return category
        
    def printStats(self):
        for item in self.__categoryCount:
            print("%5d  %s"%(self.__categoryCount[item], item))
            
if __name__ == "__main__":
    trials = int(input("How many trials? "))
    random.seed()
    r = Roll()
    for trial in range(trials):
        r.toss()
        cat = r.evaluate()
        # The following line was removed for speed
        # print(r, cat)

    r.printStats()
