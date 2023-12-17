from datetime import datetime

class Order:
    def __init__(self, id, customer, order, date):
        self.id = id
        self.customer = customer
        self.order = order
        self.date = date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Order: {self.id} customer: {self.customer} order: {self.order} time ordered: {self.date}'