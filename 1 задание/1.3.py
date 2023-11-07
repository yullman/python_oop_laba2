class car:
    color = None
    fuel = None
    spoiler = None
    shini = None

    def turn(self):
        pass
    
    def go(self):
        pass
    
    def stop(self):
        pass

myCar = car()
myCar.color = 'Black'
myCar.spoiler = 'netu'
myCar.fuel = 1000


def info(self):
    print(self.color)
    print(self.fuel)
    print(self.spoiler)
    print(self.shini)
    
info(myCar)

print("")

car2 = car()
car.color = 'blue'
car.fuel = 100

info(car2)
