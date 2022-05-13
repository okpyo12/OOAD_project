class CarDB:

    def __init__(self):
        self.CarNum = ''
        self.CarlotNum = ''

    def setCarNum(self, carnum):
        self.CarNum = carnum

    def getCarNum(self):
        return self.CarNum

    def setCarlotNumm(self, parkinglotnum):
        self.CarlotNum = str(parkinglotnum)

    def getCarlotNum(self):
        return self.CarlotNum