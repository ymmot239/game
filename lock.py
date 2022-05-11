
class Lock():
    
    def get(self,time,bars,choice, absence):
        final = choice
        locked = []
        if time == 630:
            if bars[2]>50:
                locked.append(final.pop(0))
        if time == 745:
            if bars[0] <80:
                locked.append(final.pop(0))
        if (time == 830) or (time == 1000) or (time == 1145) or (time == 1400):
            if bars[2]<80:
                locked.append(final.pop(1))
        if (time == 1330) or (time == 1545):
            if bars[0]<80:
                locked.append(final.pop(2))
        if time == 1545:
            if absence <=4:
                locked.append(final.pop(0))
        if (time==1700) or (time == 1800) or (time==1900) or (time == 2000):
            if bars[0]<80:
                locked.append(final.pop(3))
        if time ==2100:
            if bars[2]<80:
                locked.append(final.pop(1))
        if (time ==2200) or (time == 2300) or (time == 2400):
            if bars[2]<90:
                locked.append(final.pop(1)) 
        if time <= 500:
            if bars[2]<90:
                locked.append(final.pop(1)) 
        return [final,locked]
        
    def getWeekend(self,bars,choice):
        final = choice
        locked = []
        if bars[0]<90:
            locked.append(final.pop(4))
        if bars[0]<80:
            locked.append(final.pop(3))
        return [final,locked]
        
