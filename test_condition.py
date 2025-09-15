#!/usr/bin/env python3
"""
测试条件评估
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine.execution_engine_v3 import ExecutionEngineV3

def test_condition():
    """测试条件评估"""
    print("=" * 60)
    print("测试条件评估")
    print("=" * 60)
    
    engine = ExecutionEngineV3("test_condition_data")
    
    # 测试记录
    test_record = {'id': 1, 'name': 'Alice', 'age': 25}
    
    # 测试条件
    test_conditions = [
        {
            'name': 'age > 20',
            'condition': {
                'type': 'COMPARISON',
                'operator': '>',
                'left': {'type': 'COLUMN', 'name': 'age'},
                'right': {'type': 'NUMBER', 'value': 20}
            }
        },
        {
            'name': 'age < 20',
            'condition': {
                'type': 'COMPARISON',
                'operator': '<',
                'left': {'type': 'COLUMN', 'name': 'age'},
                'right': {'type': 'NUMBER', 'value': 20}
            }
        },
        {
            'name': 'age = 25',
            'condition': {
                'type': 'COMPARISON',
                'operator': '=',
                'left': {'type': 'COLUMN', 'name': 'age'},
                'right': {'type': 'NUMBER', 'value': 25}
            }
        }
    ]
    
    print(f"测试记录: {test_record}")
    print()
    
    for test in test_conditions:
        print(f"测试条件: {test['name']}")
        print(f"条件: {test['condition']}")
        
        try:
            result = engine._evaluate_condition(test['condition'], test_record)
            print(f"结果: {result}")
            
            # 手动验证
            age = test_record['age']
            expected = False
            if test['name'] == 'age > 20':
                expected = age > 20
            elif test['name'] == 'age < 20':
                expected = age < 20
            elif test['name'] == 'age = 25':
                expected = age == 25
            
            print(f"期望结果: {expected}")
            print(f"结果正确: {'✅' if result == expected else '❌'}")
        except Exception as e:
            print(f"❌ 评估失败: {e}")
        
        print()

if __name__ == "__main__":
    test_condition()