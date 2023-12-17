As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed. 

As a shop manager
So I can manage orders
I want to be able to create a new order.



Welcome to the shop management program!

What do you want to do?
  1 = list all shop items
  2 = create a new item
  3 = list all orders
  4 = create a new order

1 [enter]

Here's a list of all shop items:

 #1 Super Shark Vacuum Cleaner - Unit price: 99 - Quantity: 30
 #2 Makerspresso Coffee Machine - Unit price: 69 - Quantity: 15
 (...)


nouns:
items
name
price
quantity (stock)
orders
customers
date


verbs:
create new item
list item names and prices
create new order


## Classes

class Item:
    parameters:
        id: int - item id
        name: string - the name of the item
        price: float - the prices of the item
        quantity: int - the total stock of the item


class Customer:
    parameters:
        id: int - customer id
        name: string - the name of the customer
        orders: [int] - list of orders


class Order:
    parameters:
        id: int - order id
        order: dict<Item[name]: item[quantity]> - a dict for the item order and how many
        date: datetime - the date the order was made


## Database

table: items
id: serial
name: sting
price: float
quantity: int


table: customers
id: serial
name: string


table: orders
id: serial
order_item: string
item_quantity: int
date: datetime
customer_id: int
