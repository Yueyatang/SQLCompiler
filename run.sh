#!/bin/bash

echo "========================================"
echo "数据库系统 V3.0 启动器"
echo "========================================"
echo ""
echo "请选择运行模式:"
echo "1. 交互式模式 (推荐)"
echo "2. 功能演示"
echo "3. 组件测试"
echo "4. 完整测试"
echo "5. 退出"
echo ""
read -p "请输入选择 (1-5): " choice

case $choice in
    1)
        echo ""
        echo "启动交互式模式..."
        python main_v3.py
        ;;
    2)
        echo ""
        echo "启动功能演示..."
        python final_demo_v3.py
        ;;
    3)
        echo ""
        echo "启动组件测试..."
        python simple_test_v3.py
        ;;
    4)
        echo ""
        echo "启动完整测试..."
        python test_v3.py
        ;;
    5)
        echo "退出程序"
        exit 0
        ;;
    *)
        echo "无效选择，请重新运行"
        exit 1
        ;;
esac