class Customer:
    def __init__(self, id, name, order=[]):
        self.id = id
        self.name = name
        self.order = order

    def add_order(self, order):
        self.order.append(order)