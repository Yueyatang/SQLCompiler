#!/usr/bin/env python3
"""
调试WHERE条件问题
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from compiler.sql_compiler_v3 import SQLCompilerV3
from engine.execution_engine_v3 import ExecutionEngineV3

def debug_where_condition():
    """调试WHERE条件问题"""
    print("=== 调试WHERE条件问题 ===")
    
    try:
        # 创建编译器和执行引擎
        compiler = SQLCompilerV3()
        engine = ExecutionEngineV3("debug_where_data")
    except Exception as e:
        print(f"初始化失败: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # 3. 创建测试表和数据
    print("\n3. 创建测试表和数据...")
    
    # 创建表
    create_sql = "CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);"
    create_result = compiler.compile(create_sql)
    if create_result['success']:
        engine.execute_plan(create_result['execution_plan'])
        print("表创建成功")
    else:
        print(f"创建表失败: {create_result['errors']}")
        return
    
    # 插入测试数据
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
            print(f"插入数据: {id_val}, {name}, {age}")
        else:
            print(f"插入数据失败: {insert_result['errors']}")
    
    # 测试SQL语句
    test_sql = "SELECT * FROM tst1 WHERE age > 15;"
    print(f"\n测试SQL: {test_sql}")
    
    # 1. 编译SQL
    print("\n1. 编译SQL...")
    compile_result = compiler.compile(test_sql)
    
    if not compile_result['success']:
        print(f"编译失败: {compile_result['errors']}")
        return
    
    print("编译成功!")
    
    # 2. 检查WHERE条件结构
    where_clause = compile_result['execution_plan'].get('where_clause')
    print(f"\n2. WHERE条件结构: {where_clause}")
    
    if where_clause:
        print(f"WHERE条件类型: {where_clause['type']}")
        print(f"操作符: {where_clause['operator']}")
        print(f"左操作数: {where_clause['left']}")
        print(f"右操作数: {where_clause['right']}")
    
    # 4. 执行查询
    print("\n4. 执行查询...")
    result = engine.execute_plan(compile_result['execution_plan'])
    print(f"查询结果: {result}")
    
    # 5. 手动测试WHERE条件评估
    print("\n5. 手动测试WHERE条件评估...")
    
    # 获取表数据
    table_name = "tst1"
    table_info = engine.catalog[table_name]
    schema = table_info['schema']
    
    # 获取表的页面
    page_ids = engine.storage.get_table_pages(table_name)
    all_records = []
    for page_id in page_ids:
        page_data = engine.storage.read_page(page_id)
        records = engine._extract_records_from_page(page_data, schema)
        all_records.extend(records)
    
    print(f"表中的所有记录: {all_records}")
    
    # 手动评估WHERE条件
    if where_clause:
        print(f"\n手动评估WHERE条件: {where_clause}")
        for i, record in enumerate(all_records):
            print(f"\n记录 {i+1}: {record}")
            condition_result = engine._evaluate_condition(where_clause, record)
            print(f"WHERE条件结果: {condition_result}")
            
            # 详细调试
            left = engine._evaluate_expression(where_clause['left'], record)
            right = engine._evaluate_expression(where_clause['right'], record)
            operator = where_clause['operator']
            
            print(f"  左操作数: {left} (类型: {type(left)})")
            print(f"  右操作数: {right} (类型: {type(right)})")
            print(f"  操作符: {operator}")
            
            if operator == '>':
                comparison_result = left > right
                print(f"  {left} > {right} = {comparison_result}")

if __name__ == "__main__":
    debug_where_condition()
