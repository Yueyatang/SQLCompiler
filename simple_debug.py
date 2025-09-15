#!/usr/bin/env python3
"""
简单调试WHERE条件问题
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from compiler.sql_compiler_v3 import SQLCompilerV3
from engine.execution_engine_v3 import ExecutionEngineV3

def main():
    print("=== 简单调试WHERE条件问题 ===")
    
    # 创建编译器和执行引擎
    compiler = SQLCompilerV3()
    engine = ExecutionEngineV3("debug_where_data")
    
    # 1. 创建表
    print("1. 创建表...")
    create_sql = "CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);"
    create_result = compiler.compile(create_sql)
    if create_result['success']:
        engine.execute_plan(create_result['execution_plan'])
        print("表创建成功")
    else:
        print(f"创建表失败: {create_result['errors']}")
        return
    
    # 2. 插入测试数据
    print("2. 插入测试数据...")
    test_data = [
        (1, 'Alice', 25),
        (2, 'OMOKAGE', 18),
        (3, 'YUGUMA', 12)
    ]
    
    for id_val, name, age in test_data:
        insert_sql = f"INSERT INTO tst1 VALUES ({id_val}, '{name}', {age});"
        insert_result = compiler.compile(insert_sql)
        if insert_result['success']:
            engine.execute_plan(insert_result['execution_plan'])
            print(f"插入: {id_val}, {name}, {age}")
    
    # 3. 查询所有数据
    print("\n3. 查询所有数据...")
    select_all_sql = "SELECT * FROM tst1;"
    select_all_result = compiler.compile(select_all_sql)
    if select_all_result['success']:
        all_data = engine.execute_plan(select_all_result['execution_plan'])
        print(f"所有数据: {all_data}")
    
    # 4. 查询带WHERE条件的数据
    print("\n4. 查询WHERE age > 15...")
    select_where_sql = "SELECT * FROM tst1 WHERE age > 15;"
    select_where_result = compiler.compile(select_where_sql)
    if select_where_result['success']:
        where_data = engine.execute_plan(select_where_result['execution_plan'])
        print(f"WHERE结果: {where_data}")
        
        # 检查WHERE条件结构
        where_clause = select_where_result['execution_plan'].get('where_clause')
        print(f"WHERE条件: {where_clause}")
    else:
        print(f"查询失败: {select_where_result['errors']}")

if __name__ == "__main__":
    main()
