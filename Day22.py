




# 最小可运行的 agent harness 内核
#
# def agent_loop(messages):
#     while True:
#         response = client.messages.create(
#             model=MODEL, system=SYSTEM, messages=messages,
#             tools=TOOLS, max_tokens=8000,
#         )
#         messages.append({"role": "assistant", "content": response.content})
#
#         if response.stop_reason != "tool_use":
#             return
#
#         results = []
#         for block in response.content:
#             if block.type == "tool_use":
#                 output = run_bash(block.input["command"])
#                 results.append({
#                     "type": "tool_result",
#                     "tool_use_id": block.id,
#                     "content": output,
#                 })
#         messages.append({"role": "user", "content": results})

