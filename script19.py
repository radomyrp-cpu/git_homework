class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger= 40
        self.energy = 60
    def eat(self):
        self.hunger -= 30
        if self.hunger <0:
            self.hunger = 0
        print(self.name, "is eating")
    def play(self):
        self.hunger += 10
        self.energy -= 20
        print(self.name, "is playing")
    def sleep(self):
        self.energy += 40
        if self.energy > 100:
            self.energy = 100
        print(self.name, "is sleeping")
    def __str__(self):
        return f"Cat: {self.name}. Hunger: {self.hunger}. Energy: {self.energy}"
class Human:
    def __init__(self, name, cat):
        self.name = name
        self.cat = cat
        self.money = 60
    def work(self):
        self.money += 50
        print(self.name, "went to work")
    def feed_cat(self):
        if self.money < 20:
            self.work()
        self.money -= 20
        self.cat.eat()
    def live_day(self, day):
        print("Day:", day)
        self.cat.hunger += 15
        if self.cat.hunger >= 40:
            self.feed_cat()
        if self.cat.energy < 30:
            self.cat.sleep()
        else:
            self.cat.play()
        print("Money:", self.money)
        print(self.cat)
my_cat = Cat("Хлоя")
human = Human("я", my_cat)
for day in range(1, 8):
    human.live_day(day)
print("nоne week passed")