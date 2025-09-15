#!/usr/bin/env python3
"""
测试磁盘存储管理功能
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main_with_disk_management import DatabaseSystemWithDiskManagement

def test_disk_management():
    """测试磁盘管理功能"""
    print("=" * 80)
    print("测试磁盘存储管理功能")
    print("=" * 80)
    
    # 创建数据库系统
    db = DatabaseSystemWithDiskManagement("test_disk_data")
    
    try:
        # 登录
        if not db.login('admin', 'admin123'):
            print("❌ 登录失败")
            return
        
        print("✅ 登录成功")
        
        # 显示初始状态
        print("\n📊 初始磁盘状态:")
        db.print_disk_status()
        
        # 创建测试表
        print("\n🔧 创建测试表...")
        result = db.execute_sql("CREATE TABLE test_table (id INT, name VARCHAR(50), data TEXT);")
        print(f"创建表结果: {result}")
        
        # 插入测试数据
        print("\n📝 插入测试数据...")
        for i in range(10):
            result = db.execute_sql(f"INSERT INTO test_table VALUES ({i}, 'User{i}', 'Test data {i}');")
            print(f"插入第{i+1}条记录: {result}")
        
        # 查询数据
        print("\n🔍 查询数据...")
        result = db.execute_sql("SELECT * FROM test_table WHERE id < 5;")
        print(f"查询结果: {result}")
        
        # 显示磁盘状态变化
        print("\n📊 操作后磁盘状态:")
        db.print_disk_status()
        
        # 测试存储策略调整
        print("\n⚙️ 测试存储策略调整...")
        result = db.adjust_storage_strategy(force=True)
        print(f"策略调整结果: {result}")
        
        # 测试强制清理
        print("\n🧹 测试强制清理...")
        result = db.force_cleanup()
        print(f"清理结果: {result}")
        
        # 最终状态
        print("\n📊 最终磁盘状态:")
        db.print_disk_status()
        
        print("\n✅ 磁盘存储管理功能测试完成！")
        
    except Exception as e:
        print(f"❌ 测试过程中出现错误: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # 关闭数据库系统
        db.shutdown()

if __name__ == "__main__":
    test_disk_management()