#!/usr/bin/env python3
"""
简单测试
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from compiler.parser_v3 import ParserV3

def main():
    parser = ParserV3()
    test_sql = "SELECT * FROM tst1 WHERE age > 15;"
    
    print(f"SQL: {test_sql}")
    ast = parser.parse(test_sql)
    
    print(f"解析器错误: {parser.errors}")
    
    if ast:
        print(f"AST类型: {ast.get('type')}")
        print(f"WHERE条件: {ast.get('where_clause')}")
    else:
        print("解析失败")

if __name__ == "__main__":
    main()
