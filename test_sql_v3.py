#!/usr/bin/env python3
"""
测试SQL功能
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main_v3 import DatabaseSystemV3

def test_sql():
    """测试SQL功能"""
    print("=" * 60)
    print("测试数据库系统 V3.0 SQL功能")
    print("=" * 60)
    
    # 创建数据库系统
    db = DatabaseSystemV3("test_sql_data")
    
    # 登录
    if not db.login('admin', 'admin123'):
        print("❌ 登录失败")
        return
    
    print("✅ 登录成功")
    
    # 测试SQL语句
    test_cases = [
        {
            'name': '创建表',
            'sql': "CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);",
            'expected_success': True
        },
        {
            'name': '插入第一条记录',
            'sql': "INSERT INTO tst1 VALUES (1, 'Alice', 25);",
            'expected_success': True
        },
        {
            'name': '插入第二条记录',
            'sql': "INSERT INTO tst1 VALUES (2, 'Bob', 30);",
            'expected_success': True
        },
        {
            'name': '插入第三条记录',
            'sql': "INSERT INTO tst1 VALUES (3, 'Charlie', 18);",
            'expected_success': True
        },
        {
            'name': '查询所有记录',
            'sql': "SELECT * FROM tst1;",
            'expected_success': True
        },
        {
            'name': '条件查询 - 年龄大于20',
            'sql': "SELECT * FROM tst1 WHERE age > 20;",
            'expected_success': True
        },
        {
            'name': '删除年龄大于20的记录',
            'sql': "DELETE FROM tst1 WHERE age > 20;",
            'expected_success': True
        },
        {
            'name': '验证删除结果',
            'sql': "SELECT * FROM tst1;",
            'expected_success': True
        }
    ]
    
    print("\n执行测试用例...")
    passed = 0
    failed = 0
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{i}. {test_case['name']}")
        print(f"   SQL: {test_case['sql']}")
        
        result = db.execute_sql(test_case['sql'])
        
        if result['success'] == test_case['expected_success']:
            print("   ✅ 测试通过")
            passed += 1
            
            # 打印查询结果
            if 'data' in result and result['data']:
                print("   查询结果:")
                for row in result['data']:
                    print(f"     {row}")
            elif 'message' in result:
                print(f"   {result['message']}")
        else:
            print(f"   ❌ 测试失败: {result.get('error', '未知错误')}")
            failed += 1
    
    print(f"\n测试结果统计:")
    print(f"   通过: {passed}")
    print(f"   失败: {failed}")
    print(f"   总计: {passed + failed}")
    
    if failed == 0:
        print("   🎉 所有测试通过!")
    else:
        print("   ⚠️  有测试失败")
    
    print("\n" + "=" * 60)
    print("测试完成!")

if __name__ == "__main__":
    test_sql()