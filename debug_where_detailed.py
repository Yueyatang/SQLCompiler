#!/usr/bin/env python3
"""
详细调试WHERE条件
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from compiler.sql_compiler_v3 import SQLCompilerV3

def debug_where_detailed():
    """详细调试WHERE条件"""
    print("=" * 60)
    print("详细调试WHERE条件")
    print("=" * 60)
    
    compiler = SQLCompilerV3()
    
    # 先创建表
    create_sql = "CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);"
    print(f"编译: {create_sql}")
    result = compiler.compile(create_sql)
    if result['success']:
        print("✅ 创建表编译成功")
        print(f"执行计划: {result['execution_plan']}")
    else:
        print(f"❌ 创建表编译失败: {result['errors']}")
        return
    
    # 测试WHERE条件
    where_sql = "SELECT * FROM tst1 WHERE age > 20;"
    print(f"\n编译: {where_sql}")
    result = compiler.compile(where_sql)
    
    if result['success']:
        print("✅ WHERE查询编译成功")
        print(f"AST: {result['ast']}")
        print(f"语义分析结果: {result['semantic_result']}")
        print(f"执行计划: {result['execution_plan']}")
        
        # 检查WHERE条件
        if 'where_clause' in result['execution_plan']:
            where_clause = result['execution_plan']['where_clause']
            print(f"WHERE条件: {where_clause}")
            
            if where_clause:
                print(f"WHERE条件类型: {where_clause['type']}")
                if where_clause['type'] == 'COMPARISON':
                    print(f"  左操作数: {where_clause['left']}")
                    print(f"  操作符: {where_clause['operator']}")
                    print(f"  右操作数: {where_clause['right']}")
            else:
                print("❌ WHERE条件为空!")
        else:
            print("❌ 执行计划中没有WHERE条件!")
    else:
        print(f"❌ WHERE查询编译失败: {result['errors']}")

if __name__ == "__main__":
    debug_where_detailed()