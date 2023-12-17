from datetime import datetime
from lib.order_repository import OrderRepository, Order

def test_get_all_orders(db_connection):
    db_connection.seed('seeds/shop_test_table.sql')
    repo = OrderRepository(db_connection)

    orders = repo.all()
    assert orders == [
        Order(1, 'Andre', {"Strawberries": 2, "Milk": 2, "Eggs (pack of 6)": 1}, datetime.strptime('20230423 12:32:00', '%Y%m%d %H:%M:%S')),
        Order(2, 'Charlie', {"Honey": 1, "Mango": 4, "Oat Milk": 3, "Salt": 1}, datetime.strptime('20230426 11:24:24', '%Y%m%d %H:%M:%S')),
        Order(3, 'Daniel', {"Rice": 1}, datetime.strptime('20230502 17:11:23', '%Y%m%d %H:%M:%S')),
        Order(4, 'Billy', {"Baked Beans": 6, "Eggs (pack of 6)": 2}, datetime.strptime('20230623 11:11:11', '%Y%m%d %H:%M:%S')),
        Order(5, 'Emilia', {"Milk": 1, "Oat Milk": 2}, datetime.strptime('20230629 15:13:12', '%Y%m%d %H:%M:%S')),
        Order(6, 'Faith', {"Salt": 2, "Pepper": 3}, datetime.strptime('20230423 19:24:01', '%Y%m%d %H:%M:%S')),
        Order(7, 'Andre', {"Honey": 3, "Milk": 2}, datetime.strptime('20230728 14:10:55', '%Y%m%d %H:%M:%S')),
        Order(8, 'Daniel', {"Baked Beans": 5, "Milk": 2, "Strawberries": 3}, datetime.strptime('20230801 10:44:09', '%Y%m%d %H:%M:%S')),
        Order(9, 'Georgina', {"Mango": 6}, datetime.strptime('20230812 13:53:42', '%Y%m%d %H:%M:%S')),
        Order(10, 'Billy', {"Salt": 2, "Rice": 1}, datetime.strptime('20230820 09:38:14', '%Y%m%d %H:%M:%S')),
        Order(11, 'Andre', {"Strawberries": 1, "Eggs (pack of 6)": 4}, datetime.strptime('20230918 15:21:53', '%Y%m%d %H:%M:%S'))
    ]


def test_make_order(db_connection):
    db_connection.seed('seeds/shop_test_table.sql')
    repo = OrderRepository(db_connection)

    repo.make_order(Order(None, 'Faith', {'Rice': 2, "Eggs (pack of 6)": 3}, datetime(2023, 11, 5, 21, 41, 11)))

    orders = repo.all()
    assert orders == [
        Order(1, 'Andre', {"Strawberries": 2, "Milk": 2, "Eggs (pack of 6)": 1}, datetime.strptime('20230423 12:32:00', '%Y%m%d %H:%M:%S')),
        Order(2, 'Charlie', {"Honey": 1, "Mango": 4, "Oat Milk": 3, "Salt": 1}, datetime.strptime('20230426 11:24:24', '%Y%m%d %H:%M:%S')),
        Order(3, 'Daniel', {"Rice": 1}, datetime.strptime('20230502 17:11:23', '%Y%m%d %H:%M:%S')),
        Order(4, 'Billy', {"Baked Beans": 6, "Eggs (pack of 6)": 2}, datetime.strptime('20230623 11:11:11', '%Y%m%d %H:%M:%S')),
        Order(5, 'Emilia', {"Milk": 1, "Oat Milk": 2}, datetime.strptime('20230629 15:13:12', '%Y%m%d %H:%M:%S')),
        Order(6, 'Faith', {"Salt": 2, "Pepper": 3}, datetime.strptime('20230423 19:24:01', '%Y%m%d %H:%M:%S')),
        Order(7, 'Andre', {"Honey": 3, "Milk": 2}, datetime.strptime('20230728 14:10:55', '%Y%m%d %H:%M:%S')),
        Order(8, 'Daniel', {"Baked Beans": 5, "Milk": 2, "Strawberries": 3}, datetime.strptime('20230801 10:44:09', '%Y%m%d %H:%M:%S')),
        Order(9, 'Georgina', {"Mango": 6}, datetime.strptime('20230812 13:53:42', '%Y%m%d %H:%M:%S')),
        Order(10, 'Billy', {"Salt": 2, "Rice": 1}, datetime.strptime('20230820 09:38:14', '%Y%m%d %H:%M:%S')),
        Order(11, 'Andre', {"Strawberries": 1, "Eggs (pack of 6)": 4}, datetime.strptime('20230918 15:21:53', '%Y%m%d %H:%M:%S')),
        Order(12, 'Faith', {'Rice': 2, "Eggs (pack of 6)": 3}, datetime(2023, 11, 5, 21, 41, 11))
    ]
    