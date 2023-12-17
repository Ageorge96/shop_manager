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