from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository, Item
from lib.order_repository import OrderRepository, Order
from datetime import datetime

class Application:

    def __init__(self):
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.connection.seed('seeds/shop_table.sql')
        self.item_repo = ItemRepository(self.connection)
        self.order_repo = OrderRepository(self.connection)

# ======= Main program =======
    def run(self):
        print('Welcome to your Shop Manager\n')
        print('What would you like to do?\n')

        menu_string = """\
1 - See all items
2 - Add item
3 - Add stock to item
4 - See all orders
5 - Add order
"""
        
        
        while True:
            print(menu_string)
            selected = input('Select an option: ')

            if self.input_valid(selected, menu_string):
                break

        match selected:
            case '1':
                self.all_items()
            case '2':
                self.add_item_to_store()
            case '3':
                self.add_stock_to_item()
            case '4':
                self.all_orders()
            case '5':
                self.make_order()
            case 'clear':
                self.connection.seed('seeds/clear_shop.sql')
            
        self.exit_program()

    def exit_program(self):
        while True:
            quit = input('\nDo you want to exit Shop Manager? y/n ').lower()

            if quit == 'y':
                exit()
            elif quit == 'n':
                self.run()
            else:
                print('\nPlease provide a valid input')

# ======== Menu functions ==========
    def all_items(self):
        items = self.item_repo.all()
        for item in items:
            print(item)


    def add_item_to_store(self):
        print('Add new item to shop')
        while True:
            name = input('What is the name of the item? ').title()
            while True:
                try:
                    price = float(input('How much is the item? '))
                    break
                except ValueError:
                    print('Value needs to be a floating point integer (Decimal)')

            while True:
                try:
                    stock = int(input('How much stock is available? '))
                    break
                except ValueError:
                    print('Value needs to be an integer')

            print(f'\nName: {name}, Price: {price}, Stock: {stock}\n')
            while True:
                confirmation = input('Is this correct? y/n ').lower()
                if confirmation == 'y' or confirmation == 'n':
                    break
                else:
                    print('Please enter y or n')
                    continue
            if confirmation == 'y':
                break
            

        item = Item(None, name, price, stock)
        self.item_repo.add(item)


    def add_stock_to_item(self):
        # refactor to use repo.all()
        #rows = self.connection.execute('SELECT * FROM items ORDER BY id')
        items = self.item_repo.all()

        for item in items:
            print(f"{item.id}: {item.name}")
            #print(type(row['name']))

        item_selected = input("\nPlease select an item by name or id: ")

        if item_selected.isnumeric():
            self.add_stock(items, 'id', int(item_selected))
        elif item_selected.isalpha():
            self.add_stock(items, 'name', item_selected.title())
        else:
            print('Selection was invalid')

    def add_stock(self, rows, column, item):
        for row in rows:
            if item == getattr(row, column):
                while True:
                    confirmation = input(f"Do you want to add stock to {row.name}? y/n ").lower()

                    if confirmation == 'y':
                        break
                    elif confirmation == 'n':
                        return
                    else:
                        print("\nPlease provide a valid input")
                
                additional_stock = int(input('How much stock do you want to add? '))

                if column == 'name':
                    self.connection.execute("UPDATE items SET quantity = quantity + %s WHERE name = %s", [additional_stock, item])
                else:
                    self.connection.execute("UPDATE items SET quantity = quantity + %s WHERE id = %s", [additional_stock, item])
                return
        
        print("Unable to find this item in stock")


    def all_orders(self):
        orders = self.order_repo.all()

        for order in orders:
            print(order)

    
    def make_order(self):
        #request customer name first
        while True:
            customer_query = input('Welcome customer may I take your name? ').title()

            confirmation = input(f'{customer_query}, is this correct? y/n ')

            if confirmation == 'y':
                break
            elif confirmation == 'n':
                continue
            else:
                print('Please provide a valid input')
        
        existing_customer_list = self.connection.execute('SELECT * FROM customers')

        for customer in existing_customer_list:
            if customer_query == customer['name']:
                print(f'Welcome back {customer_query}!')
                break
                
        else:
            while True:
                new_customer_query = input('Are you a new customer? y/n ')

                if new_customer_query == 'y':
                    print('Welcome new customer!')
                    self.connection.execute('INSERT INTO customers (name) VALUES (%s)', [customer_query])
                    break
                elif new_customer_query == 'n':
                    print('Sorry we have been unable to find your records')
                    return
                else:
                    print('Please provide a valid input')

        items = self.item_repo.all()
        order = {}
        total = 0

        while True:
            #list items
            while True:
                for item in items:
                    print(f"{item.id}: {item.name}, price: £{item.price:.2f}")
                
                # allow customer to select item by name or id
                item_selected = input("\nPlease select an item by name or id: ")

                if item_selected.isnumeric():
                    item_for_order = self.item_repo.find('id', int(item_selected))
                elif item_selected.isalpha():
                    item_for_order = self.item_repo.find('name', item_selected.title())
                else:
                    print('Selection was invalid')

                if item_for_order is None:
                    print('Selection was invalid')
                    return
                
                if self.confirmation(f"{item_for_order.name}, is this correct? y/n "):
                    break
                else:
                    order_more = input('Would you like to order something else? y/n')

                    if order_more == 'y':
                        continue
                    else:
                        # consider adding different else case
                        return
            
            while True:
                # select quantity
                volume_of_order = int(input(f'How many would you like to order? {item_for_order.quantity} in stock: '))
                # check there is enough in stock
                if volume_of_order > item_for_order.quantity:
                    print("There is not enough in stock to complete order")
                    continue
                else: 
                    total += volume_of_order * item_for_order.price
                    round(total, 2)
                    break

            order[item_for_order.name] = volume_of_order
            #show customer order total price
            print(f'Your basket: {order}')
            print(f'Total: £{total:.2f}')

            # ask customer for additional items
            if self.confirmation('Would you like to order something else? y/n '):
                continue
            else: 
                print(f'\nOrder for: {customer_query}')
                print(f'Your basket: {order}')
                print(f'Total: £{total:.2f}\n')
                # confirm order
                if self.confirmation('Is everything correct? y/n '):
                    print('Order confirmed')
                    break
                else:
                    print('Canceling order')
                    return
            
        
        # add order to db
        new_order = Order(None, customer_query, order, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.order_repo.make_order(new_order)
        # reduce all items by quantity
        self.item_repo.take_stock(new_order.order)

    #def find_item_for_order(self, items, column, selected)










# ========== Operations =============
    def input_valid(self, input, menu_num):
        if input == 'clear':
            return True
        
        if not input.isnumeric():
            print('Please enter an available numeric value\n')
            return False
        
        if input not in menu_num:
            print('Option invalid. Please select one of the options available\n')
            return False

        return True
    
    def confirmation(self, query):
        while True:
            confirmation = input(query)
            
            if confirmation == 'y':
                return True
            elif confirmation == 'n':
                return False
            else:
                print('Input is invalid')



if __name__ == '__main__':
    app = Application()
    app.run()