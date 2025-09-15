#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from compiler.parser_v3 import SQLParserV3
from compiler.semantic_v3 import SemanticAnalyzerV3
from compiler.sql_compiler_v3 import SQLCompilerV3
from engine.execution_engine_v3 import ExecutionEngineV3
from storage.storage_engine_v3 import StorageEngineV3

class SQLInterpreter:
    def __init__(self):
        self.storage = StorageEngineV3('./data')
        self.parser = SQLParserV3()
        self.semantic_analyzer = SemanticAnalyzerV3(self.storage)
        self.compiler = SQLCompilerV3()
        self.engine = ExecutionEngineV3(self.storage)
    
    def execute_query(self, sql: str) -> Dict[str, Any]:
        try:
            # 1. 解析SQL
            ast = self.parser.parse(sql)
            print(f"解析结果 (AST): {json.dumps(ast, ensure_ascii=False, indent=2)}")
            
            # 2. 语义分析
            semantic_result = self.semantic_analyzer.analyze(ast)
            if not semantic_result['success']:
                return {'success': False, 'error': semantic_result['error']}
            
            # 3. 编译生成执行计划
            execution_plan = self.compiler.generate_execution_plan(ast)
            print(f"执行计划: {json.dumps(execution_plan, ensure_ascii=False, indent=2)}")
            
            # 4. 执行查询
            result = self.engine.execute_plan(execution_plan)
            return result
        except Exception as e:
            return {'success': False, 'error': str(e)}


# 定义测试用例
def run_test_cases():
    interpreter = SQLInterpreter()
    
    print("===== 测试复杂查询、排序和平均数计算功能 =====")
    
    # 测试1: 创建测试表
    print("\n--- 测试1: 创建测试表 ---")
    sql = "CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(50), age INT, score FLOAT, class VARCHAR(20))"
    print(f"执行SQL: {sql}")
    result = interpreter.execute_query(sql)
    print(f"结果: {result}")
    
    # 测试2: 插入测试数据
    print("\n--- 测试2: 插入测试数据 ---")
    sql = "INSERT INTO students VALUES (1, '张三', 20, 85.5, '一班'), (2, '李四', 21, 90.0, '一班'), (3, '王五', 20, 78.5, '二班'), (4, '赵六', 22, 92.5, '二班'), (5, '钱七', 21, 88.0, '一班')"
    print(f"执行SQL: {sql}")
    result = interpreter.execute_query(sql)
    print(f"结果: {result}")
    
    # 测试3: 简单查询带排序
    print("\n--- 测试3: 简单查询带排序 ---")
    sql = "SELECT * FROM students ORDER BY score DESC"
    print(f"执行SQL: {sql}")
    result = interpreter.execute_query(sql)
    print(f"结果: {result}")
    if result['success']:
        print("查询结果数据:")
        for row in result['data']:
            print(row)
    
    # 测试4: 分组查询计算平均分
    print("\n--- 测试4: 分组查询计算平均分 ---")
    sql = "SELECT class, AVG(score) AS avg_score, COUNT(*) AS student_count FROM students GROUP BY class"
    print(f"执行SQL: {sql}")
    result = interpreter.execute_query(sql)
    print(f"结果: {result}")
    if result['success']:
        print("查询结果数据:")
        for row in result['data']:
            print(row)
    
    # 测试5: 分组查询带HAVING条件
    print("\n--- 测试5: 分组查询带HAVING条件 ---")
    sql = "SELECT class, AVG(score) AS avg_score FROM students GROUP BY class HAVING AVG(score) > 85"
    print(f"执行SQL: {sql}")
    result = interpreter.execute_query(sql)
    print(f"结果: {result}")
    if result['success']:
        print("查询结果数据:")
        for row in result['data']:
            print(row)
    
    # 测试6: 复杂查询（WHERE + GROUP BY + ORDER BY）
    print("\n--- 测试6: 复杂查询（WHERE + GROUP BY + ORDER BY） ---")
    sql = "SELECT class, AVG(score) AS avg_score, MAX(score) AS max_score FROM students WHERE age > 20 GROUP BY class ORDER BY avg_score DESC"
    print(f"执行SQL: {sql}")
    result = interpreter.execute_query(sql)
    print(f"结果: {result}")
    if result['success']:
        print("查询结果数据:")
        for row in result['data']:
            print(row)
    
    # 测试7: 多列排序
    print("\n--- 测试7: 多列排序 ---")
    sql = "SELECT * FROM students ORDER BY class ASC, score DESC"
    print(f"执行SQL: {sql}")
    result = interpreter.execute_query(sql)
    print(f"结果: {result}")
    if result['success']:
        print("查询结果数据:")
        for row in result['data']:
            print(row)

if __name__ == '__main__':
    run_test_cases()