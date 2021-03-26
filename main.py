class Cashier:
    def _init_(self, name, num):
        self.name = name
        self.num = num

    def helpCustomer(self):
        print("Help Customer")
        return True


class Customer:
    def __init__(self, name):
        self.name = name

    def makerOrder(self, order):
        print("I")
        return True


class Cook:
    def _init_(self, name, num):
        self.name = name
        self.num = num

    def helpCustomer(self):
        print("Help Customer")
        return True


Cashier = ('Lily')
