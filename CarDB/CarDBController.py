from CarDB.CarDB import CarDB

class CarDBController(CarDB):

    def __init__(self):
        self.carDB = CarDB()

    def settingCarNum(self, carnum):
        self.carDB.setCarNum(carnum)

    def gettingCarNum(self):
        return self.carDB.getCarNum()

    def settingCarlotNum(self, parkinglotnum):
        self.carDB.setCarlotNumm(parkinglotnum)

    def gettingCarlotNum(self):
        return self.carDB.getCarlotNum()
    
    def clearDB(self):
        with open("CarDB/DB.txt", 'w') as f:
            f.write('')

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

    def insertDB(self, carnum, parkinglotnum):
        self.settingCarNum(carnum)
        self.settingCarlotNum(parkinglotnum)
        if self.isCarNum():
            with open("CarDB/DB.txt", 'a') as f:
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
                return True
            else:
                return False
        else:
            return False