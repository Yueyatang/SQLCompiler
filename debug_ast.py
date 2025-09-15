#!/usr/bin/env python3
"""
调试AST结构
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from compiler.lexer_v3 import LexerV3
from compiler.parser_v3 import ParserV3

def debug_ast():
    """调试AST结构"""
    lexer = LexerV3()
    parser = ParserV3()
    
    sql = "CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);"
    
    print(f"SQL: {sql}")
    print("-" * 60)
    
    # 词法分析
    tokens = lexer.tokenize(sql)
    print(f"Token数量: {len(tokens)}")
    
    # 语法分析
    ast = parser.parse(sql)
    if ast:
        print("AST结构:")
        print(f"  类型: {ast['type']}")
        print(f"  表名: {ast['table_name']}")
        print(f"  列定义类型: {type(ast['columns'])}")
        print(f"  列定义: {ast['columns']}")
        
        if isinstance(ast['columns'], list):
            for i, col in enumerate(ast['columns']):
                print(f"    列{i}: {col}")
        else:
            print(f"    列定义不是列表: {ast['columns']}")
    else:
        print("AST解析失败")
        for error in parser.errors:
            print(f"错误: {error}")

if __name__ == "__main__":
    debug_ast()