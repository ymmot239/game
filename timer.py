class Timer():

    def __init__(self):
        self.times = [2400, 100, 200, 300, 400, 500, 630, 645, 715, 745, 800, 830, 1000, 1145, 1330, 1400, 1545, 1700, 1800, 1900, 2000, 2100, 2200, 2300]
        self.weekend = [2400, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200]
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.timePointer = 6
        self.dayPointer = 0
        self.weeks = 0

    def getTime(self):
        if self.dayPointer <=  4:
            return self.times[self.timePointer]
        else:
            return self.weekend[self.timePointer]

    def getTimeString(self):
        week = ""
        day = self.days[self.dayPointer]
        hour = self.getTime()//100
        minute = self.getTime()%100
        ampm = "am"
        if (hour > 12) and (hour <24):
            hour -=12
            ampm = "pm"
        if hour == 12:
            ampm = "pm"
        if hour == 24:
            hour -=12
        if minute == 0:
            minute = "00"
        if self.weeks >0:
            week = "Week " + str(self.weeks+1) + " "
        return week + day + ", " + str(hour) + ":" + str(minute) + " " + ampm

    def incrementTime(self):
        self.timePointer+=1

        if self.dayPointer >= 5:
            if (self.timePointer > len(self.weekend)-1):
                self.timePointer = 0
                if (self.weekend[self.timePointer] == 2400) :
                    self.dayPointer+=1
            

        else:
            if self.timePointer > len(self.times)-1:
                self.timePointer = 0
            if (self.times[self.timePointer] == 2400):
                self.dayPointer+=1
                if self.dayPointer == 5:
                    self.timePointer = 0

        if self.dayPointer > len(self.days)-1:
            self.dayPointer = 0
            self.weeks+=1

    def nextDay(self):
        if self.dayPointer <=  4:
            if (self.times[self.timePointer] < 630) or self.times[self.timePointer]==2400:
                pass
            else:
                self.dayPointer+=1
                if self.dayPointer > len(self.days)-1:
                    self.dayPointer = 0
                    self.weeks+=1
            self.timePointer = 6
        else:
            if (self.times[self.timePointer] < 800) or self.times[self.timePointer]==2400:
                pass
            else:
                self.dayPointer+=1
                if self.dayPointer > len(self.days)-1:
                    self.dayPointer = 0
                    self.weeks+=1
            self.timePointer = 4
