
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
        self.pointer = 0

    def getTimeString(self):
        hour = self.times[self.pointer]//100
        minute = self.times[self.pointer]%100
        ampm = "am"
        if hour > 12:
            hour -=12
            ampm = "pm"
        if minute == 0:
            minute == "00"
        return str(hour) + ":" + str(minute) + " " + ampm

    def incrementTime(self):
        self.pointer+=1

