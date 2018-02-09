import datetime

now = datetime.datetime.now()

class Call(object):
    def __init__(self, id, caller_name, caller_number, time_of_call, reason_of_call):
        self.id = id
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time_of_call = time_of_call
        self.reason_of_call = reason_of_call
    def display(self):
        print "ID: ", self.id
        print "Caller Name: ", self.caller_name
        print "Caller Number: ", self.caller_number
        print "Time of Call: ", self.time_of_call
        print "Reason of Call: ", self.reason_of_call
        print "--------------"

class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.q_size = len(calls)
    def add(self, caller):
        # insert new caller to end of queue
        self.calls.insert(self.q_size, caller)
        self.q_size += 1
    def remove(self):
        # remove caller at beginning of queue
        self.calls.pop(0)
        self.q_size -= 1
    def remove_call(self, number):
        # remove caller by phone number
        for i in range(0, self.q_size):
            if self.calls[i].caller_number == number:
                self.calls.pop(i)
                self.q_size -= 1
                break
    def sort(self):
        for i in range(0, self.q_size):
            for j in range(0, self.q_size):
                if self.calls[i].time_of_call < self.calls[j].time_of_call:
                    temp = self.calls[i]
                    self.calls[i] = self.calls[j]
                    self.calls[j] = temp
    def info(self):
        for i in range(0, self.q_size):
            print "Name: ", self.calls[i].caller_name
            print "Number: ", self.calls[i].caller_number
            print "Callers in Queue: ", self.q_size
            print "Time of Call: ", self.calls[i].time_of_call
            print "---------------"

# now.strftime("%X")
call1 = Call(3, "TJ", "510-111-1111", "2:00", "sales")
call2 = Call(4, "Frances", "510-222-2222", "2:05", "technical")
call3 = Call(5, "Lucas", "510-333-3333", "2:10", "return")
call4 = Call(6, "Vincent", "510-444-4444", "1:50", "sales")
callers = [call1, call2, call3]
sfCallers = CallCenter(callers)
sfCallers.info()
sfCallers.add(call4)
sfCallers.info()
sfCallers.remove_call("510-333-3333")
sfCallers.info()
sfCallers.remove()
sfCallers.info()
sfCallers.add(call1)
sfCallers.info()
sfCallers.sort()
sfCallers.info()
