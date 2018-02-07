class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()
    def display_all(self):
        print "Price: ", self.price
        print "Speed: ", self.speed
        print "Fuel: ", self.fuel
        print "Mileage: ", self.mileage
        print "Tax: ", self.tax
        print "---------------"

car1 = Car(8000, "60mph", "Full", "30mpg")
car2 = Car(10000, "65mph", "Half Full", "27mpg")
car3 = Car(15000, "80mph", "Empy", "25mpg")
car4 = Car(5500, "40mph", "Quarter Full", "40mpg")
car5 = Car(11000, "70mph", "Almost Empy", "15mpg")
car6 = Car(25000, "100mph", "Full", "10mpg")


    