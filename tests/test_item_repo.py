from lib.item_repository import ItemRepository, Item

def test_get_all_items(db_connection):
    db_connection.seed('seeds/shop_test_table.sql')
    repo = ItemRepository(db_connection)
    
    items = repo.all()
    assert items == [
        Item(1, 'Honey', 2.89, 50),
	    Item(2, 'Strawberries', 1.69, 37), 
	    Item(3, 'Mango', 1.20, 29), 
	    Item(4, 'Milk', 2.19, 40), 
	    Item(5, 'Oat Milk', 1.89, 28),
	    Item(6, 'Salt', 1.70, 21), 
	    Item(7, 'Pepper', 1.30, 18), 
	    Item(8, 'Rice', 5.79, 14),
	    Item(9, 'Eggs (pack of 6)', 3.10, 23), 
	    Item(10, 'Baked Beans', 1.89, 38)
    ]

def test_add_item(db_connection):
    db_connection.seed('seeds/shop_test_table.sql')
    repo = ItemRepository(db_connection)
    item_1 = Item(None, 'Ham', 1.29, 20)
    item_2 = Item(None, 'Butter', 1.79, 14)
    item_3 = Item(None, 'Cheese', 2.19, 10)

    repo.add(item_1)
    repo.add(item_2)
    repo.add(item_3)

    items = repo.all()
    assert items == [
        Item(1, 'Honey', 2.89, 50),
	    Item(2, 'Strawberries', 1.69, 37), 
	    Item(3, 'Mango', 1.20, 29), 
	    Item(4, 'Milk', 2.19, 40), 
	    Item(5, 'Oat Milk', 1.89, 28),
	    Item(6, 'Salt', 1.70, 21), 
	    Item(7, 'Pepper', 1.30, 18), 
	    Item(8, 'Rice', 5.79, 14),
	    Item(9, 'Eggs (pack of 6)', 3.10, 23), 
	    Item(10, 'Baked Beans', 1.89, 38),
        Item(11, 'Ham', 1.29, 20),
        Item(12, 'Butter', 1.79, 14),
        Item(13, 'Cheese', 2.19, 10)
    ]


    