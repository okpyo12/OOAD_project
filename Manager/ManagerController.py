from Manager.Manager import Manager

class ManagerController(Manager):

    def __init__(self):
        self.manager = Manager()

    def settingFixedCarNum(self, carnum):
        self.manager.setFixedCar(carnum)

    def gettingFixedCarNum(self):
        return self.manager.getFixedCar()

    def settingFixedCarlotNum(self, parkinglotnum):
        self.manager.setFixedCarlotNumm(parkinglotnum)

    def gettingCarlotNum(self):
        return self.manager.getFixedCarlotNum()
    
    def clearDB(self):
        with open("Manager/FixedCarDB.txt", 'w') as f:
            f.write('')

    def settingFixecCarDB(self):
        self.manager.fixedcardb = []
        with open("Manager/FixedCarDB.txt", 'r+') as f:
            lines = f.readlines()
            for line in lines:
                line = line.rstrip()
                Carnum, Lotnum = line.split(':')
                self.manager.fixedcardb.append([Carnum,Lotnum])

    def gettingFixedCarDB(self):
        return self.manager.getFixedCarDB()
            

    def insertFixedCarDB(self, carnum, parkinglotnum):
        self.settingFixedCarNum(carnum)
        self.settingFixedCarlotNum(parkinglotnum)
        if self.isCarNum():
            with open("Manager/FixedCarDB.txt", 'r') as f:
                lines = f.readlines()
            with open("Manager/FixedCarDB.txt", 'a') as f:
                for line in lines:
                    line = line.rstrip()
                    Carnum, Lotnum = line.split(':')
                    if self.manager.fixedcarnum == Carnum or self.manager.fixedcarlotnum == Lotnum or int(self.manager.fixedcarlotnum) > 15 or int(self.manager.fixedcarlotnum) < 1:
                        return False
                f.write(self.manager.fixedcarnum+":"+self.manager.fixedcarlotnum+"\n")
            
            with open("CarDB/LotDB.txt", 'r') as f:
                lines = f.readlines()
            with open("CarDB/LotDB.txt", 'w') as f:
                cnt = 0
                for line in lines:
                    line = line.rstrip()
                    if cnt != int(self.manager.fixedcarlotnum)-1:
                        f.write(line+"\n")
                    else:
                        f.write("2"+"\n")
                    cnt += 1

            self.settingFixedCarNum('')
            self.settingFixedCarlotNum('')
            return True
        else:
            self.settingFixedCarNum('')
            self.settingFixedCarlotNum('')
            return False
    
    def deleteFixedCarDB(self, carnum, parkinglotnum):
        self.settingFixedCarNum(carnum)
        self.settingFixedCarlotNum(parkinglotnum)
        checknum = 0
        if self.isCarNum():
            with open("Manager/FixedCarDB.txt", 'r') as f:
                lines = f.readlines()
            with open("Manager/FixedCarDB.txt", 'w') as f:
                for line in lines:
                    line = line.rstrip()
                    carnum, lotnum = line.split(':')
                    if self.manager.fixedcarnum == carnum and self.manager.fixedcarlotnum == lotnum or int(self.manager.fixedcarlotnum) > 15 or int(self.manager.fixedcarlotnum) < 1:
                        checknum = 1
                    else:
                        f.write(line+"\n")
            if checknum == 1:
                with open("CarDB/LotDB.txt", 'r') as f:
                    lines = f.readlines()
                with open("CarDB/LotDB.txt", 'w') as f:
                    cnt = 0
                    for line in lines:
                        line = line.rstrip()
                        if cnt != int(self.manager.fixedcarlotnum)-1:
                            f.write(line+"\n")
                        else:
                            f.write("0"+"\n")
                        cnt += 1
                return True
            else:
                return False
        else:
            return False
    
    def isCarNum(self):
        if len(self.manager.fixedcarnum) == 7 or len(self.manager.fixedcarnum) == 8:
            if len(self.manager.fixedcarnum) == 7:
                if (self.manager.fixedcarnum[0:1].isdigit() and self.manager.fixedcarnum[2].isalpha() and self.manager.fixedcarnum[3:6].isdigit()):
                    return True
                else:
                    return False
            else:
                if (self.manager.fixedcarnum[0:2].isdigit() and self.manager.fixedcarnum[3].isalpha() and self.manager.fixedcarnum[4:7].isdigit()):
                    return True
                else:
                    return False
        else:
            return False