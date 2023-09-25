class Dog:
    species = 'mammal'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def description(self):
        return "{0} is {1} years old".format(self.name,self.age)
    
    def speak(self,sound):
        return "{} say {}".format(self.name,sound)


class RussellTerrier(Dog):
    def run(self,speed):
        return '{} runs {}'.format(self.name,speed)
    
class Bulldog(Dog):
    def run(self,speed):
        return '{} runs {}'.format(self.name,speed)


jim = Bulldog('Jim',12)
print(jim.description)

print(jim.run('slowly'))
print(isinstance(jim,Dog))

julie = Dog('julie',100)
print(isinstance(julie,Dog))

johnnywalker = RussellTerrier('johnny Walker',4)
print(isinstance(johnnywalker,Bulldog))

print(isinstance(julie,jim))