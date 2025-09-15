#!/usr/bin/env python3
"""
最终测试WHERE条件修复
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from compiler.sql_compiler_v3 import SQLCompilerV3
from engine.execution_engine_v3 import ExecutionEngineV3

def main():
    print("=== 最终测试WHERE条件修复 ===")
    
    # 创建编译器和执行引擎
    compiler = SQLCompilerV3()
    engine = ExecutionEngineV3("final_test_data")
    
    # 1. 创建表
    print("1. 创建表...")
    create_sql = "CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);"
    create_result = compiler.compile(create_sql)
    if create_result['success']:
        engine.execute_plan(create_result['execution_plan'])
        print("✅ 表创建成功")
    else:
        print(f"❌ 创建表失败: {create_result['errors']}")
        return
    
    # 2. 插入测试数据
    print("\n2. 插入测试数据...")
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
            print(f"✅ 插入: {id_val}, {name}, {age}")
        else:
            print(f"❌ 插入失败: {insert_result['errors']}")
    
    # 3. 查询所有数据
    print("\n3. 查询所有数据...")
    select_all_sql = "SELECT * FROM tst1;"
    select_all_result = compiler.compile(select_all_sql)
    if select_all_result['success']:
        all_data = engine.execute_plan(select_all_result['execution_plan'])
        print(f"✅ 所有数据 ({all_data['row_count']} 行):")
        for row in all_data['data']:
            print(f"   {row}")
    else:
        print(f"❌ 查询失败: {select_all_result['errors']}")
    
    # 4. 查询WHERE age > 15
    print("\n4. 查询 WHERE age > 15...")
    select_where_sql = "SELECT * FROM tst1 WHERE age > 15;"
    select_where_result = compiler.compile(select_where_sql)
    if select_where_result['success']:
        where_data = engine.execute_plan(select_where_result['execution_plan'])
        print(f"✅ WHERE结果 ({where_data['row_count']} 行):")
        for row in where_data['data']:
            print(f"   {row}")
        
        # 验证结果
        expected_count = 2  # Alice(25) 和 OMOKAGE(18)
        if where_data['row_count'] == expected_count:
            print(f"✅ 结果正确: 返回了 {expected_count} 行数据")
        else:
            print(f"❌ 结果错误: 期望 {expected_count} 行，实际 {where_data['row_count']} 行")
    else:
        print(f"❌ WHERE查询失败: {select_where_result['errors']}")

if __name__ == "__main__":
    main()
