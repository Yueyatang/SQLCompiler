#!/usr/bin/env python3
"""
简单的数据库系统 V3.0 测试
"""

import os
import sys

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_lexer():
    """测试词法分析器"""
    print("测试词法分析器...")
    try:
        from compiler.lexer_v3 import LexerV3
        
        lexer = LexerV3()
        sql = "CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);"
        tokens = lexer.tokenize(sql)
        
        print(f"✅ 词法分析成功，识别到 {len(tokens)} 个token")
        for token in tokens[:5]:  # 只显示前5个
            print(f"   {token['type']}: {token['value']}")
        return True
    except Exception as e:
        print(f"❌ 词法分析失败: {e}")
        return False

def test_parser():
    """测试语法分析器"""
    print("\n测试语法分析器...")
    try:
        from compiler.parser_v3 import ParserV3
        
        parser = ParserV3()
        sql = "CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);"
        ast = parser.parse(sql)
        
        if ast:
            print("✅ 语法分析成功")
            print(f"   AST类型: {ast['type']}")
            print(f"   表名: {ast['table_name']}")
            return True
        else:
            print("❌ 语法分析失败")
            return False
    except Exception as e:
        print(f"❌ 语法分析失败: {e}")
        return False

def test_semantic():
    """测试语义分析器"""
    print("\n测试语义分析器...")
    try:
        from compiler.semantic_v3 import SemanticAnalyzerV3
        
        analyzer = SemanticAnalyzerV3()
        
        # 构造AST
        ast = {
            'type': 'CREATE_TABLE',
            'table_name': 'tst1',
            'columns': [
                {'name': 'id', 'type': {'type': 'int'}, 'constraints': []},
                {'name': 'name', 'type': {'type': 'varchar', 'length': 50}, 'constraints': []},
                {'name': 'age', 'type': {'type': 'int'}, 'constraints': []}
            ]
        }
        
        result = analyzer.analyze(ast)
        
        if result['valid']:
            print("✅ 语义分析成功")
            print(f"   表名: {result['table_name']}")
            return True
        else:
            print(f"❌ 语义分析失败: {result['errors']}")
            return False
    except Exception as e:
        print(f"❌ 语义分析失败: {e}")
        return False

def test_storage():
    """测试存储系统"""
    print("\n测试存储系统...")
    try:
        from storage.page_storage_v3 import PageStorageV3
        
        storage = PageStorageV3("test_storage")
        
        # 分配页面
        page_id = storage.allocate_page()
        print(f"✅ 页面分配成功: {page_id}")
        
        # 写入数据
        test_data = b"Hello, World!" + b'\x00' * (4096 - 13)
        storage.write_page(page_id, test_data)
        print("✅ 数据写入成功")
        
        # 读取数据
        read_data = storage.read_page(page_id)
        print(f"✅ 数据读取成功: {read_data[:13].decode('utf-8')}")
        
        # 释放页面
        storage.deallocate_page(page_id)
        print("✅ 页面释放成功")
        
        return True
    except Exception as e:
        print(f"❌ 存储系统测试失败: {e}")
        return False

def test_auth():
    """测试认证系统"""
    print("\n测试认证系统...")
    try:
        from auth.auth_manager import AuthManager
        from storage.page_storage_v3 import PageStorageV3
        
        storage = PageStorageV3("test_auth")
        auth_manager = AuthManager(storage)
        
        # 测试登录
        if auth_manager.login('admin', 'admin123'):
            print("✅ 管理员登录成功")
            current_user = auth_manager.get_current_user()
            print(f"   当前用户: {current_user['username']} ({current_user['role']})")
            return True
        else:
            print("❌ 管理员登录失败")
            return False
    except Exception as e:
        print(f"❌ 认证系统测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("=" * 60)
    print("数据库系统 V3.0 组件测试")
    print("=" * 60)
    
    tests = [
        test_lexer,
        test_parser,
        test_semantic,
        test_storage,
        test_auth
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 60)
    print(f"测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有组件测试通过!")
    else:
        print("⚠️  有组件测试失败")
    
    print("=" * 60)

if __name__ == "__main__":
    main()