# 数据库系统 V3.0 使用指南

## 系统概述

数据库系统 V3.0 是一个完全重新设计的小型数据库系统，严格遵循《大型平台软件设计实习》要求，支持完整的SQL编译、页式存储、数据持久化和权限管理功能。

## 快速开始

### 1. 环境要求

- Python 3.8+
- 依赖包：ply (Python Lex-Yacc)

### 2. 安装依赖

```bash
pip install ply
```

### 3. 运行方式

#### 方式一：交互式模式（推荐）
```bash
cd demo
python main_v3.py
```

#### 方式二：功能演示
```bash
cd demo
python final_demo_v3.py
```

#### 方式三：组件测试
```bash
cd demo
python simple_test_v3.py
```

#### 方式四：完整测试
```bash
cd demo
python test_v3.py
```

## 详细功能说明

### 1. 交互式模式

#### 启动系统
```bash
python main_v3.py
```

#### 登录系统
系统启动后会自动提示登录：
```
请先登录:
用户名: admin
密码: admin123
```

**默认账户：**
- 用户名：`admin`
- 密码：`admin123`
- 权限：管理员（拥有所有权限）

#### 可用命令

##### SQL语句
```sql
-- 创建表
CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);

-- 插入数据
INSERT INTO tst1 VALUES (1, 'Alice', 25);
INSERT INTO tst1 VALUES (2, 'Bob', 30);
INSERT INTO tst1 VALUES (3, 'Charlie', 18);

-- 查询数据
SELECT * FROM tst1;
SELECT * FROM tst1 WHERE age > 20;
SELECT id, name FROM tst1 WHERE age < 25;

-- 更新数据
UPDATE tst1 SET age = 26 WHERE id = 1;

-- 删除数据
DELETE FROM tst1 WHERE age > 20;

-- 删除表
DROP TABLE tst1;
```

##### 系统命令
```
help     - 显示帮助信息
info     - 显示数据库信息
catalog  - 显示系统目录
users    - 显示用户列表（仅管理员）
logout   - 登出系统
exit     - 退出程序
```

### 2. 功能演示模式

#### 运行演示
```bash
python final_demo_v3.py
```

**演示内容：**
- 词法分析：显示SQL语句的token识别过程
- 语义分析：展示表结构验证和类型检查
- 存储系统：演示页面分配和数据存储
- 数据操作：模拟增删改查操作
- 查询结果：展示WHERE条件过滤
- 数据持久化：显示页面管理信息

### 3. 组件测试模式

#### 运行组件测试
```bash
python simple_test_v3.py
```

**测试内容：**
- 词法分析器测试
- 语法分析器测试
- 语义分析器测试
- 存储系统测试
- 认证系统测试

### 4. 完整测试模式

#### 运行完整测试
```bash
python test_v3.py
```

**测试流程：**
1. 登录测试
2. 创建表测试
3. 插入数据测试
4. 查询数据测试
5. 更新数据测试
6. 删除数据测试
7. 数据持久化测试

## 支持的SQL语法

### 数据定义语言 (DDL)

#### CREATE TABLE
```sql
CREATE TABLE table_name (
    column1 TYPE [constraints],
    column2 TYPE [constraints],
    ...
);
```

**支持的数据类型：**
- `INT` / `INTEGER` - 整数
- `VARCHAR(n)` - 变长字符串
- `CHAR(n)` - 定长字符串
- `FLOAT` / `DOUBLE` - 浮点数
- `BOOLEAN` / `BOOL` - 布尔值
- `DATE` - 日期
- `TIME` - 时间
- `DATETIME` - 日期时间

**支持的约束：**
- `PRIMARY KEY` - 主键
- `NOT NULL` - 非空
- `UNIQUE` - 唯一
- `DEFAULT value` - 默认值

**示例：**
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT DEFAULT 0,
    email VARCHAR(100) UNIQUE
);
```

#### DROP TABLE
```sql
DROP TABLE table_name;
```

### 数据操作语言 (DML)

#### INSERT
```sql
-- 插入所有列
INSERT INTO table_name VALUES (value1, value2, ...);

-- 插入指定列
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
```

**示例：**
```sql
INSERT INTO users VALUES (1, 'Alice', 25, 'alice@example.com');
INSERT INTO users (id, name, age) VALUES (2, 'Bob', 30);
```

#### SELECT
```sql
-- 查询所有列
SELECT * FROM table_name;

-- 查询指定列
SELECT column1, column2, ... FROM table_name;

-- 带WHERE条件
SELECT * FROM table_name WHERE condition;
```

**支持的操作符：**
- 比较：`=`, `!=`, `<>`, `<`, `<=`, `>`, `>=`
- 逻辑：`AND`, `OR`, `NOT`
- 算术：`+`, `-`, `*`, `/`, `%`

**示例：**
```sql
SELECT * FROM users WHERE age > 20;
SELECT name, email FROM users WHERE age BETWEEN 18 AND 65;
SELECT * FROM users WHERE name LIKE 'A%' AND age > 25;
```

#### UPDATE
```sql
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

**示例：**
```sql
UPDATE users SET age = 26 WHERE id = 1;
UPDATE users SET name = 'Alice Smith', email = 'alice.smith@example.com' WHERE id = 1;
```

#### DELETE
```sql
DELETE FROM table_name WHERE condition;
```

**示例：**
```sql
DELETE FROM users WHERE age < 18;
DELETE FROM users WHERE id = 1;
```

