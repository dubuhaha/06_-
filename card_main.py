#! /anaconda3/bin/python3

import card_tools

# 无效循环，用户决定什么时候退出
while True:

    # 显示功能菜单
    card_tools.show_menu()

    action_str = input("请输入希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            card_tools.new_card()
        # 显示全部
        elif action_str == "2":
            card_tools.show_all()
        # 查询名片
        elif action_str == "3":
            card_tools.search_card()

    # 0 退出系统
    elif action_str == "0":

        print("欢迎再次使用【名片管理系统】")

        break
    # 其它内容输入错误，需要提示用户
    else:
        print("您输入的不正常，请重新选择")
