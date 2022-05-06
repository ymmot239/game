class Bars():

    def __init__(self):
        self.sanity = 50
        self.hunger = 50
        self.exhaustion = 50

    def change(self,s,h,e):
        self.sanity +=s
        self.hunger+=h
        self.exhaustion+=e
    
    def get(self):
        return [self.sanity,self.hunger,self.exhaustion]
