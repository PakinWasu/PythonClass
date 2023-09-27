class Pets:
    dogs = []
    def __init__(self,dogs):
        self.dogs = dogs

class Dog:
    species = 'mammal'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def description(self):
        return self.name,self.age
    
    def speak(self,sound):
        return "%s say %s"%(self.name,sound)
    def eat(self):
        self.is_hungry = False

class RussellTerrier(Dog):
    def run(self,speed):
        return '{} runs {}'.format(self.name,speed)
    
class Bulldog(Dog):
    def run(self,speed):
        return '{} runs {}'.format(self.name,speed)

my_dogs = [
    Bulldog('Tom',6),
    RussellTerrier('Fletcher',7),
    Dog("Larry",9)
]

my_pets = Pets(my_dogs)

print('I have {} dogs'.format(len(my_pets.dogs)))

for dog in my_pets.dogs:
    print('{} is {}.'.format(dog.name,dog.age))
print("And thery're all {}s , of couse".format(dog.species))
