# 重要子agent实现代码：   
- if block.type == "tool_use":
- if block.name == "task":
- desc = block.input.get("description", "subtask")
- prompt = block.input.get("prompt", "")
- print(f"> task ({desc}): {prompt[:80]}")
- output = run_subagent(prompt)
- else:
- handler = TOOL_HANDLERS.get(block.name)
- output = handler(**block.input) if handler else f"Unknown tool: {block.name}"
- print(f"  {str(output)[:200]}")
- results.append({"type": "tool_result", "tool_use_id": block.id, "content": str(output)})
- messages.append({"role": "user", "content": results})

- # 首先我认为，subagent像是一个可以帮助干脏任务以及运行大量占token且不重要的代码的额外之地，并且与主队话互不干扰，我觉得这点和codex其实有点区别，codex里是分叉技能保留前面内容但是从分叉出分指出一个独立对话框进行，其实更像他的侧边聊天最后可以并入主队话

# 观察：

- ## 何时被派出去：在收到task命令调用后
- ## 结果怎么回来：通过总结成一条summary
- ## 什么时候在主对话：在两端时，运行任务前和返回结果后，[Subagent started]上面，[Subagent started]后面
- ## 什么时候派了子 Agent：出现[Subagent started]，前面常出现[sub]
- ## 结果如何汇合：返回总结摘要->将信息汇入主信息列表->下一次loop循环即可看见