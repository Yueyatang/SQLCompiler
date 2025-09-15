-- 小型数据库系统测试脚本
-- 演示增删改查操作

-- 1. 创建表 (CREATE)
CREATE TABLE users (id INT, name VARCHAR(50), age INT, email VARCHAR(100));

-- 2. 插入数据 (INSERT)
INSERT INTO users VALUES (1, 'Alice', 25, 'alice@example.com');
INSERT INTO users VALUES (2, 'Bob', 30, 'bob@example.com');
INSERT INTO users VALUES (3, 'Charlie', 22, 'charlie@example.com');
INSERT INTO users VALUES (4, 'Diana', 28, 'diana@example.com');

-- 3. 查询数据 (SELECT)
SELECT * FROM users;
SELECT name, age FROM users WHERE age > 25;
SELECT * FROM users WHERE name = 'Alice';

-- 4. 更新数据 (UPDATE)
UPDATE users SET age = 26 WHERE name = 'Alice';
UPDATE users SET email = 'alice.new@example.com' WHERE id = 1;

-- 5. 再次查询验证更新
SELECT * FROM users WHERE name = 'Alice';

-- 6. 删除数据 (DELETE)
DELETE FROM users WHERE age < 23;

-- 7. 最终查询结果
SELECT * FROM users;

-- 8. 删除表 (DROP)
-- DROP TABLE users;
