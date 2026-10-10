import save

from PY_learn.PY_learn.day17_json.todo_persist import add_task

tasks = []
while True:
    cmd = input("todo> ")
    if cmd == "add":   add_task(tasks)      # 函数 · Day 10
    elif cmd == "list": show(tasks)          # list 遍历 · Day 5
    elif cmd == "done": mark_done(tasks)       # dict 状态 · Day 6
    elif cmd == "quit":
        save(tasks)                        # JSON 持久化 · Day 17
        break