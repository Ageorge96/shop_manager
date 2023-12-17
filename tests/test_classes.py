from lib.customer import Customer
from lib.item import Item
from lib.order import Order


# ======= Customer tests========
def test_customer():
    customer = Customer(1, 'Andre')
    assert customer.name == 'Andre'

def test_add_order():
    customer = Customer(1, 'Megan')
    customer.add_order(2)
    assert customer.order == [2]
    customer.add_order(6)
    assert customer.order == [2, 6]


# ======= Item tests ========

def test_item():
    item = Item(2, 'ham', 1.29, 20)
    assert item.name == 'ham'
    assert item.price == 1.29
    assert item.quantity == 20

def test_item_add():
    item = Item(2, 'ham', 1.29, 20)
    item.add_stock(5)
    assert item.quantity == 25

def test_item_reduce():
    item = Item(2, 'ham', 1.29, 20)
    item.reduce_stock(5)
    assert item.quantity == 15