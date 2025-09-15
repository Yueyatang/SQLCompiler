# 数据库系统 V3.0

> 完全重新设计的小型数据库系统，严格遵循《大型平台软件设计实习》要求

## 🎯 项目特点

- ✅ **完全重新设计**：从零开始构建所有核心组件
- ✅ **严格遵循要求**：完全符合Readthis.md的所有规范
- ✅ **数据持久化**：程序重启后数据完整保留
- ✅ **权限管理**：保持原有的认证和权限功能
- ✅ **完整SQL支持**：CREATE、INSERT、SELECT、DELETE等操作

## 🚀 快速开始

### 1. 安装依赖
```bash
pip install ply
```

### 2. 运行系统

#### 方式一：使用启动器（推荐）
```bash
# Windows
run.bat

# Linux/Mac
chmod +x run.sh
./run.sh
```

#### 方式二：直接运行
```bash
# 交互式模式
python main_v3.py

# 功能演示
python final_demo_v3.py

# 组件测试
python simple_test_v3.py

# 完整测试
python test_v3.py
```

### 3. 登录系统
- **用户名**：`admin`
- **密码**：`admin123`

## 📋 验证您的示例

运行以下命令验证系统功能：

```bash
python final_demo_v3.py
```

**您的示例SQL执行结果：**

```sql
CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);
INSERT INTO tst1 VALUES (1, 'Alice', 25);
SELECT * FROM tst1 WHERE age > 20;
-- 结果: 1, 'Alice', 25

DELETE FROM tst1 WHERE age > 20;
-- 结果: Alice那条记录被成功删除
```

## 🏗️ 系统架构

### 核心组件

1. **SQL编译器** (`compiler/`)
   - 词法分析器：识别SQL关键字和操作符
   - 语法分析器：构建抽象语法树(AST)
   - 语义分析器：类型检查和表结构验证
   - 执行计划生成：将AST转换为执行计划

2. **存储系统** (`storage/`)
   - 页式存储：4KB页面大小
   - LRU缓存：提升访问效率
   - 数据持久化：文件系统存储

3. **执行引擎** (`engine/`)
   - 查询执行：SELECT、INSERT、UPDATE、DELETE
   - 记录管理：序列化/反序列化
   - 条件评估：WHERE条件处理

4. **权限管理** (`auth/`)
   - 用户认证：登录/登出系统
   - 权限控制：表级权限管理
   - 会话管理：用户会话维护

## 📚 文档

- [快速开始指南](QUICK_START.md) - 5分钟快速体验
- [详细使用指南](USAGE_GUIDE_V3.md) - 完整功能说明
- [项目总结](PROJECT_SUMMARY_V3.md) - 技术实现细节

## 🎮 运行模式

### 1. 交互式模式（推荐新手）
```bash
python main_v3.py
```
- 完整的SQL交互界面
- 实时错误提示
- 用户友好的命令提示

### 2. 功能演示（推荐学习）
```bash
python final_demo_v3.py
```
- 展示所有核心功能
- 详细的执行过程
- 完整的示例演示

### 3. 组件测试（推荐开发）
```bash
python simple_test_v3.py
```
- 测试各个组件功能
- 快速验证系统状态
- 调试和开发辅助

### 4. 完整测试（推荐验证）
```bash
python test_v3.py
```
- 完整的测试套件
- 数据持久化验证
- 系统稳定性测试

## 💡 支持的SQL语法

### 数据定义语言 (DDL)
```sql
-- 创建表
CREATE TABLE table_name (
    column1 TYPE [constraints],
    column2 TYPE [constraints],
    ...
);

-- 删除表
DROP TABLE table_name;
```

### 数据操作语言 (DML)
```sql
-- 插入数据
INSERT INTO table_name VALUES (value1, value2, ...);
INSERT INTO table_name (col1, col2) VALUES (val1, val2);

-- 查询数据
SELECT * FROM table_name;
SELECT col1, col2 FROM table_name WHERE condition;

-- 更新数据
UPDATE table_name SET col = value WHERE condition;

-- 删除数据
DELETE FROM table_name WHERE condition;
```

### 支持的数据类型
- `INT` / `INTEGER` - 整数
- `VARCHAR(n)` - 变长字符串
- `CHAR(n)` - 定长字符串
- `FLOAT` / `DOUBLE` - 浮点数
- `BOOLEAN` / `BOOL` - 布尔值

### 支持的操作符
- 比较：`=`, `!=`, `<>`, `<`, `<=`, `>`, `>=`
- 逻辑：`AND`, `OR`, `NOT`
- 算术：`+`, `-`, `*`, `/`, `%`

## 🔐 权限管理

### 用户类型
- **管理员** (`admin`)：拥有所有权限
- **普通用户** (`user`)：只能操作自己的表

### 权限类型
- `SELECT` - 查询权限
- `INSERT` - 插入权限
- `UPDATE` - 更新权限
- `DELETE` - 删除权限
- `CREATE` - 创建表权限
- `DROP` - 删除表权限

## 📊 系统要求

- **Python版本**：3.8+
- **依赖包**：ply (Python Lex-Yacc)
- **操作系统**：Windows、Linux、macOS
- **内存要求**：最少512MB
- **磁盘空间**：最少100MB

## 🎯 核心特性

### 1. 编译原理应用
- 词法分析：使用PLY库实现SQL词法分析
- 语法分析：构建完整的抽象语法树
- 语义分析：实现类型检查和语义验证
- 执行计划：将AST转换为可执行的逻辑计划

### 2. 操作系统知识应用
- 文件系统：页面文件的创建、读写、删除
- 内存管理：LRU页面缓存算法
- 存储管理：页式存储模型设计

### 3. 数据库知识应用
- 存储引擎：页面式存储管理
- 查询处理：SQL语句的解析和执行
- 事务管理：基本的ACID属性
- 权限控制：完整的用户权限系统

## 🚨 故障排除

### 常见问题

1. **导入错误**
   ```
   ModuleNotFoundError: No module named 'ply'
   ```
   **解决方案**：`pip install ply`

2. **权限错误**
   ```
   权限不足：无法执行操作
   ```
   **解决方案**：使用管理员账户登录

3. **数据丢失**
   ```
   表不存在
   ```
   **解决方案**：检查数据目录完整性

## 📈 性能特点

- **页面缓存**：LRU算法，默认100个页面
- **存储优化**：4KB页面大小，减少I/O开销
- **内存管理**：智能缓存替换策略
- **数据持久化**：程序重启后数据完整保留

## 🔮 未来扩展

- 索引系统：B+树索引支持
- 事务管理：完整的事务ACID支持
- 并发控制：多用户并发访问
- 查询优化：查询计划优化器
- 数据类型扩展：更多数据类型支持

## 📞 技术支持

- 查看详细文档：`USAGE_GUIDE_V3.md`
- 查看项目总结：`PROJECT_SUMMARY_V3.md`
- 运行帮助命令：在交互模式中输入 `help`

## 🎉 成功验证

如果看到以下输出，说明系统运行正常：

```
✅ 词法分析成功，识别到 17 个token
✅ 语义分析成功
✅ 页面分配成功
✅ 数据写入成功
✅ 查询结果: 1, 'Alice', 25
✅ 删除操作成功
```

---

**恭喜！您已经成功运行了数据库系统 V3.0！** 🎊

系统完全符合您的要求，能够正确处理您提到的所有SQL操作，同时保持了原有的权限管理功能。所有组件都经过了测试验证，确保功能的正确性和稳定性。