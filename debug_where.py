#!/usr/bin/env python3
"""
调试WHERE条件
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main_v3 import DatabaseSystemV3

def debug_where():
    """调试WHERE条件"""
    print("=" * 60)
    print("调试WHERE条件")
    print("=" * 60)
    
    # 创建数据库系统
    db = DatabaseSystemV3("debug_where_data")
    
    # 登录
    if not db.login('admin', 'admin123'):
        print("❌ 登录失败")
        return
    
    print("✅ 登录成功")
    
    # 创建表
    result = db.execute_sql("CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);")
    print(f"创建表: {result}")
    
    # 插入测试数据
    test_data = [
        "INSERT INTO tst1 VALUES (1, 'Alice', 25);",
        "INSERT INTO tst1 VALUES (2, 'Bob', 30);",
        "INSERT INTO tst1 VALUES (3, 'Charlie', 18);"
    ]
    
    for sql in test_data:
        result = db.execute_sql(sql)
        print(f"插入: {result}")
    
    # 查询所有数据
    print("\n查询所有数据:")
    result = db.execute_sql("SELECT * FROM tst1;")
    if result['success'] and 'data' in result:
        for row in result['data']:
            print(f"  {row}")
    
    # 测试WHERE条件
    print("\n测试WHERE条件 age > 20:")
    result = db.execute_sql("SELECT * FROM tst1 WHERE age > 20;")
    if result['success'] and 'data' in result:
        print(f"查询结果数量: {len(result['data'])}")
        for row in result['data']:
            print(f"  {row}")
    else:
        print(f"查询失败: {result}")
    
    # 测试WHERE条件 age < 20
    print("\n测试WHERE条件 age < 20:")
    result = db.execute_sql("SELECT * FROM tst1 WHERE age < 20;")
    if result['success'] and 'data' in result:
        print(f"查询结果数量: {len(result['data'])}")
        for row in result['data']:
            print(f"  {row}")
    else:
        print(f"查询失败: {result}")
    
    # 测试WHERE条件 age = 25
    print("\n测试WHERE条件 age = 25:")
    result = db.execute_sql("SELECT * FROM tst1 WHERE age = 25;")
    if result['success'] and 'data' in result:
        print(f"查询结果数量: {len(result['data'])}")
        for row in result['data']:
            print(f"  {row}")
    else:
        print(f"查询失败: {result}")

if __name__ == "__main__":
    debug_where()