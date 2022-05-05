class Choices():

    def __init__(self):
        #list of all possible choices
        self.choices = ["wake up", "nap", "get ready", "eat", "gather things", "check messages", "study", "phone" ]
        #choices and results should be the same length
        #note: in 2.7, dictionarys are unordered
        # sanity, hunger, exhaustion
        self.results = {
            "wake up":[0,0,0],
            "nap":[0,0,-10],
            "get ready":[0,0,0],
            "eat":[0,-10,0],
            "gather things":[5,0,0],
            "check messages":[10,0,0],
            "study":[5,0,5],
            "phone":[10,0,2]
        }
    
    def getChoices(self, time):
        if (time >= 2200) or (time<=500):
            return [self.choices[7]] # phone (needs sleep)
        if time == 630:
            return [self.choices[0],self.choices[1]] # wake up, nap
        elif time == 645:
            return [self.choices[1],self.choices[2]] # nap, get ready
        elif time == 715:
            return [self.choices[3],self.choices[4],self.choices[5],self.choices[1]] # eat, gather, check messages, nap
        elif time == 745:
            return [self.choices[6], self.choices[7],self.choices[1]] # study, phone, nap
        else:
            return ["nap"]
    
    def getChoicesWeekend(self, time):
        return ["phone"]

    def getResult(self, inputs):
        return self.results[inputs]
