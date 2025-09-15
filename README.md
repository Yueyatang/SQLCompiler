# 小型数据库系统

这是一个分步构建的数据库系统项目，包含以下三个主要部分：

## 项目结构

### 1. SQL编译器 (compiler/)
- **词法分析器** (lexer.py): 将SQL语句分解为token
- **语法分析器** (parser.py): 构建抽象语法树(AST)
- **语义分析器** (semantic.py): 进行类型检查和语义验证

### 2. 存储系统 (storage/)
- **存储管理器** (storage_manager.py): 管理数据文件的创建、删除和访问
- **页面管理器** (page_manager.py): 管理数据页面的分配和回收
- **缓冲区管理器** (buffer_manager.py): 实现LRU缓存机制

### 3. 数据库引擎 (engine/)
- **查询执行器** (query_executor.py): 执行SQL查询计划
- **事务管理器** (transaction_manager.py): 管理事务的ACID属性
- **索引系统** (index_manager.py): 实现B+树索引

## 技术栈

- **语言**: Python 3.8+
- **依赖**: 
  - ply (Python Lex-Yacc) - 用于词法和语法分析
  - struct - 用于二进制数据序列化
  - os, io - 用于文件系统操作

## 安装和运行

```bash
# 安装依赖
pip install ply

# 运行数据库
python main.py
```

## 支持的SQL语句

- CREATE TABLE
- INSERT INTO
- SELECT
- UPDATE
- DELETE
- DROP TABLE

## 示例

```sql
-- 创建表
CREATE TABLE users (id INT, name VARCHAR(50), age INT);

-- 插入数据
INSERT INTO users VALUES (1, 'Alice', 25);

-- 查询数据
SELECT * FROM users WHERE age > 20;
```
