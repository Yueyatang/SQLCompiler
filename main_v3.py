#!/usr/bin/env python3
"""
数据库系统主程序 V3.0
完全重新设计，整合所有模块，支持权限管理
"""

import sys
import os
from typing import Dict, Any, Optional, List

# 添加模块路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from .compiler.sql_compiler_v3 import SQLCompilerV3
    from .engine.execution_engine_v3 import ExecutionEngineV3
    from .storage.storage_adapter import StorageAdapter
    from .auth.auth_manager import AuthManager
    from .auth.permission_manager import PermissionManager
except ImportError:
    from compiler.sql_compiler_v3 import SQLCompilerV3
    from engine.execution_engine_v3 import ExecutionEngineV3
    from storage.storage_adapter import StorageAdapter
    from auth.auth_manager import AuthManager
    from auth.permission_manager import PermissionManager

class DatabaseSystemV3:
    """数据库系统 V3.0"""
    
    def __init__(self, data_dir: str = "data"):
        """初始化数据库系统"""
        self.data_dir = data_dir
        self.compiler = SQLCompilerV3()
        self.engine = ExecutionEngineV3(data_dir)
        
        # 初始化存储适配器
        self.storage_adapter = StorageAdapter(data_dir)
        
        # 初始化权限管理
        self.auth_manager = AuthManager(self.storage_adapter)
        self.permission_manager = PermissionManager(self.storage_adapter, self.auth_manager)
        
        # 确保数据目录存在
        os.makedirs(data_dir, exist_ok=True)
        
        # 同步编译器目录和执行引擎目录
        self._sync_catalogs()
    
    def _sync_catalogs(self):
        """同步编译器目录和执行引擎目录"""
        engine_catalog = self.engine.get_catalog()
        compiler_catalog = self.compiler.get_catalog()
        
        # 将执行引擎的目录同步到编译器
        for table_name, table_info in engine_catalog.items():
            if table_name not in compiler_catalog:
                self.compiler.semantic_analyzer.catalog[table_name] = table_info['schema']
    
    def login(self, username: str, password: str) -> bool:
        """用户登录"""
        return self.auth_manager.login(username, password)
    
    def logout(self) -> bool:
        """用户登出"""
        return self.auth_manager.logout()
    
    def is_authenticated(self) -> bool:
        """检查是否已认证"""
        return self.auth_manager.is_authenticated()
    
    def get_current_user(self) -> Optional[Dict[str, Any]]:
        """获取当前用户信息"""
        return self.auth_manager.get_current_user()
    
    def execute_sql(self, sql: str) -> Dict[str, Any]:
        """执行SQL语句"""
        try:
            # 检查认证状态
            if not self.is_authenticated():
                return {
                    'success': False,
                    'error': '用户未登录，请先登录'
                }
            
            # 编译SQL语句
            compile_result = self.compiler.compile(sql)
            
            if not compile_result['success']:
                return {
                    'success': False,
                    'error': f"编译错误: {'; '.join(compile_result['errors'])}"
                }
            
            # 获取执行计划
            execution_plan = compile_result['execution_plan']
            if not execution_plan:
                return {
                    'success': False,
                    'error': "执行计划生成失败"
                }
            
            # 权限检查
            current_user = self.get_current_user()
            if not self._check_permission(execution_plan, current_user['user_id']):
                return {
                    'success': False,
                    'error': f"权限不足：无法执行 {execution_plan['type']} 操作"
                }
            
            # 执行计划
            result = self.engine.execute_plan(execution_plan)
            
            # 同步目录
            self._sync_catalogs()
            
            return result
            
        except Exception as e:
            return {
                'success': False,
                'error': f"执行错误: {str(e)}"
            }
    
    def _check_permission(self, execution_plan: Dict[str, Any], user_id: int) -> bool:
        """检查执行权限"""
        plan_type = execution_plan['type']
        table_name = execution_plan.get('table_name')
        
        if not table_name:
            return True  # 没有涉及表的操作
        
        # 映射执行计划类型到权限类型
        permission_map = {
            'CREATE_TABLE': 'CREATE',
            'INSERT': 'INSERT',
            'SELECT': 'SELECT',
            'UPDATE': 'UPDATE',
            'DELETE': 'DELETE',
            'DROP_TABLE': 'DROP'
        }
        
        permission_type = permission_map.get(plan_type)
        if not permission_type:
            return True  # 未知操作类型，允许执行
        
        return self.permission_manager.check_permission(user_id, table_name, permission_type)
    
    def interactive_mode(self):
        """交互式模式"""
        print("欢迎使用数据库系统 V3.0!")
        print("=" * 60)
        
        # 登录
        while not self.is_authenticated():
            print("请先登录:")
            username = input("用户名: ").strip()
            password = input("密码: ").strip()
            
            if self.login(username, password):
                current_user = self.get_current_user()
                print(f"登录成功! 欢迎, {current_user['username']} ({current_user['role']})")
                break
            else:
                print("登录失败，请重试")
        
        print("\n输入 'exit' 或 'quit' 退出")
        print("输入 'help' 查看帮助")
        print("输入 'info' 查看数据库信息")
        print("输入 'catalog' 查看系统目录")
        print("输入 'logout' 登出")
        print("输入 'users' 查看用户列表 (仅管理员)")
        
        while True:
            try:
                sql = input("\nSQL> ").strip()
                
                if sql.lower() in ['exit', 'quit']:
                    print("再见!")
                    break
                elif sql.lower() == 'help':
                    self.show_help()
                elif sql.lower() == 'info':
                    self.engine.print_database_info()
                elif sql.lower() == 'catalog':
                    self.engine.print_catalog()
                elif sql.lower() == 'logout':
                    if self.logout():
                        print("已登出")
                        break
                    else:
                        print("登出失败")
                elif sql.lower() == 'users':
                    self._show_users()
                elif sql:
                    result = self.execute_sql(sql)
                    self._print_result(result)
                        
            except KeyboardInterrupt:
                print("\n再见!")
                break
            except EOFError:
                print("\n再见!")
                break
    
    def _show_users(self):
        """显示用户列表"""
        current_user = self.get_current_user()
        if not current_user or current_user['role'] != 'admin':
            print("权限不足：只有管理员可以查看用户列表")
            return
        
        users = self.auth_manager.list_users()
        if not users:
            print("没有找到用户")
            return
        
        print("用户列表:")
        print("-" * 60)
        print(f"{'ID':<5} {'用户名':<15} {'角色':<10} {'状态':<8} {'创建时间':<12}")
        print("-" * 60)
        
        for user in users:
            status = "活跃" if user['is_active'] else "停用"
            created_time = user['created_at']
            print(f"{user['user_id']:<5} {user['username']:<15} {user['role']:<10} {status:<8} {created_time:<12}")
    
    def _print_result(self, result: Dict[str, Any]):
        """打印执行结果"""
        if result['success']:
            if 'message' in result:
                print(f"✅ {result['message']}")
            
            if 'data' in result:
                self._print_query_result(result['data'], result.get('columns', []))
            
            if 'affected_rows' in result:
                print(f"影响行数: {result['affected_rows']}")
        else:
            print(f"❌ {result['error']}")
    
    def _print_query_result(self, data: List[Dict[str, Any]], columns: List[str]):
        """打印查询结果"""
        if not data:
            print("查询结果为空")
            return
        
        if not columns:
            columns = list(data[0].keys())
        
        # 计算列宽
        col_widths = {}
        for col in columns:
            col_widths[col] = max(len(str(col)), max(len(str(row.get(col, ''))) for row in data))
        
        # 打印表头
        header = " | ".join(f"{col:<{col_widths[col]}}" for col in columns)
        print(header)
        print("-" * len(header))
        
        # 打印数据行
        for row in data:
            row_str = " | ".join(f"{str(row.get(col, '')):<{col_widths[col]}}" for col in columns)
            print(row_str)
        
        print(f"\n共 {len(data)} 行")
    
    def show_help(self):
        """显示帮助信息"""
        help_text = """
支持的SQL语句:

1. 创建表:
   CREATE TABLE table_name (column1 TYPE, column2 TYPE, ...);

2. 插入数据:
   INSERT INTO table_name VALUES (value1, value2, ...);

3. 查询数据:
   SELECT * FROM table_name;
   SELECT column1, column2 FROM table_name WHERE condition;

4. 更新数据:
   UPDATE table_name SET column = value WHERE condition;

5. 删除数据:
   DELETE FROM table_name WHERE condition;

6. 删除表:
   DROP TABLE table_name;

支持的数据类型:
- INT: 整数
- VARCHAR(n): 变长字符串
- FLOAT: 浮点数
- BOOLEAN: 布尔值

支持的操作符:
- 比较: =, !=, <, <=, >, >=
- 逻辑: AND, OR, NOT
- 算术: +, -, *, /

示例:
   CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);
   INSERT INTO tst1 VALUES (1, 'Alice', 25);
   SELECT * FROM tst1 WHERE age > 20;
   UPDATE tst1 SET age = 26 WHERE id = 1;
   DELETE FROM tst1 WHERE age < 18;
   DROP TABLE tst1;

特殊命令:
   help    - 显示此帮助信息
   info    - 显示数据库信息
   catalog - 显示系统目录
   users   - 显示用户列表 (仅管理员)
   logout  - 登出
   exit    - 退出程序

权限说明:
   - 管理员拥有所有权限
   - 普通用户只能操作自己创建的表
   - 需要相应权限才能执行增删改查操作
        """
        print(help_text)
    
    def run_test_suite(self):
        """运行测试套件"""
        print("运行测试套件...")
        
        # 使用默认管理员账户登录
        if not self.login('admin', 'admin123'):
            print("无法使用默认管理员账户登录")
            return
        
        # 测试SQL语句
        test_sqls = [
            "CREATE TABLE tst1 (id INT, name VARCHAR(50), age INT);",
            "INSERT INTO tst1 VALUES (1, 'Alice', 25);",
            "INSERT INTO tst1 VALUES (2, 'Bob', 30);",
            "INSERT INTO tst1 VALUES (3, 'Charlie', 18);",
            "SELECT * FROM tst1;",
            "SELECT * FROM tst1 WHERE age > 20;",
            "UPDATE tst1 SET age = 26 WHERE id = 1;",
            "SELECT * FROM tst1 WHERE id = 1;",
            "DELETE FROM tst1 WHERE age > 20;",
            "SELECT * FROM tst1;"
        ]
        
        print("执行测试SQL语句...")
        for i, sql in enumerate(test_sqls, 1):
            print(f"\n{i}. {sql}")
            result = self.execute_sql(sql)
            self._print_result(result)
        
        print("\n测试完成!")

def main():
    """主函数"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            # 运行测试
            db = DatabaseSystemV3()
            db.run_test_suite()
        else:
            # 从文件执行SQL
            db = DatabaseSystemV3()
            if not db.login('admin', 'admin123'):
                print("无法使用默认管理员账户登录")
                return
            
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                sql_script = f.read()
                result = db.execute_sql(sql_script)
                db._print_result(result)
    else:
        # 交互式模式
        db = DatabaseSystemV3()
        db.interactive_mode()

if __name__ == "__main__":
    main()