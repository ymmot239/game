class Choices():

    def __init__(self):
        #list of all possible choices
        self.choices = ["wake up", "nap", "get ready", "eat", "gather things", "check messages", "study", "phone","socialize","yes","no","absence makeup","sleep","check grades","play video games","shower","clean" ]
        #choices and results should be the same length
        #note: in 2.7, dictionarys are unordered
        # sanity, hunger, exhaustion
        self.results = {
            "wake up":[0,0,0],           #0
            "nap":[0,0,-10],             #1
            "get ready":[0,0,0],         #2
            "eat":[0,-10,0],             #3
            "gather things":[5,0,0],     #4
            "check messages":[10,0,0],   #5
            "study":[5,0,5],             #6
            "phone":[10,0,2],            #7
            "socialize":[10,0,0],        #8
            "yes":[-10,0,5],             #9
            "no":[-20,0,5],              #10
            "absence makeup":[0,0,5],    #11
            "sleep":[0,0,0],             #12
            "check grades":[-1,0,0],     #13
            "play video games":[10,0,10],#14
            "shower":[10,0,-10],         #15
            "clean":[10,0,5]             #16
        }
    
    def getChoices(self, time):
        if (time >= 2200) or (time<=500):
            return [self.choices[7],self.choices[12]] # phone, sleep
        if time == 630:
            return [self.choices[0],self.choices[1]] # wake up, nap
        elif time == 645:
            return [self.choices[1],self.choices[2]] # nap, get ready
        elif time == 715:
            return [self.choices[3],self.choices[4],self.choices[5],self.choices[1]] # eat, gather, check messages, nap
        elif time == 745:
            return [self.choices[6], self.choices[7],self.choices[1]] # study, phone, nap
        elif time == 800:
            return [self.choices[3],self.choices[8]] # eat, socialize
        elif time == 830:
            return [self.choices[9],self.choices[10]] # yes, no
        elif time == 1000:
            return [self.choices[9],self.choices[10]] # yes, no
        elif time == 1145:
            return [self.choices[9],self.choices[10]] # yes, no
        elif time == 1330:
            return [self.choices[12], self.choices[3],self.choices[6]] # sleep, eat, study
        elif time == 1400:
            return [self.choices[9],self.choices[10]] # yes, no
        elif time == 1545:
            return [self.choices[11],self.choices[12],self.choices[6],self.choices[7],self.choices[13]] # absence makeup , sleep, study, phone, grades
        elif time == 1700:
            return [self.choices[3],self.choices[12],self.choices[14],self.choices[6]] # eat, sleep, game, study
        elif time == 1800:
            return [self.choices[3],self.choices[12],self.choices[14],self.choices[6]] # eat, sleep, game, study
        elif time == 1900:
            return [self.choices[3],self.choices[12],self.choices[14],self.choices[6]] # eat, sleep, game, study
        elif time == 2000:
            return [self.choices[3],self.choices[12],self.choices[14],self.choices[6]] # eat, sleep, game, study
        elif time == 2100:
            return [self.choices[15],self.choices[7]] #shower, phone
        else:
            return ["nap"]
    
    def getChoicesWeekend(self, time):
        return [self.choices[3],self.choices[7],self.choices[14],self.choices[6],self.choices[16],self.choices[12]] #eat, phone, game, study, clean, sleep

    def getResult(self, inputs):
        return self.results[inputs]


