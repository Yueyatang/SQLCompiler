#!/usr/bin/env python3
"""
数据库系统 V3.0 测试脚本
"""

import os
import sys
import shutil

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main_v3 import DatabaseSystemV3

def test_database_system():
    """测试数据库系统"""
    print("=" * 80)
    print("数据库系统 V3.0 测试")
    print("=" * 80)
    
    # 清理测试数据
    test_data_dir = "test_data_v3"
    if os.path.exists(test_data_dir):
        shutil.rmtree(test_data_dir)
    
    # 创建数据库系统
    db = DatabaseSystemV3(test_data_dir)
    
    # 使用默认管理员账户登录
    print("1. 登录测试...")
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
            'name': '更新记录',
            'sql': "UPDATE tst1 SET age = 26 WHERE id = 1;",
            'expected_success': True
        },
        {
            'name': '验证更新结果',
            'sql': "SELECT * FROM tst1 WHERE id = 1;",
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
    
    print("\n2. 执行测试用例...")
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
        else:
            print(f"   ❌ 测试失败: {result.get('error', '未知错误')}")
            failed += 1
    
    print(f"\n3. 测试结果统计:")
    print(f"   通过: {passed}")
    print(f"   失败: {failed}")
    print(f"   总计: {passed + failed}")
    
    if failed == 0:
        print("   🎉 所有测试通过!")
    else:
        print("   ⚠️  有测试失败")
    
    # 测试数据持久化
    print("\n4. 测试数据持久化...")
    db.logout()
    
    # 重新创建数据库系统（模拟重启）
    db2 = DatabaseSystemV3(test_data_dir)
    if db2.login('admin', 'admin123'):
        print("✅ 重新登录成功")
        
        # 查询数据是否还在
        result = db2.execute_sql("SELECT * FROM tst1;")
        if result['success'] and result['data']:
            print("✅ 数据持久化成功")
            print("   剩余数据:")
            for row in result['data']:
                print(f"     {row}")
        else:
            print("❌ 数据持久化失败")
    else:
        print("❌ 重新登录失败")
    
    print("\n" + "=" * 80)
    print("测试完成!")

if __name__ == "__main__":
    test_database_system()