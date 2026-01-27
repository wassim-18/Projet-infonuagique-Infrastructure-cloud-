```sql
CREATE DATABASE ecommerce;
USE ecommerce;

CREATE TABLE clients (
  client_id INT AUTO_INCREMENT PRIMARY KEY,
  client_fname VARCHAR(50),
  client_lname VARCHAR(50),
  client_email VARCHAR(100)
);

INSERT INTO clients (client_fname, client_lname, client_email) VALUES
('Ali','Ben Salah','ali@gmail.com'),
('Sara','Trabelsi','sara@yahoo.com'),
('Wassim','Younes','wassim@hotmail.com'),
('Nour','Mejri','nour@gmail.com');
