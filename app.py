from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository, Item
from lib.order_repository import OrderRepository, Order

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
                print('5')
            case '5':
                pass
            case 'clear':
                self.connection.seed('seeds/clear_shop.sql')
            
        self.exit_program()

    def exit_program(self):
        while True:
            quit = input('\nDo you want to exit Shop Manager? ').lower()

            if quit == 'y':
                exit()
            elif quit == 'n':
                self.run()
            else:
                print('\nPlease provide a valid input\n')

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
        rows = self.connection.execute('SELECT * FROM items ORDER BY id')

        for row in rows:
            print(f"{row['id']}: {row['name']}")
            #print(type(row['name']))

        item_selected = input("\nPlease select an item by name or id: ")

        if item_selected.isnumeric():
            self.add_stock(rows, 'id', int(item_selected))

        elif item_selected.isalpha():
            self.add_stock(rows, 'name', item_selected.title())

    def add_stock(self, rows, column, item):
        for row in rows:
            if item == row[column]:
                while True:
                    confirmation = input(f"Do you want to add stock to {row['name']}? y/n ").lower()

                    if confirmation == 'y':
                        break
                    elif confirmation == 'n':
                        return
                    else:
                        print("\nPlease provide a valid input")
                
                additional_stock = int(input('How much stock do you want to add? '))
                print(column)
                print(item)

                
                if column == 'name':
                    self.connection.execute("UPDATE items SET quantity = quantity + %s WHERE name = %s", [additional_stock, item])
                else:
                    self.connection.execute("UPDATE items SET quantity = quantity + %s WHERE id = %s", [additional_stock, item])
                return






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



if __name__ == '__main__':
    app = Application()
    app.run()