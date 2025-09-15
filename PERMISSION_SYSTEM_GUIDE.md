# 权限系统使用指南

## 🎯 功能概述

您的数据库系统现在已经集成了完整的权限管理功能，包括：

- ✅ 用户认证（登录/登出）
- ✅ 用户管理（创建用户、角色管理）
- ✅ 权限控制（表级权限管理）
- ✅ 会话管理（安全的用户状态管理）

## 🚀 快速开始

### 1. 启动系统
```bash
cd "C:\Users\19655\Desktop\SQLCompiler2.0\SQLCompiler2.0\demo"
python main.py
```

### 2. 默认管理员账户
- **用户名**: `admin`
- **密码**: `admin123`

## 📋 支持的SQL命令

### 认证命令
```sql
-- 登录
LOGIN username 'password'

-- 登出
LOGOUT

-- 修改密码
CHANGE PASSWORD 'old_password' TO 'new_password'
```

### 用户管理（仅管理员）
```sql
-- 创建用户
CREATE USER username 'password' ROLE role

-- 查看用户列表
SHOW USERS
```

### 权限管理
```sql
-- 授权权限
GRANT permission1, permission2 ON table_name TO username

-- 撤销权限
REVOKE permission1, permission2 ON table_name FROM username

-- 查看用户权限
SHOW GRANTS FOR username
```

### 数据操作（需要相应权限）
```sql
-- 创建表
CREATE TABLE table_name (column1 TYPE, column2 TYPE, ...)

-- 插入数据
INSERT INTO table_name VALUES (value1, value2, ...)

-- 查询数据
SELECT * FROM table_name
SELECT column1, column2 FROM table_name WHERE condition

-- 更新数据
UPDATE table_name SET column = value WHERE condition

-- 删除数据
DELETE FROM table_name WHERE condition

-- 删除表
DROP TABLE table_name
```

## 🔐 权限类型

| 权限 | 描述 | 适用操作 |
|------|------|----------|
| SELECT | 查询权限 | SELECT语句 |
| INSERT | 插入权限 | INSERT语句 |
| UPDATE | 更新权限 | UPDATE语句 |
| DELETE | 删除权限 | DELETE语句 |
| CREATE | 创建表权限 | CREATE TABLE语句 |
| DROP | 删除表权限 | DROP TABLE语句 |
| GRANT | 授权权限 | GRANT/REVOKE语句 |

## 👥 用户角色

### 管理员 (admin)
- 拥有所有权限
- 可以创建和管理其他用户
- 可以授予和撤销权限
- 可以查看所有用户信息

### 普通用户 (user)
- 默认没有任何权限
- 需要管理员显式授权
- 只能访问被授权的表

## 📝 使用示例

### 1. 基本工作流程
```sql
-- 1. 登录管理员
LOGIN admin 'admin123'

-- 2. 创建普通用户
CREATE USER alice 'password123' ROLE user

-- 3. 创建表
CREATE TABLE users (id INT, name VARCHAR(50), age INT)

-- 4. 授权权限
GRANT SELECT, INSERT ON users TO alice

-- 5. 登出管理员
LOGOUT

-- 6. 以alice身份登录
LOGIN alice 'password123'

-- 7. 执行操作
INSERT INTO users VALUES (1, 'Alice', 25)
SELECT * FROM users

-- 8. 登出
LOGOUT
```

### 2. 权限管理示例
```sql
-- 查看用户列表
SHOW USERS

-- 查看用户权限
SHOW GRANTS FOR alice

-- 撤销权限
REVOKE INSERT ON users FROM alice

-- 再次查看权限
SHOW GRANTS FOR alice
```

## ⚠️ 注意事项

1. **密码安全**: 密码需要用单引号包围
2. **权限检查**: 所有数据操作都需要相应的权限
3. **会话管理**: 系统会自动管理用户会话状态
4. **表所有者**: 创建表的用户自动成为表的所有者
5. **权限继承**: 表所有者自动拥有该表的所有权限

## 🔧 系统特性

### 安全特性
- 密码哈希存储（SHA-256 + 盐）
- 会话令牌管理
- 权限验证机制
- 操作审计日志

### 管理特性
- 用户角色管理
- 细粒度权限控制
- 权限查询和统计
- 用户状态管理

## 🐛 故障排除

### 常见问题

1. **登录失败**
   - 检查用户名和密码是否正确
   - 确保密码用单引号包围

2. **权限不足**
   - 确认已登录
   - 检查是否有相应权限
   - 联系管理员授权

3. **语法错误**
   - 检查SQL语句格式
   - 确保关键字拼写正确
   - 注意引号使用

### 调试命令
```sql
-- 查看当前用户
-- (系统会自动显示在提示符中)

-- 查看帮助
help
```

## 🎉 总结

您的数据库系统现在具备了企业级的权限管理功能！可以安全地管理多用户环境，实现细粒度的数据访问控制。

开始使用吧！🚀
