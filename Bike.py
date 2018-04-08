class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print "Bike's price: "+str(self.price)+ ", Bike's maximum speed: "+self.max_speed+ ", Bike's total miles: "+ str(self.miles)
        
        return self
    def ride(self):
        self.miles += 10
        print "Riding, Total miles: " + str(self.miles)
       
        return self
    def reverse(self):
        
        self.miles -= 5
        print "Reversing"
        if self.miles < 0:
            self.miles = 0
        return self


bike1 = Bike(200, "25mph")
"""bike1.ride().ride().ride().reverse().displayinfo()"""
"""bike1.ride().ride().reverse().reverse().displayinfo()"""
bike1.reverse().reverse().reverse().displayinfo()