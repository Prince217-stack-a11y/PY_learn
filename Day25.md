# 一、进行s08教材demo复现
- ## 发现：agent会倾向判断自己用了compact技能但是实际没有
- ## 压缩触发总结：
- ### 首先触发tool_result_budget，生成54个文件，用<persisted-output>替代
- ### 其次触发snip_compact28次，因为最大消息数设置为50所以触发较为频繁
- ### 再其次触发micro_compact520处，将tool-results缩写成一行引用，保留了最新 3 个结果
- ### 因为压缩后上下文字符数仍然超过限制，最后调用了一次compact_history进行全局摘要，调用了一次llm，利用一条 `[Compacted]` 消息替换当前历史。
- ## 最后我对他进行提问，问他核心的需求，他没有遗漏，问他全部的问题也没有遗漏
- [ 额外发现：我最后要求他进行todowrite填写，再次看到其读到prompt："Before starting any multi-step task, use todo_write to plan your steps. "并且进行todowrite函数滴用]
- ### 在完成todowrite过程中再次触发【auto compact】，保存transcript。整个过程不断回顾历史对话并区分对话方，然后触发压缩，最终把核心任务写成清单并核对完成
# 总结，压缩后记得核心需求但是不会主动提及较早的且非必要需求，如果进一步询问会回答出来



