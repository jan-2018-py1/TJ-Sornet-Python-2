class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 0
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health += 5
        return self
    def display_health(self):
        print "Health: ", self.health
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"

animal = Animal("king")
animal.walk().walk().walk().run().run().display_health()
# animal.pet().fly().display_health() # confirm that Animal class cannot call pet() and fly() method and display_health() does not say "I am a Dragon"

dog = Dog("lassie")
dog.walk().walk().walk().run().run().pet().display_health()
# dog.fly().display_health() # confirm that Dog class cannot fly

dragon = Dragon("drako")
dragon.display_health()

