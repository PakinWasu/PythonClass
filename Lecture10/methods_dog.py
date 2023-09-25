class Dog:
    species = 'mammal'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def description(self):
        return "{0} is {1} years old".format(self.name,self.age)
    
    def speak(self,sound):
        return "{} say {}".format(self.name,sound)

mikey = Dog('Mikey',6)

print(mikey.description)
print(mikey.speak('Gruff Gruff'))
