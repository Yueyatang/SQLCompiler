#!/usr/bin/env python3
"""
直接测试解析器
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from compiler.parser_v3 import ParserV3
from compiler.lexer_v3 import LexerV3

def main():
    print("=== 直接测试解析器 ===")
    
    # 创建词法分析器和解析器
    lexer = LexerV3()
    parser = ParserV3()
    
    # 测试SQL语句
    test_sql = "SELECT * FROM tst1 WHERE age > 15;"
    print(f"测试SQL: {test_sql}")
    
    # 词法分析
    print("\n1. 词法分析...")
    tokens = lexer.tokenize(test_sql)
    print(f"Token数量: {len(tokens)}")
    
    # 语法分析
    print("\n2. 语法分析...")
    ast = parser.parse(test_sql)
    print(f"AST: {ast}")
    
    # 检查解析器错误
    if parser.errors:
        print(f"解析器错误: {parser.errors}")
    
    if ast and 'where_clause' in ast:
        print(f"WHERE条件: {ast['where_clause']}")
    else:
        print("AST中没有WHERE条件")

if __name__ == "__main__":
    main()
