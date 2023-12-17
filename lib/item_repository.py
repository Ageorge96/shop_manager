from .item import Item

class ItemRepository:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM items')

        items = []

        for row in rows:
            items.append(Item(row['id'], row['name'], row['price'], row['quantity']))

        return items
    
    def add(self, item):
        self.connection.execute('INSERT INTO items (name, price, quantity) VALUES (%s, %s, %s)', [item.name, item.price, item.quantity])