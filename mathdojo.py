"""class MathDojo(object):
    def __init__(self, num):
        self.num = 0
    def add(self, *add):
        self.num+=sum(add)
        return self
    def subtract(self, *sub):
        self.num-=sum(sub)
        return self
    def result(self):
        print self.num
        return self
    
md = MathDojo(0)
md.add(2).add(2,5).subtract(3,2).result()"""


class MathDojo(object):
    def __init__(self, num):
        self.num = 0
    def add(self, *add):
        for i in add:
            if type(i) == list:
                for x in i:
                    self.num+=x
            elif type(i) == tuple:
                for x in i:
                    self.num+=x
            elif type(i) == int:
                self.num+=i
        return self

    def subtract(self, *sub):
        for i in sub:
            if type(i) == list:
                for x in i:
                    self.num-=x
            elif type(i) == tuple:
                for x in i:
                    self.num-=x
            elif type(i) == int:
                self.num-=i
        return self
    
    def result(self):
        print self.num
        return self

md = MathDojo(0)
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()