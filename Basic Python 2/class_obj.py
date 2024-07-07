class Dog:
    def __init__(self, breed, size, color, age):
        self.breed = breed
        self.size = size
        self.color = color
        self.age = age
        self.health = 50

    def eat(self):
        self.health += 1

    def sleep(self):
        self.health += 2

    def play(self):
        self.health -= 1

    def bark(self):
        if self.health <= 0:
            print("Dog is dead")
        elif self.health <= 30:
            print("Dog is sick")
        else:
            print("Woof Woof")

    def sick(self):
        self.health -= 10


chow = Dog("Chow Chow", "Large", "White", 1)
chow.bark()
chow.eat()
for i in range(5):
    chow.sick()
chow.bark()
chow.sleep()
chow.sick()
chow.bark()
