DROP TABLE IF EXISTS items;
DROP SEQUENCE IF EXISTS item_id_seq;
DROP TABLE IF EXISTS customers CASCADE;
DROP SEQUENCE IF EXISTS customer_id_seq;
DROP TABLE IF EXISTS orders;
DROP SEQUENCE IF EXISTS order_id_seq;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    price FLOAT,
    quantity SMALLINT
);

CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	name VARCHAR(35)
);

CREATE TABLE orders (
	id SERIAL PRIMARY KEY,
	item_id TEXT,
	item_quantity TEXT,
	order_time TIMESTAMP,
	customer_id INT,
	CONSTRAINT fk_customer FOREIGN KEY (customer_id)
		REFERENCES customers(id)
		ON DELETE CASCADE
);


INSERT INTO items (name, price, quantity) VALUES 
    ('Honey', 2.89, 50), --1
	('Strawberries', 1.69, 37), --2
	('Mango', 1.20, 29), --3
	('Milk', 2.19, 40), --4
	('Oat Milk', 1.89, 28), --5
	('Salt', 1.70, 21), --6
	('Pepper', 1.30, 18), --7
	('Rice', 5.79, 14), --8
	('Eggs (pack of 6)', 3.10, 23), --9
	('Baked Beans', 1.89, 38); --10

INSERT INTO customers (name) VALUES 
    ('Andre'),
	('Billy'),
	('Charlie'),
	('Daniel'),
	('Emilia'),
	('Faith'),
	('Georgina');

INSERT INTO orders (item_id, item_quantity, order_time, customer_id) VALUES
    ('2, 4, 9', '2, 2, 1', '20230423 12:32:00', 1), --1
	('1, 3, 5, 6', '1, 4, 3, 1', '20230426 11:24:24', 3), --2
	('8', '1', '20230502 17:11:23', 4), --3
	('10, 9', '6, 2', '20230623 11:11:11', 2), --4
	('4, 5', '1, 2', '20230629 15:13:12', 5), --5
	('6, 7', '2, 3', '20230423 19:24:01', 6), --6
	('1, 4', '3, 2', '20230728 14:10:55', 1), --7
	('10, 4, 2', '5, 2, 3', '20230801 10:44:09', 4), --8
	('3', '6', '20230812 13:53:42', 7), --9
	('6, 8', '2, 1', '20230820 09:38:14', 2), --10
	('2, 9', '1, 4', '20230918 15:21:53', 1); --11