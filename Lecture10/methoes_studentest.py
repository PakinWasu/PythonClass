class StudentTest:
    def __init__(self,name,score1,score2,score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def sumScore(self):
        return self.score1+self.score2+self.score3
    
    def __str__(self) :
        return 'Name:{}, Total of score: {}'.format(self.name,self.sumScore())
    
std1 = StudentTest('Jantra',20,35,25)
print(std1.name,std1.sumScore)

print(std1)