import numpy as np
class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, arg, *args):
        self.result += 0 + arg + sum(args)
        return self
    def subtract(self, arg, *args):
        self.result -= (arg + sum(args))
        return self

md = MathDojo()
print "Result: ", md.add(2).add(2,5).subtract(3,2).result


