from datetime import datetime

class Order:
    def __init__(self, id, customer, order, time_of_order):
        self.id = id
        self.customer = customer
        self.order = order
        self.time_of_order = time_of_order

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Order: {self.id}, {self.customer}   Order: {self.order} Order made at: {self.time_of_order}'