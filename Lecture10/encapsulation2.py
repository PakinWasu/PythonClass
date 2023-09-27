class employee():
    def __init__(self) :
        self.__maxearn = 30000
        
    def earn(self):
        print('eraning is:{}'.format(self.__maxearn))
    
    def setmaxeran(self,earn):
        self.__maxearn = earn


emp1 = employee()
emp1.earn()

emp1.__maxearn = 10000
emp1.earn()

emp1.setmaxeran(15000)
emp1.earn()