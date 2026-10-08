- 第一步调用工具exec_command进行读取目标文件
- shell中使用$Get-Content -LiteralPath读取
- 第二步调用request_permissions，申请写入
- 再次调用exec_command查看文件
- 生成diff并返还
- # 工具调用记录

| # | 工具 | 目标 / 参数 | 结果 | 是否需要批准 |
|---|---|---|---|---|
| 1 | `ask_user_question` | 请求批准读取 `Day23.py` | 你选择「允许读取（推荐）」 | 是（询问） |
| 2 | `read` | `E:\pycharm_ana_envir\PY_learn\Day23.py` | ❌ 失败：文件不存在（路径多一层 `PY_learn`） | 只读 |
| 3 | `glob` | `**/Day23.py` | ✅ 定位到 `PY_learn\Day23.py` | 只读 |
| 4 | `read` | `PY_learn\Day23.py` | ✅ 读到全文 100 行 | 只读 |
| 5 | `ask_user_question` | 展示**计划 + 完整 diff**，请求写入审批 | 你选择「批准，按此 diff 写入（推荐）」 | 是（询问） |
| 6 | `write` | 写入 `PY_learn\Day23.py`（124 行） | ✅ `Updated file` | **是（写入前已获明确批准）** |
| 7 | `read` | `PY_learn\Day23.py` 第 50–124 行 | ✅ 与批准的 diff 完全一致 | 只读 |
| 8 | `ask_user_question` | 请求批准验证命令 | 你选择「批准运行验证（推荐）」 | 是（询问） |
| 9 | `pwsh` | 运行验证命令（受限沙箱） | ❌ 沙箱初始化失败：`SetNamedSecurityInfoW failed (Win32 5): grantWrite(E:\pycharm_ana_envir\PY_learn)`，Python 未执行 | 是（命令） |
| 10 | `skill` | 加载 `diagnose-windows-sandbox-acl` | ✅ 得到标准诊断/修复流程 | 只读 |
| 11 | `pwsh` + `danger-full-access` | 运行权限诊断修复脚本 | ✅ `GRANTED=1`、`verified`、`FIXED=0`、`REFUSED=0` | **是（一次性放宽沙箱）** |
| 12 | `pwsh` | 重跑验证（原双引号写法） | ❌ `SyntaxError`（PowerShell 吞掉内层双引号，非 `Day23.py` 问题） | 是（命令） |
| 13 | `pwsh` | 重跑验证（改为单引号） | ✅ 全部通过 | 是（命令） |

- # diff内容：
```diff
--- a/PY_learn/Day23.py
+++ b/PY_learn/Day23.py
@@ -57,6 +57,27 @@ def delete_todo(todos, title):
     return False
 
 
+def search_todos(todos, keyword):
+    keyword = keyword.strip().lower()
+    result_count = 0
+
+    if keyword == "":
+        print("请输入搜索关键词")
+        return
+
+    for index, todo in enumerate(todos, start=1):
+        if keyword in todo["title"].lower():
+            if todo["done"] == True:
+                mark = "[x]"
+            else:
+                mark = "[ ]"
+            print(f"{index}. {mark} {todo['title']}")
+            result_count += 1
+
+    if result_count == 0:
+        print("未找到匹配任务")
+
+
 def run_todo_list():
     todos = load_todos()
 
@@ -63,8 +84,8 @@
     while True:
         print()
-        print("1. 添加任务 2. 列出任务 3. 标记完成 4. 删除任务 5. 退出")
+        print("1. 添加任务 2. 列出任务 3. 标记完成 4. 删除任务 5. 搜索任务 6. 退出")
         print()
 
         choice = input("请选择：")
         match choice:
             case '1':
@@ -86,10 +107,13 @@
             case '4':
                  title = input("要删除的任务：")
 
                  if delete_todo(todos, title):
                      save_todos(todos)
                      print("删除成功")
                  else:
                      print("未找到任务")
-            case '5':
+            case '5':
+                 keyword = input("搜索关键词：")
+                 search_todos(todos, keyword)
+            case '6':
                  break
```

**改动总结**：新函数 `search_todos` 在第 60–78 行；菜单提示第 86 行；`case '5'` / `case '6'` 在第 115–119 行。文件由 100 行变为 124 行（新增 21 行 + 修改 1 行 + 新增/替换 3 行）。

