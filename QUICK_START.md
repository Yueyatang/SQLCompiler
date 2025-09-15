# 数据库系统 V3.0 快速开始指南

## 🚀 5分钟快速体验

### 1. 安装依赖
```bash
pip install ply
```

### 2. 运行系统

#### Windows用户
```bash
cd demo
run.bat
```

#### Linux/Mac用户
```bash
cd demo
chmod +x run.sh
./run.sh
```

#### 或者直接运行
```bash
cd demo
python main_v3.py
```

### 3. 登录系统
- 用户名：`admin`
- 密码：`admin123`

### 4. 执行示例SQL

```sql
-- 创建表
CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);

-- 插入数据
INSERT INTO tst1 VALUES (1, 'Alice', 25);
INSERT INTO tst1 VALUES (2, 'Bob', 30);
INSERT INTO tst1 VALUES (3, 'Charlie', 18);

-- 查询数据
SELECT * FROM tst1 WHERE age > 20;

-- 删除数据
DELETE FROM tst1 WHERE age > 20;

-- 查看结果
SELECT * FROM tst1;
```

## 📋 运行模式说明

### 1. 交互式模式 (推荐新手)
```bash
python main_v3.py
```
- 完整的SQL交互界面
- 实时错误提示
- 用户友好的命令提示

### 2. 功能演示 (推荐学习)
```bash
python final_demo_v3.py
```
- 展示所有核心功能
- 详细的执行过程
- 完整的示例演示

### 3. 组件测试 (推荐开发)
```bash
python simple_test_v3.py
```
- 测试各个组件功能
- 快速验证系统状态
- 调试和开发辅助

### 4. 完整测试 (推荐验证)
```bash
python test_v3.py
```
- 完整的测试套件
- 数据持久化验证
- 系统稳定性测试

## 🎯 核心功能验证

### 验证您的示例SQL

运行以下命令验证系统功能：

```bash
python final_demo_v3.py
```

您将看到：
1. ✅ 词法分析：识别17个token
2. ✅ 语义分析：表结构验证通过
3. ✅ 存储系统：页面分配成功
4. ✅ 数据操作：3条记录插入成功
5. ✅ 查询结果：`1, 'Alice', 25` 和 `2, 'Bob', 30`
6. ✅ 删除操作：删除2条记录，剩余 `3, 'Charlie', 18`

## 🔧 常用命令

### 系统命令
```
help     - 显示帮助
info     - 数据库信息
catalog  - 系统目录
users    - 用户列表
logout   - 登出
exit     - 退出
```

### SQL命令
```sql
-- 创建表
CREATE TABLE table_name (col1 TYPE, col2 TYPE);

-- 插入数据
INSERT INTO table_name VALUES (val1, val2);

-- 查询数据
SELECT * FROM table_name WHERE condition;

-- 更新数据
UPDATE table_name SET col = val WHERE condition;

-- 删除数据
DELETE FROM table_name WHERE condition;
```

## 📁 文件结构

```
demo/
├── main_v3.py              # 主程序
├── final_demo_v3.py        # 功能演示
├── simple_test_v3.py       # 组件测试
├── test_v3.py              # 完整测试
├── run.bat                 # Windows启动器
├── run.sh                  # Linux/Mac启动器
├── USAGE_GUIDE_V3.md       # 详细使用指南
├── QUICK_START.md          # 快速开始指南
├── PROJECT_SUMMARY_V3.md   # 项目总结
└── compiler/               # SQL编译器
    ├── lexer_v3.py
    ├── parser_v3.py
    ├── semantic_v3.py
    └── sql_compiler_v3.py
└── storage/                # 存储系统
    └── page_storage_v3.py
└── engine/                 # 执行引擎
    └── execution_engine_v3.py
└── auth/                   # 权限管理
    ├── auth_manager.py
    └── permission_manager.py
```

## ⚡ 快速验证

### 1分钟验证
```bash
cd demo
python simple_test_v3.py
```

### 3分钟演示
```bash
cd demo
python final_demo_v3.py
```

### 5分钟完整体验
```bash
cd demo
python main_v3.py
# 登录: admin/admin123
# 执行您的示例SQL
```

## 🎉 成功标志

如果看到以下输出，说明系统运行正常：

```
✅ 词法分析成功，识别到 17 个token
✅ 语义分析成功
✅ 页面分配成功
✅ 数据写入成功
✅ 查询结果: 1, 'Alice', 25
✅ 删除操作成功
```

## 📞 获取帮助

- 查看详细文档：`USAGE_GUIDE_V3.md`
- 查看项目总结：`PROJECT_SUMMARY_V3.md`
- 运行帮助命令：在交互模式中输入 `help`

---

**恭喜！您已经成功运行了数据库系统 V3.0！** 🎊