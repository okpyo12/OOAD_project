class Manager:

    def __init__(self):
        self.manager = ''
        self.fixedcarnum = ''
        self.fixedcarlotnum = 0
        self.fixedcardb = []

    def setFixedCar(self, carnum):
        self.fixedcarnum = carnum

    def getFixedCar(self):
        return self.fixedcarnum

    def setFixedCarlotNumm(self, parkinglotnum):
        self.fixedcarlotnum = str(parkinglotnum)

    def getFixedCarlotNum(self):
        return self.fixedcarlotnum

    def setFixedCarDB(self):
        self.fixedcardb = self.fixedcardb

    def getFixedCarDB(self):
        return self.fixedcardb