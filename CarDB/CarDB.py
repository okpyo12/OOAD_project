class CarDB:

    def __init__(self):
        self.CarNum = ''
        self.CarlotNum = ''
        self.parkinglotarr = []

    def setCarNum(self, carnum):
        self.CarNum = carnum

    def getCarNum(self):
        return self.CarNum

    def setCarlotNumm(self, parkinglotnum):
        self.CarlotNum = str(parkinglotnum)

    def getCarlotNum(self):
        return self.CarlotNum

    def setParkingLotarr(self, lotarr):
        self.parkinglotarr = lotarr

    def getParkingLotarr(self):
        return self.parkinglotarr