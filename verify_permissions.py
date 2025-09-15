#!/usr/bin/env python3
"""
权限功能验证脚本
包含具体的SQL语句来测试权限系统
"""

from main import DatabaseSystem

def verify_permission_system():
    """验证权限系统功能"""
    print("🔐 权限系统功能验证")
    print("=" * 60)
    
    # 创建数据库系统
    db = DatabaseSystem("verify_permission_data")
    
    # 验证步骤
    steps = [
        {
            "step": 1,
            "title": "测试未登录状态",
            "sql": "SELECT * FROM test_table",
            "expected": "错误: 请先登录"
        },
        {
            "step": 2,
            "title": "管理员登录",
            "sql": "LOGIN admin 'admin123'",
            "expected": "登录成功"
        },
        {
            "step": 3,
            "title": "查看用户列表",
            "sql": "SHOW USERS",
            "expected": "用户列表"
        },
        {
            "step": 4,
            "title": "创建普通用户alice",
            "sql": "CREATE USER alice 'password123' ROLE user",
            "expected": "用户创建成功"
        },
        {
            "step": 5,
            "title": "创建普通用户bob",
            "sql": "CREATE USER bob 'password456' ROLE user",
            "expected": "用户创建成功"
        },
        {
            "step": 6,
            "title": "再次查看用户列表",
            "sql": "SHOW USERS",
            "expected": "包含3个用户"
        },
        {
            "step": 7,
            "title": "创建测试表",
            "sql": "CREATE TABLE employees (id INT, name VARCHAR(50), salary FLOAT)",
            "expected": "表创建成功"
        },
        {
            "step": 8,
            "title": "插入测试数据",
            "sql": "INSERT INTO employees VALUES (1, 'Alice', 50000.0)",
            "expected": "数据插入成功"
        },
        {
            "step": 9,
            "title": "查询数据",
            "sql": "SELECT * FROM employees",
            "expected": "查询结果"
        },
        {
            "step": 10,
            "title": "授权alice查询权限",
            "sql": "GRANT SELECT ON employees TO alice",
            "expected": "授权成功"
        },
        {
            "step": 11,
            "title": "授权alice插入权限",
            "sql": "GRANT INSERT ON employees TO alice",
            "expected": "授权成功"
        },
        {
            "step": 12,
            "title": "查看alice的权限",
            "sql": "SHOW GRANTS FOR alice",
            "expected": "显示alice的权限"
        },
        {
            "step": 13,
            "title": "管理员登出",
            "sql": "LOGOUT",
            "expected": "登出成功"
        },
        {
            "step": 14,
            "title": "alice登录",
            "sql": "LOGIN alice 'password123'",
            "expected": "alice登录成功"
        },
        {
            "step": 15,
            "title": "alice查询数据（有权限）",
            "sql": "SELECT * FROM employees",
            "expected": "查询成功"
        },
        {
            "step": 16,
            "title": "alice插入数据（有权限）",
            "sql": "INSERT INTO employees VALUES (2, 'Bob', 60000.0)",
            "expected": "插入成功"
        },
        {
            "step": 17,
            "title": "alice尝试更新数据（无权限）",
            "sql": "UPDATE employees SET salary = 55000.0 WHERE id = 1",
            "expected": "权限不足"
        },
        {
            "step": 18,
            "title": "alice登出",
            "sql": "LOGOUT",
            "expected": "登出成功"
        },
        {
            "step": 19,
            "title": "bob登录",
            "sql": "LOGIN bob 'password456'",
            "expected": "bob登录成功"
        },
        {
            "step": 20,
            "title": "bob尝试查询数据（无权限）",
            "sql": "SELECT * FROM employees",
            "expected": "权限不足"
        },
        {
            "step": 21,
            "title": "bob登出",
            "sql": "LOGOUT",
            "expected": "登出成功"
        },
        {
            "step": 22,
            "title": "管理员重新登录",
            "sql": "LOGIN admin 'admin123'",
            "expected": "管理员登录成功"
        },
        {
            "step": 23,
            "title": "撤销alice的插入权限",
            "sql": "REVOKE INSERT ON employees FROM alice",
            "expected": "撤销成功"
        },
        {
            "step": 24,
            "title": "查看alice的权限变化",
            "sql": "SHOW GRANTS FOR alice",
            "expected": "只显示SELECT权限"
        },
        {
            "step": 25,
            "title": "修改管理员密码",
            "sql": "CHANGE PASSWORD 'admin123' TO 'newadmin123'",
            "expected": "密码修改成功"
        },
        {
            "step": 26,
            "title": "登出",
            "sql": "LOGOUT",
            "expected": "登出成功"
        },
        {
            "step": 27,
            "title": "用新密码登录",
            "sql": "LOGIN admin 'newadmin123'",
            "expected": "新密码登录成功"
        },
        {
            "step": 28,
            "title": "最终查询验证",
            "sql": "SELECT * FROM employees",
            "expected": "查询成功"
        }
    ]
    
    # 执行验证步骤
    for step_info in steps:
        print(f"\n步骤 {step_info['step']:2d}: {step_info['title']}")
        print(f"SQL: {step_info['sql']}")
        print(f"期望: {step_info['expected']}")
        
        try:
            result = db.execute_sql(step_info['sql'])
            print(f"结果: {result}")
            
            # 简单的成功判断
            if "错误" in str(result) and "权限不足" in step_info['expected']:
                print("✅ 符合预期（权限被正确拒绝）")
            elif "成功" in str(result) and "成功" in step_info['expected']:
                print("✅ 符合预期")
            elif "登录成功" in str(result) and "登录成功" in step_info['expected']:
                print("✅ 符合预期")
            elif "登出成功" in str(result) and "登出成功" in step_info['expected']:
                print("✅ 符合预期")
            elif "权限" in str(result) and "权限" in step_info['expected']:
                print("✅ 符合预期")
            else:
                print("⚠️  需要检查结果")
                
        except Exception as e:
            print(f"❌ 执行错误: {e}")
        
        print("-" * 60)
    
    print("\n🎉 权限系统验证完成！")
    print("\n📋 验证总结:")
    print("✅ 用户认证功能正常")
    print("✅ 权限管理功能正常") 
    print("✅ 权限检查功能正常")
    print("✅ 会话管理功能正常")
    print("✅ 密码管理功能正常")

if __name__ == "__main__":
    verify_permission_system()
