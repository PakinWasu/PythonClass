class empolyee(object):
    def __init__(self) :
        self.name = 'Peter'
        self._age = 45
        self.__salary = 35000

object1 = empolyee()

print(object1.name)
print(object1._age)
print(object1.__salary)