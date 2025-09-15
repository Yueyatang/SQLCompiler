#!/usr/bin/env python3
"""
数据库系统主程序 V2.0
完全符合实践要求：整合所有模块
"""

import sys
import os
from compiler.sql_compiler_v2 import SQLCompilerV2
from engine.database_engine_v2 import DatabaseEngineV2

class DatabaseSystemV2:
    """数据库系统 V2.0"""
    
    def __init__(self, data_dir="data"):
        """初始化数据库系统"""
        self.data_dir = data_dir
        self.compiler = SQLCompilerV2()
        self.engine = DatabaseEngineV2(data_dir)
        
        # 确保数据目录存在
        os.makedirs(data_dir, exist_ok=True)
        
    def execute_sql(self, sql):
        """执行SQL语句"""
        try:
            # 编译SQL语句
            compile_result = self.compiler.compile(sql)
            
            if compile_result['errors']:
                return f"编译错误: {'; '.join(compile_result['errors'])}"
            
            # 获取执行计划
            execution_plan = compile_result['execution_plan']
            if not execution_plan:
                return "执行计划生成失败"
            
            # 执行计划
            result = self.engine.execute_plan(execution_plan)
            
            return result
            
        except Exception as e:
            return f"执行错误: {str(e)}"
    
    def interactive_mode(self):
        """交互式模式"""
        print("欢迎使用数据库系统 V2.0!")
        print("输入 'exit' 或 'quit' 退出")
        print("输入 'help' 查看帮助")
        print("输入 'info' 查看数据库信息")
        print("输入 'catalog' 查看系统目录")
        
        while True:
            try:
                sql = input("\nSQL> ").strip()
                
                if sql.lower() in ['exit', 'quit']:
                    print("再见!")
                    break
                elif sql.lower() == 'help':
                    self.show_help()
                elif sql.lower() == 'info':
                    self.engine.print_database_info()
                elif sql.lower() == 'catalog':
                    self.compiler.print_catalog()
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

1. 创建表:
   CREATE TABLE table_name (column1 TYPE, column2 TYPE, ...);

2. 插入数据:
   INSERT INTO table_name VALUES (value1, value2, ...);

3. 查询数据:
   SELECT * FROM table_name;
   SELECT column1, column2 FROM table_name WHERE condition;

4. 更新数据:
   UPDATE table_name SET column = value WHERE condition;

5. 删除数据:
   DELETE FROM table_name WHERE condition;

6. 删除表:
   DROP TABLE table_name;

支持的数据类型:
- INT: 整数
- VARCHAR(n): 变长字符串
- FLOAT: 浮点数
- BOOLEAN: 布尔值

支持的操作符:
- 比较: =, !=, <, <=, >, >=
- 逻辑: AND, OR, NOT
- 算术: +, -, *, /

示例:
   CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(50), age INT);
   INSERT INTO users VALUES (1, 'Alice', 25);
   SELECT * FROM users WHERE age > 20;
   UPDATE users SET age = 26 WHERE id = 1;
   DELETE FROM users WHERE age < 18;
   DROP TABLE users;

特殊命令:
   help    - 显示此帮助信息
   info    - 显示数据库信息
   catalog - 显示系统目录
   exit    - 退出程序
        """
        print(help_text)
    
    def run_test_suite(self):
        """运行测试套件"""
        print("运行测试套件...")
        from comprehensive_test import ComprehensiveTest
        
        test = ComprehensiveTest("test_data")
        test.run_all_tests()

def main():
    """主函数"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            # 运行测试
            db = DatabaseSystemV2()
            db.run_test_suite()
        else:
            # 从文件执行SQL
            db = DatabaseSystemV2()
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                sql_script = f.read()
                result = db.execute_sql(sql_script)
                print(result)
    else:
        # 交互式模式
        db = DatabaseSystemV2()
        db.interactive_mode()

if __name__ == "__main__":
    main()
