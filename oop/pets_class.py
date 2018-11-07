class Pets:
    
    type = "mammals"

    def __init__(self, lst):
        self.lst = lst

    def num_pets(self):
        return ("I have {} dogs".format(len(self.lst)))

    def pets_type(self):
        return "And they're all {}, of course".format(self.type)

    def walk(self):
        return "they all walk"

class Dogs:
    
    is_hungry = True
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dog_details(self):
        return ("{} is {}".format(self.name, self.age))

    def eat(self):
        self.is_hungry = False
        return self.is_hungry

    def walk(self):
        return self.name + " is walking!"

tom = Dogs("Tom", 6)
fletcher = Dogs("Fletcher", 7)
larry = Dogs("Larry", 9)

petsList = Pets([tom, fletcher, larry])

print(petsList.num_pets())
print(tom.dog_details())
print(fletcher.dog_details())
print(larry.dog_details())
print(petsList.pets_type())

if((tom.eat() and fletcher.eat() and larry.eat()) == False):
    print("My dogs are not hungry")