# 数据库系统使用说明

## 快速开始

### 1. 安装依赖
```bash
pip install ply
```

### 2. 运行数据库
```bash
python3 main.py
```

### 3. 基本使用示例

#### 创建表
```sql
CREATE TABLE users (id INT, name VARCHAR(50), age INT)
```

#### 插入数据
```sql
INSERT INTO users VALUES (1, 'Alice', 25)
INSERT INTO users VALUES (2, 'Bob', 30)
```

#### 查询数据
```sql
SELECT * FROM users
```

#### 更新数据
```sql
UPDATE users SET age = 26 WHERE id = 1
```

#### 删除数据
```sql
DELETE FROM users WHERE age < 18
```

#### 删除表
```sql
DROP TABLE users
```

## 演示脚本

运行完整演示：
```bash
python3 demo.py
```

运行基本测试：
```bash
python3 final_test.py
```

## 交互式模式

启动交互式模式后，你可以：
- 输入SQL语句执行
- 输入 `help` 查看帮助
- 输入 `exit` 或 `quit` 退出

## 支持的功能

### 数据类型
- `INT`: 整数
- `VARCHAR(n)`: 变长字符串
- `FLOAT`: 浮点数
- `BOOLEAN`: 布尔值

### SQL语句
- `CREATE TABLE`: 创建表
- `INSERT INTO`: 插入记录
- `SELECT`: 查询数据
- `UPDATE`: 更新记录
- `DELETE`: 删除记录
- `DROP TABLE`: 删除表

### 操作符
- 比较操作符: `=`, `!=`, `<`, `<=`, `>`, `>=`
- 逻辑操作符: `AND`, `OR`, `NOT`
- 算术操作符: `+`, `-`, `*`, `/`

## 注意事项

1. 字符串值需要用单引号包围
2. 表名和列名区分大小写
3. 每个SQL语句以分号结尾（可选）
4. 数据库文件存储在 `data/` 目录中

## 故障排除

如果遇到问题：
1. 确保已安装PLY库
2. 检查SQL语法是否正确
3. 查看错误信息进行调试
4. 可以删除 `data/` 目录重新开始
