from .order import Order
from datetime import datetime

class OrderRepository:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("""
            SELECT orders.id, customers.name, orders.item_id, orders.item_quantity, orders.order_time
            FROM orders JOIN customers ON orders.customer_id = customers.id
            """)
        
        orders = []

        for row in rows:
            
            order_dict = self.order_to_dict(row['item_id'], row['item_quantity'])
            #items = row['item_id'].split(', ')
            #quantities = row['item_quantity'].split(', ')


            orders.append(Order(row['id'], row['name'], order_dict, row['order_time']))
        return orders
    
    def make_order(self, order: Order):
        # check order item is avaliable
        items_list = list(order.order.keys())
        quantities_list = map(str, order.order.values())

        item_ids = []

        for item in items_list:
            item_id = self.connection.execute("SELECT id FROM items WHERE name = %s", [item])
            item_ids.append(str(item_id[0]['id']))


        order_items = ", ".join(item_ids)
        order_quantities = ", ".join(quantities_list)

        customer = self.connection.execute("SELECT id FROM customers WHERE name = %s", [order.customer])

        self.connection.execute("""
            INSERT INTO orders (item_id, item_quantity, order_time, customer_id) 
            VALUES (%s, %s, %s, %s)""", [order_items, order_quantities, order.time_of_order, customer[0]['id']])
    

    def order_to_dict(self, item_ids, quantities):
        
        item_id_list = item_ids.split(', ')
        quantities_list = map(int, quantities.split(', '))
        item_names = []



        for item in item_id_list:
            rows = self.connection.execute("SELECT name FROM items WHERE id = %s", [item])
            item_names.append(rows[0]['name'])

        return dict(zip(item_names, quantities_list))