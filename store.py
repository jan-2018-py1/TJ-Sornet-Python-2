class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def Sell(self):
        self.status = "sold"
        return self
    def Add_Tax(self, tax):
        self.price = self.price + (self.price * tax)
        return self.price
    def Return(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        if reason == "in the box - like new":
            self.status = "for sale"
        if reason == "open box":
            self.status = "used"
            self.price = self.price - (self.price * .20)
        return self
    def Display_Info(self):
        print "Price: ", self.price
        print "Item Name: ", self.item_name
        print "Weight: ", self.weight
        print "Brand: ", self.brand
        print "Status: ", self.status

product1 = Product(50, "Tire", "60lbs", "Hankook")
product1.Add_Tax(.12)
product1.Sell().Return("defective").Display_Info()


class Store(object):
    def __init__(self, products, location, owner):
        self.products = products[]
        self.location = location
        self.owner = owner
    def add_product(self):
        