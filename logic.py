
"""
class bars(enum.ENUM):
    SANITY = 50
    HUNGER = 50
    EXHAUSTION = 50

    def change(self,value):
        self.value = value
"""

class Timer():

    def __init__(self):
        self.times = [630, 645, 715, 745, 800, 830, 1000, 1145, 1330, 1400, 1545, 1700, 1800, 1900, 2000, 2100, 2200,
        2300, 2400, 100, 200, 300, 400, 500]
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.timePointer = 0
        self.dayPointer = 0
        self.weeks = 0

    def getTime(self):
        return self.times[self.timePointer]

    def getTimeString(self):
        week = ""
        day = self.days[self.dayPointer]
        hour = self.times[self.timePointer]//100
        minute = self.times[self.timePointer]%100
        ampm = "am"
        if (hour > 12) and (hour <24):
            hour -=12
            ampm = "pm"
        if minute == 0:
            minute = "00"
        if self.weeks >0:
            week = "Week " + str(self.weeks+1)
        return week + " " + day + ", " + str(hour) + ":" + str(minute) + " " + ampm

    def incrementTime(self):
        self.timePointer+=1
        if self.timePointer > len(self.times)-1:
            self.timePointer = 0
        
        if self.times[self.timePointer] == 2400:
            self.dayPointer+=1

        if self.dayPointer > len(self.days)-1:
            self.dayPointer = 0
            self.weeks+=1

    def nextDay(self):
        if (self.times[self.timePointer] < 630) or self.times[self.timePointer]==2400:
            pass
        else:
            self.dayPointer+=1
            if self.dayPointer > len(self.days)-1:
                self.dayPointer = 0
                self.weeks+=1
        self.timePointer = 0
        
        
