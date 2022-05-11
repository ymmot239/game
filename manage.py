import timer
import choices
import bars
import lock

class Manager():

    def __init__(self):
        self.timer = timer.Timer()
        self.choice = choices.Choices()
        self.bar = bars.Bars()
        self.lock = lock.Lock()
        self.absence = 0

    def getTime(self):
        return self.timer.getTimeString()

    def getValues(self):
        return self.bar.get()

    def getChoices(self):
        if ("Saturday" in self.timer.getTimeString()) or ("Sunday" in self.timer.getTimeString()):
            choice_weekend =  self.choice.getChoicesWeekend(self.timer.getTime())
            bars  = self.bar.get()
            return getWeekend(bars,choice_weekend)
        else:
            choice_here = self.choice.getChoices(self.timer.getTime())
            times = self.timer.getTime()
            bars = self.bar.get()
            return self.lock.get(times, bars, choice_here,self.absence)
            #return self.choice.getChoices(self.timer.getTime())

    def makeChoice(self, choice):
        change = self.choice.getResult(choice)

        outs = self.bar.get()
        if (outs[1] < 30) or (outs[2] < 30): #additonal sanity for hunger and exhaustion
            change[0]+=2
        if (outs[1] > 70) or (outs[2] > 70):
            change[0]-=5

        self.bar.change(change[0],change[1],change[2]) #make changes based on your choices

        outs = self.bar.get()
        adjust = [0,0,0]
        self.bar.change(0,2,2) #additional hunger and exhaustion per turn
        
        for x in range(3): # cap function
            if outs[x] > 100:
                adjust[x] = 100-outs[x]
            if outs[x]<0:
                adjust[x] = -outs[x]
        self.bar.change(adjust[0],adjust[1],adjust[2])
        

        if (choice == "sleep"):
            print("insert dream game here")
            if self.timer.getTime() == 1330: 
                self.timer.incrementTime()   #if you sleep (not at lunch), you sleep until the next day
            else:
                self.timer.nextDay()
            self.bar.change(0,0,-20)
        else:
            self.timer.incrementTime()

        if choice == "no": #absences and makeups
            self.absence+=1
        if choice == "absence makeup":
            self.absence-=1

        outs = self.bar.get()
        outs.append(self.absence)
        return outs
