# HOOK:
- ## Hook 是挂在 Agent 生命周期固定节点上的自动扩展逻辑。它可以在用户输入提交后、工具执行前后、Agent 准备结束时，执行日志、权限检查、副作用、收尾等操作。
- ## 为了Agent Loop 保持稳定，Hook 不直接写进 Agent Loop
- ## PreToolUse 通常在工具真正执行前进行检查
- ## Hook 和 Tool 区别：Hook由 Harness 在生命周期节点自动触发，Tool由模型主动决定调用
# Skill：
- ## 核心思想：启动时只告诉 Agent 有哪些技能真正需要时再加载完整技能内容
- ## Skill 内容在执行 load_skill() 之后进入messages

