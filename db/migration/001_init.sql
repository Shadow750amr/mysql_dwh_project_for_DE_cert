
---MYSQL
CREATE DATABASE sales;

USE sales;

--- at his point the sales.sql is executed so all the rest of the tables can be created.

---POSTGRESQL

CREATE TABLE sales_data (
    rowid INT NOT NULL,
    product_id INT,
    customer_id INT,
    price DECIMAL,
    quantity INT,
    timestamp timestamp
)

