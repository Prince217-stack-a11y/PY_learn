# Todo List 基线版（无持久化）
# 你的任务：给它加 JSON 持久化——数据存进 todo.json，重启不丢
# 需要你动手的位置都标了 TODO，共 3 处；套路见 Day 17 讲解第 4 节

import json
from pathlib import Path

todo_path = Path(__file__).resolve().parent / "todo.json"

todos = []  # TODO 第 1 处：启动时改为「todo.json 存在就 json.load 读回来，不存在保持空列表」
# 每个任务的结构：{"task": "买牛奶", "done": False}


def add_task(text):
    todos.append({"task": text, "done": False})
    print(f"已添加：{text}")


def list_tasks():
    if not todos:
        print("（还没有任务）")
        return
    for i, t in enumerate(todos, start=1):
        mark = "x" if t["done"] else " "
        print(f"{i}. [{mark}] {t['task']}")


def finish_task(index):
    # index 是用户输入的字符串：先转 int，再检查范围
    if not index.isdigit():
        print("请输入数字")
        return
    i = int(index)
    if 1 <= i <= len(todos):
        todos[i - 1]["done"] = True
        print(f"已完成：{todos[i - 1]['task']}")
    else:
        print("没有这一项")


def delete_task(index):
    if not index.isdigit():
        print("请输入数字")
        return
    i = int(index)
    if 1 <= i <= len(todos):
        removed = todos.pop(i - 1)
        print(f"已删除：{removed['task']}")
    else:
        print("没有这一项")


MENU = """
1. 添加任务
2. 查看任务
3. 完成任务
4. 删除任务
5. 退出
"""

while True:
    print(MENU)
    choice = input("请选择：").strip()

    if choice == "1":
        text = input("任务内容：").strip()
        if text:
            add_task(text)
            # TODO 第 3 处：数据变了，记得保存
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        list_tasks()
        finish_task(input("完成第几项：").strip())
        # TODO 第 3 处：数据变了，记得保存
    elif choice == "4":
        list_tasks()
        delete_task(input("删除第几项：").strip())
        # TODO 第 3 处：数据变了，记得保存
    elif choice == "5":
        print("再见！")
        break
    else:
        print("无效选择，请输入 1-5")
