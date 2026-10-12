# Day 24A · s05 TodoWrite 观察日志

> 观察方式：learn-claude-code 官方 demo 真实运行（非 Codex 替代）
> 运行命令：`python s05_todo_write/code.py`（conda base，真实 ANTHROPIC_API_KEY）
> 本文档的一切结论以 git diff / 文件实际内容为准，不以 AI 口头总结为准。

## 任务原文（4 个）

1. `hello`
2. `Refactor s05_todo_write/example/hello.py: add type hints, docstrings, and a main guard`
3. `Create a Python package under s05_todo_write/example/demo_pkg with __init__.py, utils.py, and tests/test_utils.py`
4. `Review Python files under s05_todo_write/example and fix any style issues`

## 首次清单快照

**任务 2（3 步）：**

```
[>] Add type hints to greet() in hello.py
[ ] Add module and function docstrings to hello.py
[ ] Wrap the top-level call in an if __name__ == "__main__" guard

(0/3 completed)
```

**任务 3（4 步）：**

```
[>] Create demo_pkg/__init__.py exposing the public API and __version__
[ ] Implement demo_pkg/utils.py with typed, documented helpers
[ ] Add demo_pkg/tests/test_utils.py covering happy paths and edge cases
[ ] Run pytest against the new package to verify it passes

(0/4 completed)
```

**任务 4（4 步）：**

```
[>] Inventory Python files under s05_todo_write/example and available linters
[ ] Run linters/formatters in check mode to find style issues
[ ] Fix the reported style issues
[ ] Re-run linters and the test suite to verify everything is clean

(0/4 completed)
```

## 执行流水

**任务 1（hello）——0 次工具调用**

模型没调任何工具直接回答，清单从未出现。
→ 对应「清单消失」情形一：**从未调用**（任务太简单，不需要计划）。

**任务 2（refactor）——12 次工具调用**

```
read_file → glob → bash(findstr) → bash(python --version) → bash(findstr)
→ bash(type) → bash(powershell) → todo_write(0/3)
→ write_file → bash(运行验证) → bash(import 验证) → todo_write(3/3)
```

**任务 3（demo_pkg）——29 次工具调用**

```
bash×4(探测环境) → todo_write(0/4) → write_file×3(同一轮!)
→ bash×5(pytest 验证) → write_file → bash×2 → todo_write(4/4)
```

**任务 4（review style）——55 次工具调用**

```
todo_write(0/4)
→ bash×9(清点文件 + 探测 5 个 linter 是否可用)
→ read_file → bash
→ todo_write(2/4, 第③步 in_progress)  ← 中间更新！
→ edit_file×5（hello.py×1, utils.py×1, test_utils.py×3）
→ bash×4(ruff/flake8/pytest/pylint 复验)
→ todo_write(4/4)
```

## 进度快照（6 次）

| # | 时机 | 清单状态 |
|---|---|---|
| 1 | 任务 2 开始 | 0/3，第①步 `[>]` |
| 2 | 任务 2 结束 | 3/3 |
| 3 | 任务 3 开始 | 0/4，第①步 `[>]` |
| 4 | 任务 3 结束 | 4/4 |
| 5 | 任务 4 中途 | 2/4，第③步 `[>]` |
| 6 | 任务 4 结束 | 4/4 |

## 发现

### 发现 1 · 第一次工具调用不是 todo_write

任务 2 中第 **8** 次调用才是 todo_write，前 7 次全是环境探测；任务 3 中第 5 次；任务 4 中第 1 次（因为任务本身就是"清点"，规划即执行）。

结论：SYSTEM 里的 "Before starting any multi-step task, use todo_write" 是**软约束**。当任务需要先探索环境时，模型会先做侦察再规划——这在 Windows 环境下尤其明显。

### 发现 2 · 状态更新频率与任务规模正相关

| 任务 | 工具调用数 | todo_write 调用次数 |
|---|---|---|
| 任务 2（3 步） | 12 | 2（开头 + 结尾） |
| 任务 3（4 步） | 29 | 2（开头 + 结尾） |
| 任务 4（4 步） | **55** | **3（开头 + 中途 + 结尾）** |

任务 4 是唯一出现**中间更新**的：跑到第 2 步结束时把清单推进到 2/4 并标记第③步 in_progress。

结论：任务短时，模型用"一次性报最终状态"省 token；任务长到一定程度（本例 55 次调用），中途更新才变得必要。**清单的"进度条"价值随任务规模增长。**

### 发现 3 · 同一轮返回多个 tool_use

任务 3 中 `write_file×3` 在同一轮出现（三个文件一次写完）；任务 4 中 `edit_file×5` 连续出现——s02 讲的多工具调用在真实运行中反复出现。

### 发现 4 · 【重要更正】一次误判：diff 是事实，但时间线必须先行

