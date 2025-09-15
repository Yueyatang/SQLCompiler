CREATE TABLE users (id INT, name VARCHAR(50), age INT)
INSERT INTO users VALUES (1, 'Alice', 25)
INSERT INTO users VALUES (2, 'Bob', 30)
SELECT * FROM users
SELECT name, age FROM users WHERE age > 25
UPDATE users SET age = 26 WHERE name = 'Alice'
SELECT * FROM users WHERE name = 'Alice'
DELETE FROM users WHERE age < 23
SELECT * FROM users
