class User:
    
    def __init__(self):
        self.car_num = 0
        self.parking = False
    
    def setCarNum(self, num):
        self.car_num = num

    def getCarNum(self):
        return self.car_num

    def getParking(self):
        return self.parking