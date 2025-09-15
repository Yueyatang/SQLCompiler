#!/usr/bin/env python3
"""
小型数据库系统主程序
"""

import sys
import os
from compiler.sql_compiler import SQLCompiler
from storage.storage_manager import StorageManager
from engine.database_engine import DatabaseEngine

class DatabaseSystem:
    """数据库系统主类"""
    
    def __init__(self, data_dir="data"):
        """初始化数据库系统"""
        self.data_dir = data_dir
        self.storage_manager = StorageManager(data_dir)
        self.compiler = SQLCompiler()
        self.engine = DatabaseEngine(self.storage_manager)
        
        # 确保数据目录存在
        os.makedirs(data_dir, exist_ok=True)
        
    def execute_sql(self, sql):
        """执行SQL语句"""
        try:
            # 编译SQL语句
            ast = self.compiler.compile(sql)
            
            # 执行查询计划
            result = self.engine.execute(ast)
            
            return result
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def interactive_mode(self):
        """交互式模式"""
        print("欢迎使用小型数据库系统!")
        print("输入 'exit' 或 'quit' 退出")
        print("输入 'help' 查看帮助")
        print("请先登录: LOGIN admin admin123")
        
        while True:
            try:
                # 显示当前用户状态
                current_user = self.engine.auth_manager.get_current_user()
                if current_user:
                    prompt = f"\nSQL [{current_user['username']}]> "
                else:
                    prompt = "\nSQL> "
                
                sql = input(prompt).strip()
                
                if sql.lower() in ['exit', 'quit']:
                    print("再见!")
                    break
                elif sql.lower() == 'help':
                    self.show_help()
                elif sql:
                    result = self.execute_sql(sql)
                    if result:
                        print(result)
                        
            except KeyboardInterrupt:
                print("\n再见!")
                break
            except EOFError:
                print("\n再见!")
                break
    
    def show_help(self):
        """显示帮助信息"""
        help_text = """
支持的SQL语句:

=== 认证和权限管理 ===
1. 用户登录:
   LOGIN username password

2. 用户登出:
   LOGOUT

3. 创建用户 (仅管理员):
   CREATE USER username password ROLE role

4. 修改密码:
   CHANGE PASSWORD 'old_password' TO 'new_password'

5. 授权权限:
   GRANT permission1, permission2 ON table_name TO username

6. 撤销权限:
   REVOKE permission1, permission2 ON table_name FROM username

7. 查看用户权限:
   SHOW GRANTS FOR username

8. 查看用户列表 (仅管理员):
   SHOW USERS

=== 数据操作 ===
9. 创建表:
   CREATE TABLE table_name (column1 TYPE, column2 TYPE, ...)

10. 插入数据:
    INSERT INTO table_name VALUES (value1, value2, ...)

11. 查询数据:
    SELECT * FROM table_name
    SELECT column1, column2 FROM table_name WHERE condition

12. 更新数据:
    UPDATE table_name SET column = value WHERE condition

13. 删除数据:
    DELETE FROM table_name WHERE condition

14. 删除表:
    DROP TABLE table_name

=== 权限类型 ===
- SELECT: 查询权限
- INSERT: 插入权限
- UPDATE: 更新权限
- DELETE: 删除权限
- CREATE: 创建表权限
- DROP: 删除表权限
- GRANT: 授权权限

=== 支持的数据类型 ===
- INT: 整数
- VARCHAR(n): 变长字符串
- FLOAT: 浮点数
- BOOLEAN: 布尔值

=== 使用示例 ===
1. 登录: LOGIN admin admin123
2. 创建表: CREATE TABLE users (id INT, name VARCHAR(50), age INT)
3. 插入数据: INSERT INTO users VALUES (1, 'Alice', 25)
4. 查询数据: SELECT * FROM users WHERE age > 20
5. 授权: GRANT SELECT, INSERT ON users TO alice
        """
        print(help_text)

def main():
    """主函数"""
    if len(sys.argv) > 1:
        # 从文件执行SQL
        db = DatabaseSystem()
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            sql_script = f.read()
            result = db.execute_sql(sql_script)
            print(result)
    else:
        # 交互式模式
        db = DatabaseSystem()
        db.interactive_mode()

if __name__ == "__main__":
    main()
