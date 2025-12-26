CREATE DATABASE python_db;
USE python_db;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
SELECT * FROM users;
INSERT INTO users (name,email) values("bhavesh","bhk@gmail.com");
ALTER TABLE users
ADD COLUMN password VARCHAR(100) NOT NULL;
#this is from table auto query when direct apply on show result-- 
UPDATE `python_db`.`users` SET `password` = '1234' WHERE (`id` = '1');
UPDATE users set password = 5678 where id = 1;