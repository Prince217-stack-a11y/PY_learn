import json
from pathlib import Path

todo_path = Path(__file__).with_name("todo_example.json")

todos = [{"title": "学习 JSON", "done": False,},{"title": "完成 Todo 持久化","done": True}]

with todo_path.open("w", encoding="utf-8") as file:
    json.dump(todos, file, ensure_ascii=False, indent=3)

with todo_path.open("r", encoding="utf-8") as file:
    loaded_todos = json.load(file)

print("读取到的任务：")

for todo in loaded_todos:
    mark = "[x]" if todo["done"] else "[ ]"
    print(f"{mark} {todo['title']}")



#加入内容重新覆盖
loaded_todos.append({"title": "学习文件持久化", "done": False})

with todo_path.open("w", encoding="utf-8") as file:
    json.dump(loaded_todos, file, ensure_ascii=False, indent=3)

print("追加后再次读取：")

with todo_path.open("r", encoding="utf-8") as file:
    final_todos = json.load(file)

for todo in final_todos:
    mark = "[x]" if todo["done"] else "[ ]"
    print(f"{mark} {todo['title']}")