from CarDB.CarDB import CarDB

class CarDBController(CarDB):

    def __init__(self):
        self.carDB = CarDB()

    def settingCarNum(self, carnum):
        self.carDB.setCarNum(carnum)

    def gettingCarNum(self):
        return self.carDB.getCarNum()

    def settingCarlotNum(self, parkinglotnum):
        self.carDB.setCarlotNum(parkinglotnum)

    def gettingCarlotNum(self):
        return self.carDB.getCarlotNum()

    def settingParkingLotArr(self):
        with open("CarDB/LotDB.txt", 'r+') as f:
            lines = f.readlines()
            for line in lines:
                line = line.rstrip()
                self.carDB.parkinglotarr.append(int(line))

    def gettingParkingLotArr(self):
        return self.carDB.getParkingLotarr()

    def saveParkingLotArr(self):
        with open("CarDB/LotDB.txt", 'w') as f:
            for i in range(14):
                f.write(str(self.carDB.parkinglotarr[i])+"\n")
    

    def insertDB(self, carnum, parkinglotnum):
        self.settingCarNum(carnum)
        self.settingCarlotNum(parkinglotnum)
        if self.isCarNum():
            with open("CarDB/DB.txt", 'r') as f:
                lines = f.readlines()
            with open("CarDB/DB.txt", 'a') as f:
                for line in lines:
                    line = line.rstrip()
                    Carnum, Lotnum = line.split(':')
                    if Carnum == self.carDB.CarNum or Lotnum == self.carDB.CarlotNum:
                        return False
                f.write(self.carDB.CarNum+":"+self.carDB.CarlotNum+"\n")
            self.settingCarNum('')
            self.settingCarlotNum('')
            return True
        else:
            self.settingCarNum('')
            self.settingCarlotNum('')
            return False
        
    def deleteDB(self, text, parkinglotnum):
        self.settingCarNum(text)
        self.settingCarlotNum(parkinglotnum)
        checknum = 0
        if self.isCarNum():
            with open("CarDB/DB.txt", 'r') as f:
                lines = f.readlines()
            with open("CarDB/DB.txt", 'w') as f:
                for line in lines:
                    line = line.rstrip()
                    carnum, lotnum = line.split(':')
                    if (self.carDB.CarNum == carnum and self.carDB.CarlotNum == lotnum):
                        checknum = 1
                    else:
                        f.write(line+"\n")
            if checknum == 1:
                self.saveParkingLotArr()
                return True
            else:
                return False
        else:
            return False

    def isCarNum(self):
        if len(self.carDB.CarNum) == 7 or len(self.carDB.CarNum) == 8:
            if len(self.carDB.CarNum) == 7:
                if (self.carDB.CarNum[0:1].isdigit() and self.carDB.CarNum[2].isalpha() and self.carDB.CarNum[3:6].isdigit()):
                    return True
                else:
                    return False
            else:
                if (self.carDB.CarNum[0:2].isdigit() and self.carDB.CarNum[3].isalpha() and self.carDB.CarNum[4:7].isdigit()):
                    return True
                else:
                    return False
        else:
            return False