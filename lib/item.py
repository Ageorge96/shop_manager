class Item:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Item: {self.id} {self.name} £{self.price:.2f}     Stock:{self.quantity}'

    def add_stock(self, quantity):
        self.quantity += quantity

    def reduce_stock(self, quantity):
        self.quantity -= quantity