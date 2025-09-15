#!/usr/bin/env python3
"""
调试解析器问题
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from compiler.sql_compiler_v3 import SQLCompilerV3

def main():
    print("=== 调试解析器问题 ===")
    
    # 创建编译器和执行引擎
    compiler = SQLCompilerV3()
    from engine.execution_engine_v3 import ExecutionEngineV3
    engine = ExecutionEngineV3("debug_where_data")
    
    # 先创建表
    print("1. 创建表...")
    create_sql = "CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);"
    create_result = compiler.compile(create_sql)
    if create_result['success']:
        engine.execute_plan(create_result['execution_plan'])
        print("表创建成功")
    else:
        print(f"创建表失败: {create_result['errors']}")
        return
    
    # 测试SQL语句
    test_sql = "SELECT * FROM tst1 WHERE age > 15;"
    print(f"\n测试SQL: {test_sql}")
    
    # 编译SQL
    print("\n2. 编译SQL...")
    compile_result = compiler.compile(test_sql)
    
    print(f"编译成功: {compile_result['success']}")
    if not compile_result['success']:
        print(f"编译错误: {compile_result['errors']}")
        return
    
    print(f"AST: {compile_result['ast']}")
    print(f"执行计划: {compile_result['execution_plan']}")
    
    # 检查WHERE条件
    where_clause = compile_result['execution_plan'].get('where_clause')
    print(f"\nWHERE条件: {where_clause}")
    
    if where_clause:
        print(f"WHERE条件类型: {where_clause['type']}")
        print(f"操作符: {where_clause['operator']}")
        print(f"左操作数: {where_clause['left']}")
        print(f"右操作数: {where_clause['right']}")
    else:
        print("WHERE条件为None，检查AST...")
        ast = compile_result['ast']
        if 'where_clause' in ast:
            print(f"AST中的WHERE条件: {ast['where_clause']}")
        else:
            print("AST中没有WHERE条件")

if __name__ == "__main__":
    main()