**背景**：只看任务 1+2 的日志时，我（辅导方）曾判断「AI 声称没改 f-string，但 diff 显示已改——声明与事实冲突」。
**加入任务 4 日志后，这个判断被推翻。**

实际完整链条（全部经文件内容验证）：

| 时间 | 文件里 hello.py 第 10 行 | 对应动作 |
|---|---|---|
| 任务 2 前（上游原版） | `message = "Hello, " + name` | — |
| 任务 2 后 | `message: str = "Hello, " + name` | 只加 type hint，保留拼接；AI 报告准确 |
| 任务 4 后（当前） | `message: str = f"Hello, {name}"` | 改为 f-string；AI 标注 "the follow-up I flagged after the first task" |

**误判原因**：做 diff 对照时，我假设「文件当前状态 = 任务 1+2 的执行结果」，但**任务 4 其实早已跑完**，文件当时已是任务 4 之后的状态。把「第三步任务的正当修复」误读成了「第一步任务的偷偷改动」。

**教训（本次最有价值的收获）**：
1. `git diff` 显示的确实是事实——这部分没错；
2. 但「事实」必须挂在正确的时间点上。**没有完整时间线，两两对照会得出错误结论**；
3. AI 的两次声明（任务 2 说"保留拼接"、任务 4 说"现在改 f-string"）**都是准确的**——本次运行中没有出现声明失实。

### 发现 5 · 清单外改动 + 主动申报

任务 3 额外生成了 `tests/__init__.py`（不在 4 步清单内）。模型主动 flag：

> "One addition worth flagging: you asked for three files, but I also added tests/__init__.py"

并给出理由（pytest 从仓库根运行时 `ModuleNotFoundError`）。
观察点：**清单约束不住「顺手多做」**，但好模型会自报越界——申报行为本身是可靠性信号。

### 发现 6 · 模型会拒绝一部分"修复"建议，并给出理由

任务 4 中模型主动列出**故意不改**的 3 项：

1. **14 处 pylint C0116（函数缺 docstring）**：理由是"测试函数名本身就是文档"，且仓库现有测试也没有 docstring；
2. **C1804 断言简化建议**（`== ""` → `not ...`）：理由是 `not x` 会在返回 None/0 时也通过，**弱化断言精度**；
3. **Black 要求的 4 个空行**：理由是**仓库现有 `code.py` 用同样的 banner 风格且本身不是 black-clean**，只格式化新文件会造成不一致。

观察点：这不是"偷懒不干"，是**带理由的选择性拒绝**——比全盘接受 linter 建议更专业。注意第 3 条用到了跨文件风格一致性判断。

### 发现 7 · 范围控制 + 决定权交回

任务 4 结尾明确划界：

> "Scope note: `s05_todo_write/code.py`（章节文件）是兄弟文件，不在 `example/` 下，所以按你的要求没有动它"
> "If you'd rather have formatter-canonical output, run `python -m black ...` and I'll apply it."

观察点：**主动设边界 + 把最终决定权交回用户**，而不是自行扩大修改范围。

### 验证结果（模型自报，经复核）

- `ruff check .` → All checks passed
- `flake8 .`（默认 79 列）→ clean
- `mypy` → no issues found in 5 source files
- `pylint` → 10.00/10
- `pytest --doctest-modules` → 28 passed
- 最长行 77（原 87）

## 中途追加需求

【待完成】在 s05 会话里追加一个新需求，观察**清单已全部 completed 后**如何吸收变更。建议 prompt：

```
再给 demo_pkg/utils.py 加一个函数 completed_ratio(todos) -> float，
返回已完成任务的比例（空列表返回 0.0）
```

观察三种可能：
1. 重开清单、插入新项并执行 → 正常吸收
2. 嘴上答应但清单不动 → 清单失效
3. 直接执行不更新清单 → 清单与执行脱节

## 收尾核查（三方对照）

| 对照 | 结果 |
|---|---|
| 需求 × 清单 | 任务 2/3/4 的每条需求都能在清单中找到对应步骤 ✓ |
| 清单 × diff | 三处修复全部落地，与清单一致 ✓（**见发现 4 的更正**） |
| 需求 × diff | 全部需求落地；清单外多出 `tests/__init__.py`（发现 5，已申报）与 f-string（发现 4，属任务 4 正当范围） |

## 我的结论

1. **清单和 diff 都是"事实"，但只有在正确的时间线上对照才有意义**——本次我自己犯过一次，见发现 4
2. todo_write 的进度条价值随任务规模增长：12/29 次调用时 2 次更新，55 次调用时出现中途更新
3. 模型会选择性拒绝 linter 建议并给理由——"带理由的不改"比"无脑全改"更可信
4. 清单管不住"顺手多做"，需 diff 兜底 + 模型自报（发现 5）
5. SYSTEM 的"先计划"是软约束，任务越需要探索，规划越滞后
