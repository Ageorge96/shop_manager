from .item import Item

class ItemRepository:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM items ORDER BY id')

        items = []

        for row in rows:
            items.append(Item(row['id'], row['name'], row['price'], row['quantity']))

        return items
    
    def add(self, item: Item):
        self.connection.execute('INSERT INTO items (name, price, quantity) VALUES (%s, %s, %s)', [item.name, item.price, item.quantity])

    def find(self, column, item):
        rows = self.connection.execute('SELECT * FROM items ORDER BY id')

        for row in rows:
            if item == row[column]:
                return Item(row['id'], row['name'], row['price'], row['quantity'])
            
        print('Item not found in records')
        return None
    
    def take_stock(self, order: dict):
        for item, quantity in order.items():
            self.connection.execute('UPDATE items SET quantity = quantity - %s WHERE name = %s', [quantity, item])