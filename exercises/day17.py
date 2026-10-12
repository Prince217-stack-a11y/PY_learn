# import JSON as js
#
# import data
#
# with open('data.json','a') as file:
#     js.dump('data.json',file)


# import json
#
# data = {"name": "小明","score": 88,"passed": True}
#
# text = json.dumps(data, ensure_ascii=False, indent=2)
#
# print(text)
# print(type(text))

# import json
#
# text = '{"name": "小明", "score": 88, "passed": true}'
#
# data = json.loads(text)
#
# print(data)
# print(type(data))
# print(data["name"])
#DeepSeek 接口返回
# {
#   "id": "chatcmpl-123",
#   "object": "chat.completion",
#   "created": 1789891200,
#   "model": "deepseek-chat",
#   "choices": [
#     {
#       "index": 0,
#       "message": {
#         "role": "assistant",
#         "content": "你好，我是 AI 助手。"此行是最主要数据！！！！！！！！！
#       },
#       "finish_reason": "stop"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 20,
#     "completion_tokens": 15,
#     "total_tokens": 35
#   }
# }
#层级关系
# response
# ├── id
# ├── model
# ├── choices
# │   └── 第 1 个候选结果
# │       ├── index
# │       ├── message
# │       │   ├── role
# │       │   └── content
# │       └── finish_reason
# └── usage
#     ├── prompt_tokens
#     ├── completion_tokens
#     └── total_tokens














#API练习
#要求：
# 学生数量
# 每个学生 ID
# 每个学生姓名
# 每个学生 Python 成绩
# 每个学生数学成绩
# 缺少成绩时输出“暂无成绩”
# repos_json = {
#   "code": 0,
#   "message": "success",
#   "data": {
#     "students": [
#       {
#         "id": "S001",
#         "name": "小明",
#         "scores": {
#           "python": 88,
#           "math": 76
#         }
#       },
#       {
#         "id": "S002",
#         "name": "小红",
#         "scores": {}
#       }
#     ]
#   }
# }
#
# students = repos_json["data"]["students"]
#
# print(f"学生数量：{len(students)}")
#
# for student in students:
#     student_id = student["id"]
#     name = student["name"]
#     scores = student.get("scores") or {}
#
#     py_score = scores.get("python")
#     mh_score = scores.get("math")
#
#     print(f"学生ID：{student_id}")
#     print(f"姓名：{name}")
#
#     if py_score is None:
#         print("Python成绩：暂无成绩")
#     else:
#         print(f"Python成绩：{py_score}")
#
#     if mh_score is None:
#         print("数学成绩：暂无成绩")
#     else:
#         print(f"数学成绩：{mh_score}")
#     print("-" * 30)
# #样例判断
# # 1. response 的外层是什么类型？字典
# # 2. data 是什么类型？字典
# # 3. orders 是什么类型？列表
# # 4. 单个 order 是什么类型？字典
# # 5. 真正的订单列表在第几层？第三层
# # 6. amount 为 null 时应该如何处理？添加if判断避免报错
# # 7. 为什么不能直接写 response["data"]["orders"]？因为 data 或 orders 可能缺失、为 None 或类型错误，应先判断 code，再使用 get() 和类型检查
# response_text = """
# {
#   "code": 0,
#   "message": "success",
#   "data": {
#     "page": 1,
#     "page_size": 3,
#     "total": 3,
#     "orders": [
#       {
#         "order_id": "O1001",
#         "customer": {
#           "name": "小明",
#           "city": "北京"
#         },
#         "status": "completed",
#         "amount": 199.5,
#         "items": [
#           {"name": "键盘", "quantity": 1},
#           {"name": "鼠标", "quantity": 2}
#         ]
#       },
#       {
#         "order_id": "O1002",
#         "customer": {
#           "name": "小红",
#           "city": "上海"
#         },
#         "status": "pending",
#         "amount": 88.0,
#         "items": []
#       },
#       {
#         "order_id": "O1003",
#         "customer": {
#           "name": "小刚"
#         },
#         "status": "cancelled",
#         "amount": null,
#         "items": [
#           {"name": "显示器", "quantity": 1}
#         ]
#       }
#     ]
#   }
# }
# """

# todojson化
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


def run_todo_list():
    todos = load_todos()

    while True:
        print()
        print("1. 添加任务 2. 列出任务 3. 标记完成 4. 删除任务 5. 退出")
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
                 break
            case _:
                 print("无效操作")

if __name__ == "__main__":
    run_todo_list()
















