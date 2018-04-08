class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        print self.status
        return self
    def add_tax(self, tax):
        self.price += self.price*tax
        print self.price
        return self
    def return_item(self, reason, box):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            print self.status, self.price
        else:
            if box == "new":
                self.status = "for sale"
                print self.status
            elif box == "opened":
                self.status = "used"
                self.price *= .8
                print self.status, self.price
        return self
    def display_info(self):
        print "Price: ", str(self.price)
        print "Item name: ", str(self.item_name)
        print "Weight: ", str(self.weight)
        print "Brand: ", str(self.brand)
        print "Status: ", str(self.status)
        return self
            
product = Product(2000,"gucci bag","20lbs","gucci")

product.return_item("", "opened")


        

