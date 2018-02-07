class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        # conditional to prevent instance from having negative miles
        if self.miles < 5:
            return self
        else:
            self.miles -= 5
        return self


bike1 = Bike(150, "25mph")
bike2 = Bike(200, "30mph")
bike3 = Bike(250, "35mph")

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()
