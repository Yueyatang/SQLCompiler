# 权限系统手动验证指南

## 🚀 启动系统
```bash
cd "C:\Users\19655\Desktop\SQLCompiler2.0\SQLCompiler2.0\demo"
python main.py
```

## 📋 验证步骤

### 步骤 1: 基本认证功能
```sql
-- 1.1 测试未登录状态（应该失败）
SELECT * FROM test_table

-- 1.2 管理员登录
LOGIN admin 'admin123'

-- 1.3 查看用户列表
SHOW USERS

-- 1.4 登出
LOGOUT
```

### 步骤 2: 数据操作功能
```sql
-- 2.1 重新登录
LOGIN admin 'admin123'

-- 2.2 创建表
CREATE TABLE employees (id INT, name VARCHAR(50), salary FLOAT)

-- 2.3 插入数据
INSERT INTO employees VALUES (1, 'Alice', 50000.0)
INSERT INTO employees VALUES (2, 'Bob', 60000.0)

-- 2.4 查询数据
SELECT * FROM employees
SELECT name, salary FROM employees WHERE salary > 55000

-- 2.5 更新数据
UPDATE employees SET salary = 55000.0 WHERE name = 'Alice'

-- 2.6 删除数据
DELETE FROM employees WHERE salary < 55000

-- 2.7 再次查询
SELECT * FROM employees
```

### 步骤 3: 权限控制功能
```sql
-- 3.1 登出
LOGOUT

-- 3.2 尝试未登录操作（应该失败）
SELECT * FROM employees
INSERT INTO employees VALUES (3, 'Charlie', 70000.0)
UPDATE employees SET salary = 80000.0 WHERE id = 1
DELETE FROM employees WHERE id = 1

-- 3.3 重新登录
LOGIN admin 'admin123'

-- 3.4 验证登录后可以操作
SELECT * FROM employees
```

### 步骤 4: 会话管理功能
```sql
-- 4.1 登出
LOGOUT

-- 4.2 尝试操作（应该失败）
SELECT * FROM employees

-- 4.3 重新登录
LOGIN admin 'admin123'

-- 4.4 验证可以操作
SELECT * FROM employees
```

### 步骤 5: 表管理功能
```sql
-- 5.1 创建多个表
CREATE TABLE departments (id INT, name VARCHAR(50))
CREATE TABLE projects (id INT, name VARCHAR(100), budget FLOAT)

-- 5.2 插入数据
INSERT INTO departments VALUES (1, 'Engineering')
INSERT INTO departments VALUES (2, 'Marketing')
INSERT INTO projects VALUES (1, 'Website Redesign', 50000.0)

-- 5.3 查询数据
SELECT * FROM departments
SELECT * FROM projects

-- 5.4 删除表
DROP TABLE projects
DROP TABLE departments
DROP TABLE employees
```

## ✅ 预期结果

### 成功的情况
- 登录成功: `登录成功! 欢迎, admin`
- 表创建: `表 'table_name' 创建成功`
- 数据插入: `成功插入1条记录到表 'table_name'`
- 查询结果: 显示实际数据
- 登出成功: `已成功登出`

### 失败的情况（符合预期）
- 未登录操作: `错误: 请先登录 (使用 LOGIN username password)`
- 权限不足: `错误: 权限不足，无法执行此操作`

## 🔍 验证要点

1. **认证功能**
   - ✅ 可以正常登录
   - ✅ 可以正常登出
   - ✅ 未登录时操作被拒绝

2. **数据操作功能**
   - ✅ 可以创建表
   - ✅ 可以插入数据
   - ✅ 可以查询数据
   - ✅ 可以更新数据
   - ✅ 可以删除数据
   - ✅ 可以删除表

3. **权限控制功能**
   - ✅ 未登录时无法操作
   - ✅ 登录后可以操作
   - ✅ 登出后无法操作

4. **会话管理功能**
   - ✅ 会话状态正确维护
   - ✅ 登出后会话失效

## 🎯 快速验证命令

如果您想快速验证，可以复制粘贴以下命令序列：

```sql
LOGIN admin 'admin123'
CREATE TABLE test (id INT, name VARCHAR(50))
INSERT INTO test VALUES (1, 'test')
SELECT * FROM test
LOGOUT
SELECT * FROM test
LOGIN admin 'admin123'
SELECT * FROM test
DROP TABLE test
LOGOUT
```

这个序列应该显示：
1. 登录成功
2. 表创建成功
3. 数据插入成功
4. 查询显示数据
5. 登出成功
6. 查询失败（权限控制）
7. 重新登录成功
8. 查询成功
9. 表删除成功
10. 登出成功
