import math
class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, arg, *args):
        # Check the type() of 1st argument
        # if tuple (which can be a list or another tuple), iterate through values
        if type(arg) == tuple or type(arg) == list:
            for i in arg:
                if type(i) == list or type(i) == tuple:
                    # add values inside list or tuple using sum() function
                    self.result += sum(i)
                else:
                    # if type() int, add value to self.result without using sum() function - syntax error if sum() is used
                    self.result += i
        else: 
            # type() int
            self.result += arg

        # Check the type() of additional arguments using same logic as 1st argument
        if type(args) == tuple:
            for i in args:
                if type(i) == list or type(i) == tuple:
                    self.result += sum(i)
                else:
                    self.result += i
        return self
    def subtract(self, arg, *args):
        # Check the type() of 1st argument
        # if tuple (which can be a list or another tuple), iterate through values
        if type(arg) == tuple or type(arg) == list:
            for i in arg:
                if type(i) == list or type(i) == tuple:
                    # subtract the sum() of values in list/tuple from result
                    self.result -= sum(i)
                else:
                    # subtract value if type() int
                    self.result -= i
        else: 
            # type() int
            self.result -= arg

        # Check the type() of additional arguments using same logic as 1st argument
        if type(args) == tuple:
            for i in args:
                if type(i) == list or type(i) == tuple:
                    self.result -= sum(i)
                else:
                    self.result -= i
        return self

md = MathDojo()
print "Result: ", md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
cd = MathDojo()
print "Result: ", cd.add(2).add(2,5).subtract(3,2).result
rd = MathDojo()
print "Result: ", rd.add((2,3), 4).add(5,[5,7,1.2]).add(1,(4,2)).subtract([3,4],(2,1)).result