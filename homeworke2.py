class Cat:
    print("Cat created")
    def __init__(self, name, age=1):
        self.name = name
        self.age = age
        self.hunger = 50
        self.energy = 50
    def eat(self):
        self.hunger -= 20
        print(self.name, "is eatng")

    def sleep(self):
        self.energy += 30
        print(self.name, "is sleping")

    def play(self):
        self.energy -= 20
        self.hunger += 15
        print(self.name, "is playing")
    def grow(self):
        self.age += 1

    def __str__(self):
        return f"My cat is {self.name}. Age: {self.age}"


my_cat = Cat("Barsik", 2)
print(my_cat)

my_cat.eat()
my_cat.play()
my_cat.sleep()

print("Hunger:", my_cat.hunger)
print("Energy:", my_cat.energy)

my_cat.grow()

print("New age:", my_cat.age)