CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL
);

INSERT INTO products (name, description, price) VALUES
('Acme Widget A', 'High-quality widget for business use.', 19.99),
('Acme Widget B', 'Advanced widget with premium features.', 29.99),
('Acme Widget C', 'Affordable widget for everyday tasks.', 9.99); 