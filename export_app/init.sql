CREATE SCHEMA IF NOT EXISTS development;
CREATE TABLE IF NOT EXISTS development.products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL
);
INSERT INTO development.products (product_name) VALUES 
('Premium Dashboard Tool'), 
('Automated Exporter Script'), 
('Postgres Sync Connector'), 
('Data Logger Appliance');