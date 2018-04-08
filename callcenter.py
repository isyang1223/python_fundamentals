class Call(object):
    def __init__(self, uniq_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.uniq_id = uniq_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    def display(self):
        print self.uniq_id, self.caller_name, self.caller_phone_number, self.time_of_call, self.reason_for_call
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
    def add(self, newcall):
        self.calls.append(newcall)
        self.queue_size = len(self.calls)
        return self
    def remove(self,x):
        self.calls.pop(x)
        self.queue_size = len(self.calls)
        return self
    def info(self):
        for i in self.calls:
            print i.caller_name
            print i.caller_phone_number
            print self.queue_size
        
        return self

call1 = Call(123, "johnnie", "510-666-666", "7:00", "911")
call2 = Call(234, "ian", "951-902-0006", "3:00", "what")

call3 = Call(565, "thinh", "510-234-3426", "12:00", "for")


center = CallCenter()
center.add(call1).add(call2).add(call3).remove(1).info()