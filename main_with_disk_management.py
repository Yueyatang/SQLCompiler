#!/usr/bin/env python3
"""
带磁盘存储管理功能的主程序
集成磁盘监控、存储调整、缓冲区管理、页面管理和自动清理功能
"""

import sys
import os
import time
from typing import Dict, Any, Optional, List

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from main_v3 import DatabaseSystemV3
    from storage.disk_monitor import DiskMonitor, StorageLevel
    from storage.storage_adjuster import StorageAdjuster
    from storage.adaptive_buffer_manager import AdaptiveBufferManager
    from storage.adaptive_page_manager import AdaptivePageManager
    from storage.auto_cleanup_manager import AutoCleanupManager, CleanupLevel
except ImportError as e:
    print(f"导入模块失败: {e}")
    print("请确保所有必要的模块都已正确安装")
    sys.exit(1)

class DatabaseSystemWithDiskManagement(DatabaseSystemV3):
    """带磁盘存储管理功能的数据库系统"""
    
    def __init__(self, data_directory: str = "data_with_disk_management"):
        """初始化数据库系统"""
        super().__init__(data_directory)
        
        # 磁盘存储管理组件
        self.disk_monitor = DiskMonitor(data_directory)
        self.storage_adjuster = StorageAdjuster(data_directory)
        self.auto_cleanup_manager = AutoCleanupManager(data_directory)
        
        # 注册回调
        self._register_callbacks()
        
        # 启动监控
        self._start_monitoring()
        
        print("✅ 数据库系统已启动，磁盘存储管理功能已启用")
    
    def _register_callbacks(self):
        """注册回调函数"""
        # 存储调整回调
        self.storage_adjuster.register_callback('storage_adjusted', self._on_storage_adjusted)
        self.storage_adjuster.register_callback('auto_cleanup', self._on_auto_cleanup)
        
        # 自动清理回调
        self.auto_cleanup_manager.register_callback('cleanup_completed', self._on_cleanup_completed)
        self.auto_cleanup_manager.register_callback('cleanup_failed', self._on_cleanup_failed)
    
    def _start_monitoring(self):
        """启动监控"""
        # 启动存储调整器监控
        self.storage_adjuster.start_monitoring(interval=30)
        
        # 启动自动清理监控
        self.auto_cleanup_manager.start_monitoring()
        
        print("✅ 磁盘存储监控已启动")
    
    def _on_storage_adjusted(self, data: Dict):
        """存储调整回调"""
        print(f"📊 存储策略已调整: {data['new_config']}")
    
    def _on_auto_cleanup(self, data: Dict):
        """自动清理回调"""
        print(f"🧹 自动清理已执行: {data}")
    
    def _on_cleanup_completed(self, result):
        """清理完成回调"""
        print(f"✅ 清理完成: {result.message}")
    
    def _on_cleanup_failed(self, result):
        """清理失败回调"""
        print(f"❌ 清理失败: {result.message}")
    
    def get_disk_status(self) -> Dict[str, Any]:
        """获取磁盘状态"""
        return {
            'disk_info': self.disk_monitor.get_disk_info().__dict__,
            'storage_status': self.storage_adjuster.get_storage_status(),
            'cleanup_stats': self.auto_cleanup_manager.get_stats()
        }
    
    def print_disk_status(self):
        """打印磁盘状态"""
        print("=" * 80)
        print("磁盘存储管理状态")
        print("=" * 80)
        
        # 磁盘监控状态
        self.disk_monitor.print_status()
        print()
        
        # 存储调整器状态
        self.storage_adjuster.print_status()
        print()
        
        # 自动清理状态
        self.auto_cleanup_manager.print_status()
    
    def force_cleanup(self) -> Dict[str, Any]:
        """强制清理"""
        print("🧹 执行强制清理...")
        
        # 执行自动清理
        cleanup_result = self.auto_cleanup_manager.perform_cleanup(CleanupLevel.AGGRESSIVE)
        
        # 执行存储调整器清理
        storage_cleanup = self.storage_adjuster.force_cleanup()
        
        return {
            'cleanup_result': cleanup_result.__dict__,
            'storage_cleanup': storage_cleanup
        }
    
    def adjust_storage_strategy(self, force: bool = False) -> Dict[str, Any]:
        """调整存储策略"""
        return self.storage_adjuster.adjust_storage_strategy(force)
    
    def set_cleanup_config(self, config: Dict[str, Any]):
        """设置清理配置"""
        self.auto_cleanup_manager.set_cleanup_config(config)
    
    def enable_cleanup(self):
        """启用自动清理"""
        self.auto_cleanup_manager.enable_cleanup()
    
    def disable_cleanup(self):
        """禁用自动清理"""
        self.auto_cleanup_manager.disable_cleanup()
    
    def shutdown(self):
        """关闭数据库系统"""
        print("🔄 关闭数据库系统...")
        
        # 停止监控
        self.storage_adjuster.stop_monitoring()
        self.auto_cleanup_manager.stop_monitoring()
        
        # 关闭执行引擎
        if hasattr(self.engine, 'shutdown'):
            self.engine.shutdown()
        
        print("✅ 数据库系统已关闭")

def main():
    """主函数"""
    print("=" * 80)
    print("数据库系统 - 磁盘存储管理版本")
    print("=" * 80)
    
    # 创建数据库系统
    db = DatabaseSystemWithDiskManagement()
    
    try:
        # 登录
        if not db.login('admin', 'admin123'):
            print("❌ 登录失败")
            return
        
        print("✅ 登录成功")
        
        # 显示初始磁盘状态
        print("\n📊 初始磁盘状态:")
        db.print_disk_status()
        
        # 交互式命令循环
        while True:
            try:
                print("\n" + "=" * 60)
                print("可用命令:")
                print("  SQL> <SQL语句>           - 执行SQL语句")
                print("  STATUS                   - 显示磁盘状态")
                print("  CLEANUP                  - 执行强制清理")
                print("  ADJUST                   - 调整存储策略")
                print("  ENABLE_CLEANUP           - 启用自动清理")
                print("  DISABLE_CLEANUP          - 禁用自动清理")
                print("  QUIT                     - 退出")
                print("=" * 60)
                
                command = input("请输入命令: ").strip()
                
                if command.upper() == 'QUIT':
                    break
                elif command.upper() == 'STATUS':
                    db.print_disk_status()
                elif command.upper() == 'CLEANUP':
                    result = db.force_cleanup()
                    print(f"清理结果: {result}")
                elif command.upper() == 'ADJUST':
                    result = db.adjust_storage_strategy(force=True)
                    print(f"调整结果: {result}")
                elif command.upper() == 'ENABLE_CLEANUP':
                    db.enable_cleanup()
                elif command.upper() == 'DISABLE_CLEANUP':
                    db.disable_cleanup()
                elif command.startswith('SQL>'):
                    sql = command[4:].strip()
                    if sql:
                        result = db.execute_sql(sql)
                        print(f"执行结果: {result}")
                else:
                    # 直接执行SQL
                    result = db.execute_sql(command)
                    print(f"执行结果: {result}")
                    
            except KeyboardInterrupt:
                print("\n\n用户中断，正在退出...")
                break
            except Exception as e:
                print(f"❌ 错误: {e}")
    
    finally:
        # 关闭数据库系统
        db.shutdown()

if __name__ == "__main__":
    main()