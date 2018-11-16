
class Enemy:
    life = 3

    def attack(self):
        print('Ouch!')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + ' life left')

enemy1 = Enemy() # enemy1 is an Object
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()


'''
class Tuna:
    def __init__(self): #This part of a class gets called immediately the class is created
        print('I am a fish')

    def swim(self):
        print('I can swim')

fish = Tuna()
fish.swim()
'''

'''
class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()
'''
#A Class Variable is static for all objects while an Init Variable are unique for all objects

'''
class Girl:
    gender = 'Female'

    def __init__(self, name):
        self.name = name

r = Girl('Racheal')
s = Girl('Stacia')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)
'''
'''

class Parent():

    def print_last_name(self):
        print('Roberts')

class Child(Parent):

    def print_first_name(self):
        print('Bucky')

    def print_last_name(self):
        print('Adedapo')


check = Parent()
bucky = Child()

bucky.print_first_name()
bucky.print_last_name()
check.print_last_name()
'''

'''
class Mario():

    def move(self):
        print("I am on the move...")

class Shroom():

    def eat_mushroom(self):
        print('I am bigger!')

class BigMario(Mario, Shroom):
    pass

bm = BigMario()
bm.move()
bm.eat_mushroom()
'''

