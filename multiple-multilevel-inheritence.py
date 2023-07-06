class Prey:
     def flee(self):
        print("This animal cant defend itself")

class Predator:
    def hunt(self):
        print("This animal is a menace")



class Organism:

    alive = True

class Animal(Organism):

    def eating(self):
        print(f"This animal is eating")

class Plant(Organism):
     
    def Absorb(self):
        print("This animal is absorbing nutrition")


        
class Rabbit(Animal, Prey):

    def eat_carrot(self):
        print("eat carrot")

class Dog(Animal, Predator, Prey):

    def hunt_rabbit(self):
        print("dog can hunt rabbit")

    def dog_hunted(self):
        print("Dog can be hunt down")

class Venus_Flytrap(Plant, Predator):

    def eats_bugs(self):
        print("this plant eats bugs")

class Mushroom(Predator, Plant, Prey):

    def in_hotpot(self):
        print("some kind of mushroom can be in hotpot")

    def toxic(self):
        print("toxic mushroom, hehe")

rabbit = Rabbit()
dog = Dog()
flytrap = Venus_Flytrap()
mushroom = Mushroom()

#Dogs
print("dogs")
dog.dog_hunted()
dog.eating()
dog.hunt_rabbit()
dog.hunt()

#rabbit
print("rabbit")
rabbit.eat_carrot()
rabbit.eating()
rabbit.flee()

#flytrap
print("flytrap")
flytrap.Absorb()
flytrap.eats_bugs()
flytrap.hunt()

#mushroom
print("Mushroom")
mushroom.toxic()
mushroom.Absorb()
mushroom.flee()