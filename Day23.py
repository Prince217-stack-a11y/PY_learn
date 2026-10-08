import json
from pathlib import Path

TODO_PATH = Path(__file__).with_name("todo.json")


def load_todos():
    if not TODO_PATH.exists():
        return []

    with open(TODO_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_todos(todos):
    with open(TODO_PATH, "w", encoding="utf-8") as file:
        json.dump(todos,file,ensure_ascii=False,indent=2,)


def add_todo(todos, title):
    for todo in todos:
        if todo["title"] == title:
            return False

    todos.append({"title": title, "done": False,})
    return True


def list_todos(todos):
    if not todos:
        print("暂无待办任务")
        return

    for index, todo in enumerate(todos, start=1):
        if todo["done"] == True:
            mark = "[x]"
        else:
            mark = "[ ]"
        print(f"{index}. {mark} {todo['title']}")


def complete_todo(todos, title):
    for todo in todos:
        if todo["title"] == title:
            todo["done"] = True
            return True

    return False


def delete_todo(todos, title):
    for index, todo in enumerate(todos):
        if todo["title"] == title:
            todos.pop(index)
            return True

    return False


def search_todos(todos, keyword):
    keyword = keyword.strip().lower()
    result_count = 0

    if keyword == "":
        print("请输入搜索关键词")
        return

    for index, todo in enumerate(todos, start=1):
        if keyword in todo["title"].lower():
            if todo["done"] == True:
                mark = "[x]"
            else:
                mark = "[ ]"
            print(f"{index}. {mark} {todo['title']}")
            result_count += 1

    if result_count == 0:
        print("未找到匹配任务")


def run_todo_list():
    todos = load_todos()

    while True:
        print()
        print("1. 添加任务 2. 列出任务 3. 标记完成 4. 删除任务 5. 搜索任务 6. 退出")
        print()

        choice = input("请选择：")
        match choice:
            case '1':
                 title = input("任务名称：")
                 if add_todo(todos, title):
                     save_todos(todos)
                     print("添加成功")
                 else:
                     print("任务已存在")
            case '2':
                 list_todos(todos)
            case '3':
                 title = input("要完成的任务：")
                 if complete_todo(todos, title):
                     save_todos(todos)
                     print("完成成功")
                 else:
                     print("未找到任务")
            case '4':
                 title = input("要删除的任务：")

                 if delete_todo(todos, title):
                     save_todos(todos)
                     print("删除成功")
                 else:
                     print("未找到任务")
            case '5':
                 keyword = input("搜索关键词：")
                 search_todos(todos, keyword)
            case '6':
                 break
            case _:
                 print("无效操作")

if __name__ == "__main__":
    run_todo_list()