## 权限管理

### 用户类型

#### 管理员 (admin)
- 拥有所有表的全部权限
- 可以创建、删除用户
- 可以管理权限

#### 普通用户 (user)
- 只能操作自己创建的表
- 需要被授权才能操作其他用户的表

### 权限类型

- `SELECT` - 查询权限
- `INSERT` - 插入权限
- `UPDATE` - 更新权限
- `DELETE` - 删除权限
- `CREATE` - 创建表权限
- `DROP` - 删除表权限
- `ALTER` - 修改表结构权限
- `GRANT` - 授权权限

### 权限管理命令

```sql
-- 授予权限（仅管理员或表所有者）
GRANT SELECT, INSERT ON table_name TO user_id;

-- 撤销权限（仅管理员或表所有者）
REVOKE SELECT ON table_name FROM user_id;
```

## 数据持久化

### 存储结构

- **页面大小**：4KB
- **存储位置**：`data/` 目录
- **页面文件**：`page_XXXXXX.dat`
- **元数据**：`page_info.json`, `catalog.json`

### 数据恢复

系统重启后会自动：
1. 加载页面信息
2. 恢复系统目录
3. 重建用户和权限信息
4. 恢复所有表数据

## 错误处理

### 常见错误类型

#### 词法错误
```
词法错误: 非法字符 '#' 在位置 15
```

#### 语法错误
```
语法错误: 在位置 25 附近，遇到意外的token ';'
```

#### 语义错误
```
表 'users' 不存在
列 'age' 类型不匹配: 期望 int, 得到 string
```

#### 权限错误
```
权限不足：无法执行 SELECT 操作
```

#### 运行时错误
```
执行错误: 页面空间不足
```

## 性能优化

### 缓存机制

- **LRU缓存**：最近最少使用页面替换策略
- **缓存大小**：默认100个页面
- **命中统计**：显示缓存命中率

### 存储优化

- **页面预分配**：减少动态分配开销
- **批量操作**：支持批量插入和更新
- **索引支持**：为未来扩展预留接口

## 扩展功能

### 计划中的功能

1. **索引系统**：B+树索引支持
2. **事务管理**：完整的事务ACID支持
3. **并发控制**：多用户并发访问
4. **查询优化**：查询计划优化器
5. **数据类型扩展**：更多数据类型支持

### 自定义扩展

系统采用模块化设计，可以轻松扩展：
- 新的SQL语句类型
- 新的数据类型
- 新的存储引擎
- 新的权限模型

## 故障排除

### 常见问题

#### 1. 导入错误
```
ModuleNotFoundError: No module named 'ply'
```
**解决方案：**
```bash
pip install ply
```

#### 2. 权限错误
```
权限不足：无法执行操作
```
**解决方案：**
- 使用管理员账户登录
- 检查表的所有者权限
- 确认用户有相应操作权限

#### 3. 数据丢失
```
表不存在
```
**解决方案：**
- 检查数据目录是否存在
- 确认页面文件完整
- 重新创建表结构

#### 4. 性能问题
```
查询速度慢
```
**解决方案：**
- 增加缓存大小
- 优化WHERE条件
- 考虑添加索引

## 技术支持

### 日志文件

系统运行时会生成以下日志：
- `error.log` - 错误日志
- `access.log` - 访问日志
- `performance.log` - 性能日志

### 调试模式

启用调试模式：
```bash
python main_v3.py --debug
```

### 配置文件

系统配置文件：`config.json`
```json
{
    "page_size": 4096,
    "cache_size": 100,
    "data_dir": "data",
    "debug": false
}
```

## 示例场景

### 场景1：学生管理系统

```sql
-- 创建学生表
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    grade VARCHAR(10)
);

-- 插入学生数据
INSERT INTO students VALUES (1, '张三', 20, 'A');
INSERT INTO students VALUES (2, '李四', 19, 'B');
INSERT INTO students VALUES (3, '王五', 21, 'A');

-- 查询A级学生
SELECT * FROM students WHERE grade = 'A';

-- 更新学生年龄
UPDATE students SET age = 22 WHERE id = 1;

-- 删除B级学生
DELETE FROM students WHERE grade = 'B';
```

### 场景2：商品管理系统

```sql
-- 创建商品表
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price FLOAT,
    stock INT DEFAULT 0
);

-- 批量插入商品
INSERT INTO products VALUES (1, '笔记本电脑', 5999.99, 50);
INSERT INTO products VALUES (2, '手机', 2999.99, 100);
INSERT INTO products VALUES (3, '平板电脑', 3999.99, 30);

-- 查询库存不足的商品
SELECT * FROM products WHERE stock < 40;

-- 更新价格
UPDATE products SET price = price * 0.9 WHERE id = 1;

-- 删除无库存商品
DELETE FROM products WHERE stock = 0;
```

## 总结

数据库系统 V3.0 提供了完整的SQL数据库功能，包括：

✅ **完整的SQL支持**：CREATE, INSERT, SELECT, UPDATE, DELETE  
✅ **数据持久化**：程序重启后数据不丢失  
✅ **权限管理**：用户认证和权限控制  
✅ **类型安全**：严格的数据类型检查  
✅ **错误处理**：详细的错误提示  
✅ **性能优化**：LRU缓存和页面管理  

系统完全符合《大型平台软件设计实习》的所有要求，可以用于学习和研究数据库系统的核心原理。