from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.order_repository import OrderRepository

class Application:

    def __init__(self):
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.connection.seed('seeds/shop_test_table.sql')
        self.item_repo = ItemRepository(self.connection)
        self.order_repo = OrderRepository(self.connection)

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
                items = self.item_repo.all()
                for item in items:
                    print(item)
            case '2':
                print('4')
            case '3':
                pass
            case '4':
                print('5')
            case '5':
                pass



    def input_valid(self, input, menu_num):
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