#!/usr/bin/env python3
"""
综合测试脚本 V2.0
完全符合实践要求：验证所有功能、数据持久性、错误处理
"""

import os
import shutil
from compiler.sql_compiler_v2 import SQLCompilerV2
from engine.database_engine_v2 import DatabaseEngineV2
from compiler.execution_plan import ExecutionPlan

class ComprehensiveTest:
    """综合测试类"""
    
    def __init__(self, test_data_dir: str = "test_data"):
        """初始化测试"""
        self.test_data_dir = test_data_dir
        self.compiler = SQLCompilerV2()
        self.engine = DatabaseEngineV2(test_data_dir)
        self.test_results = []
    
    def run_all_tests(self):
        """运行所有测试"""
        print("=" * 80)
        print("数据库系统综合测试")
        print("=" * 80)
        
        # 清理测试数据
        self.cleanup_test_data()
        
        try:
            # 1. SQL编译器测试
            self.test_sql_compiler()
            
            # 2. 存储系统测试
            self.test_storage_system()
            
            # 3. 数据库引擎测试
            self.test_database_engine()
            
            # 4. 数据持久性测试
            self.test_data_persistence()
            
            # 5. 错误处理测试
            self.test_error_handling()
            
            # 6. 性能测试
            self.test_performance()
            
            # 打印测试结果
            self.print_test_results()
            
        finally:
            self.cleanup_test_data()
    
    def cleanup_test_data(self):
        """清理测试数据"""
        if os.path.exists(self.test_data_dir):
            shutil.rmtree(self.test_data_dir)
    
    def test_sql_compiler(self):
        """测试SQL编译器"""
        print("\n" + "="*60)
        print("1. SQL编译器测试")
        print("="*60)
        
        test_cases = [
            {
                'name': 'CREATE TABLE语句',
                'sql': 'CREATE TABLE student(id INT PRIMARY KEY, name VARCHAR(50), age INT);',
                'expected': 'success'
            },
            {
                'name': 'INSERT语句',
                'sql': 'INSERT INTO student VALUES (1, \'Alice\', 20);',
                'expected': 'success'
            },
            {
                'name': 'SELECT语句',
                'sql': 'SELECT id, name FROM student WHERE age > 18;',
                'expected': 'success'
            },
            {
                'name': 'DELETE语句',
                'sql': 'DELETE FROM student WHERE id = 1;',
                'expected': 'success'
            },
            {
                'name': '语法错误测试',
                'sql': 'CREATE TABLE student(id INT, name VARCHAR(50), age INT',  # 缺少分号
                'expected': 'error'
            },
            {
                'name': '语义错误测试',
                'sql': 'INSERT INTO student VALUES (1, \'Alice\', \'invalid\');',  # 类型不匹配
                'expected': 'error'
            }
        ]
        
        for test_case in test_cases:
            print(f"\n测试: {test_case['name']}")
            print(f"SQL: {test_case['sql']}")
            
            result = self.compiler.compile(test_case['sql'])
            
            if test_case['expected'] == 'success':
                if not result['errors']:
                    print("✅ 测试通过")
                    self.test_results.append(f"SQL编译器 - {test_case['name']}: 通过")
                else:
                    print(f"❌ 测试失败: {result['errors']}")
                    self.test_results.append(f"SQL编译器 - {test_case['name']}: 失败")
            else:
                if result['errors']:
                    print("✅ 测试通过 (正确识别错误)")
                    self.test_results.append(f"SQL编译器 - {test_case['name']}: 通过")
                else:
                    print("❌ 测试失败 (未识别出错误)")
                    self.test_results.append(f"SQL编译器 - {test_case['name']}: 失败")
    
    def test_storage_system(self):
        """测试存储系统"""
        print("\n" + "="*60)
        print("2. 存储系统测试")
        print("="*60)
        
        # 测试页面分配
        print("\n测试页面分配...")
        page_id1 = self.engine.storage_engine.storage_system.allocate_page()
        page_id2 = self.engine.storage_engine.storage_system.allocate_page()
        print(f"分配页面: {page_id1}, {page_id2}")
        
        # 测试页面读写
        print("\n测试页面读写...")
        test_data = bytearray(4096)
        test_data[0:4] = b'TEST'
        
        success = self.engine.storage_engine.storage_system.write_page(page_id1, test_data)
        if success:
            read_data = self.engine.storage_engine.storage_system.read_page(page_id1)
            if read_data and read_data[0:4] == b'TEST':
                print("✅ 页面读写测试通过")
                self.test_results.append("存储系统 - 页面读写: 通过")
            else:
                print("❌ 页面读写测试失败")
                self.test_results.append("存储系统 - 页面读写: 失败")
        else:
            print("❌ 页面写入失败")
            self.test_results.append("存储系统 - 页面写入: 失败")
        
        # 测试缓存管理
        print("\n测试缓存管理...")
        cache = self.engine.storage_engine.cache_manager
        
        # 测试缓存命中
        data1 = cache.get_page(page_id1)
        data2 = cache.get_page(page_id1)  # 第二次访问应该命中缓存
        
        stats = cache.get_cache_statistics()
        if stats['hit_count'] > 0:
            print("✅ 缓存管理测试通过")
            self.test_results.append("存储系统 - 缓存管理: 通过")
        else:
            print("❌ 缓存管理测试失败")
            self.test_results.append("存储系统 - 缓存管理: 失败")
        
        # 清理
        self.engine.storage_engine.storage_system.deallocate_page(page_id1)
        self.engine.storage_engine.storage_system.deallocate_page(page_id2)
    
    def test_database_engine(self):
        """测试数据库引擎"""
        print("\n" + "="*60)
        print("3. 数据库引擎测试")
        print("="*60)
        
        # 测试创建表
        print("\n测试创建表...")
        schema = {
            'columns': {
                'id': {'type': {'type': 'int'}, 'primary_key': True},
                'name': {'type': {'type': 'varchar', 'length': 50}},
                'age': {'type': {'type': 'int'}}
            },
            'primary_key': 'id'
        }
        
        success = self.engine.storage_engine.create_table("test_users", schema)
        if success:
            print("✅ 创建表测试通过")
            self.test_results.append("数据库引擎 - 创建表: 通过")
        else:
            print("❌ 创建表测试失败")
            self.test_results.append("数据库引擎 - 创建表: 失败")
        
        # 测试插入记录
        print("\n测试插入记录...")
        from engine.database_engine_v2 import Record
        
        records = [
            Record({'id': 1, 'name': 'Alice', 'age': 25}, schema),
            Record({'id': 2, 'name': 'Bob', 'age': 30}, schema),
            Record({'id': 3, 'name': 'Charlie', 'age': 35}, schema)
        ]
        
        insert_success = 0
        for record in records:
            if self.engine.storage_engine.insert_record("test_users", record):
                insert_success += 1
        
        if insert_success == len(records):
            print("✅ 插入记录测试通过")
            self.test_results.append("数据库引擎 - 插入记录: 通过")
        else:
            print(f"❌ 插入记录测试失败 ({insert_success}/{len(records)})")
            self.test_results.append("数据库引擎 - 插入记录: 失败")
        
        # 测试扫描记录
        print("\n测试扫描记录...")
        scanned_records = self.engine.storage_engine.scan_records("test_users")
        print(f"扫描到 {len(scanned_records)} 条记录")
        
        if len(scanned_records) == len(records):
            print("✅ 扫描记录测试通过")
            self.test_results.append("数据库引擎 - 扫描记录: 通过")
        else:
            print(f"❌ 扫描记录测试失败 (期望{len(records)}, 实际{len(scanned_records)})")
            self.test_results.append("数据库引擎 - 扫描记录: 失败")
        
        # 测试执行计划
        print("\n测试执行计划...")
        from compiler.execution_plan import ExecutionPlan
        
        # 创建SeqScan计划
        seqscan_plan = ExecutionPlan("SeqScan", table_name="test_users")
        project_plan = ExecutionPlan("Project", columns="*")
        project_plan.add_child(seqscan_plan)
        
        try:
            result = self.engine.execute_plan(project_plan)
            if isinstance(result, list) and len(result) > 0:
                print("✅ 执行计划测试通过")
                self.test_results.append("数据库引擎 - 执行计划: 通过")
            else:
                print("❌ 执行计划测试失败")
                self.test_results.append("数据库引擎 - 执行计划: 失败")
        except Exception as e:
            print(f"❌ 执行计划测试失败: {e}")
            self.test_results.append("数据库引擎 - 执行计划: 失败")
    
    def test_data_persistence(self):
        """测试数据持久性"""
        print("\n" + "="*60)
        print("4. 数据持久性测试")
        print("="*60)
        
        # 创建一些数据
        print("\n创建测试数据...")
        schema = {
            'columns': {
                'id': {'type': {'type': 'int'}, 'primary_key': True},
                'data': {'type': {'type': 'varchar', 'length': 100}}
            },
            'primary_key': 'id'
        }
        
        self.engine.storage_engine.create_table("persistence_test", schema)
        
        from engine.database_engine_v2 import Record
        test_record = Record({'id': 1, 'data': 'persistence_test_data'}, schema)
        self.engine.storage_engine.insert_record("persistence_test", test_record)
        
        # 关闭引擎
        print("关闭数据库引擎...")
        self.engine.shutdown()
        
        # 重新启动引擎
        print("重新启动数据库引擎...")
        self.engine = DatabaseEngineV2(self.test_data_dir)
        
        # 检查数据是否仍然存在
        print("检查数据持久性...")
        tables = self.engine.storage_engine.list_tables()
        
        if "persistence_test" in tables:
            records = self.engine.storage_engine.scan_records("persistence_test")
            if len(records) > 0 and records[0].data['data'] == 'persistence_test_data':
                print("✅ 数据持久性测试通过")
                self.test_results.append("数据持久性 - 表结构: 通过")
                self.test_results.append("数据持久性 - 数据内容: 通过")
            else:
                print("❌ 数据持久性测试失败 (数据内容不正确)")
                self.test_results.append("数据持久性 - 数据内容: 失败")
        else:
            print("❌ 数据持久性测试失败 (表不存在)")
            self.test_results.append("数据持久性 - 表结构: 失败")
    
    def test_error_handling(self):
        """测试错误处理"""
        print("\n" + "="*60)
        print("5. 错误处理测试")
        print("="*60)
        
        error_tests = [
            {
                'name': '重复创建表',
                'action': lambda: self.engine.storage_engine.create_table("test_users", {}),
                'expected_error': True
            },
            {
                'name': '访问不存在的表',
                'action': lambda: self.engine.storage_engine.get_table_schema("nonexistent_table"),
                'expected_error': False  # 应该返回None而不是抛出异常
            },
            {
                'name': '向不存在的表插入数据',
                'action': lambda: self.engine.storage_engine.insert_record("nonexistent_table", None),
                'expected_error': False  # 应该返回False而不是抛出异常
            }
        ]
        
        for test in error_tests:
            print(f"\n测试: {test['name']}")
            try:
                result = test['action']()
                if test['expected_error']:
                    print("❌ 测试失败 (期望错误但未发生)")
                    self.test_results.append(f"错误处理 - {test['name']}: 失败")
                else:
                    print("✅ 测试通过 (正确处理)")
                    self.test_results.append(f"错误处理 - {test['name']}: 通过")
            except Exception as e:
                if test['expected_error']:
                    print("✅ 测试通过 (正确抛出错误)")
                    self.test_results.append(f"错误处理 - {test['name']}: 通过")
                else:
                    print(f"❌ 测试失败 (意外错误: {e})")
                    self.test_results.append(f"错误处理 - {test['name']}: 失败")
    
    def test_performance(self):
        """测试性能"""
        print("\n" + "="*60)
        print("6. 性能测试")
        print("="*60)
        
        import time
        
        # 测试大量数据插入
        print("\n测试大量数据插入...")
        schema = {
            'columns': {
                'id': {'type': {'type': 'int'}, 'primary_key': True},
                'value': {'type': {'type': 'int'}}
            },
            'primary_key': 'id'
        }
        
        self.engine.storage_engine.create_table("performance_test", schema)
        
        start_time = time.time()
        insert_count = 100
        
        from engine.database_engine_v2 import Record
        for i in range(insert_count):
            record = Record({'id': i, 'value': i * 2}, schema)
            self.engine.storage_engine.insert_record("performance_test", record)
        
        end_time = time.time()
        insert_time = end_time - start_time
        
        print(f"插入 {insert_count} 条记录耗时: {insert_time:.3f} 秒")
        print(f"平均每条记录: {insert_time/insert_count*1000:.3f} 毫秒")
        
        # 测试查询性能
        print("\n测试查询性能...")
        start_time = time.time()
        records = self.engine.storage_engine.scan_records("performance_test")
        end_time = time.time()
        query_time = end_time - start_time
        
        print(f"查询 {len(records)} 条记录耗时: {query_time:.3f} 秒")
        
        if insert_time < 10 and query_time < 5:  # 简单的性能基准
            print("✅ 性能测试通过")
            self.test_results.append("性能测试 - 插入性能: 通过")
            self.test_results.append("性能测试 - 查询性能: 通过")
        else:
            print("❌ 性能测试失败")
            self.test_results.append("性能测试 - 插入性能: 失败")
            self.test_results.append("性能测试 - 查询性能: 失败")
    
    def print_test_results(self):
        """打印测试结果"""
        print("\n" + "="*80)
        print("测试结果汇总")
        print("="*80)
        
        passed = 0
        failed = 0
        
        for result in self.test_results:
            if "通过" in result:
                print(f"✅ {result}")
                passed += 1
            else:
                print(f"❌ {result}")
                failed += 1
        
        print(f"\n总计: {passed + failed} 项测试")
        print(f"通过: {passed} 项")
        print(f"失败: {failed} 项")
        print(f"通过率: {passed/(passed+failed)*100:.1f}%")
        
        if failed == 0:
            print("\n🎉 所有测试通过！数据库系统运行正常！")
        else:
            print(f"\n⚠️  有 {failed} 项测试失败，需要进一步调试。")

def main():
    """主函数"""
    test = ComprehensiveTest()
    test.run_all_tests()

if __name__ == "__main__":
    main()
