# 06 自建 Agent 框架

> **教材**：第 7 章《构建你的 Agent 框架》
> **源码**：`code/chapter7/{my_llm.py, my_simple_agent.py, my_react_agent.py, my_calculator_tool.py, my_advanced_search.py, test_*.py}`；框架仓库 [jjyaoao/helloagents](https://github.com/jjyaoao/helloagents)
> **一句话**：从"使用者"转向"构建者"，从零构建 **HelloAgents** 框架；核心原则是"**分层解耦、职责单一、接口统一**"，核心理念是"**除了核心 Agent 类，一切皆为 Tools**"。

---

## 6.1 框架整体架构设计（第 7.1 节）

### 6.1.1 为何需要自建 Agent 框架

**（1）市面框架的快速迭代与局限性**（四点）：
- **过度抽象的复杂性**：许多框架为追求通用性引入大量抽象层与配置选项（如 LangChain 链式调用机制虽灵活，但对初学者学习曲线陡峭）。
- **快速迭代带来的不稳定性**：商业化框架为抢市场，API 变更频繁，版本升级后代码可能无法运行。
- **黑盒化的实现逻辑**：核心逻辑封装过严，难以理解内部机制、缺乏深度定制能力。
- **依赖关系的复杂性**：成熟框架携带大量依赖包，体积庞大，易与其他项目产生依赖冲突。

**（2）从使用者到构建者的能力跃迁**（三点价值）：
- **深度理解 Agent 工作原理**：亲手实现每个组件，真正理解思考过程、工具调用机制、各设计模式的好坏。
- **获得完全的控制权**：对每一行代码都有完全掌控，可精确调优。
- **培养系统设计能力**：涉及模块化设计、接口抽象、错误处理等软件工程核心技能。

**（3）定制化需求与深度掌握的必要性**：特定领域优化（金融/医疗/教育的提示词模板、特殊工具、定制安全策略）、性能与资源的精确控制、学习与教学的透明性。

### 6.1.2 HelloAgents 框架的设计理念（全书灵魂）

围绕一个核心问题：**如何让学习者既能快速上手，又能深入理解 Agent 的工作原理？** 形成四条设计理念：

1. **轻量级与教学友好的平衡**——"除了 OpenAI 的官方 SDK 和几个必要的基础库外，不引入任何重型依赖。如果遇到问题，可以直接定位到框架本身的代码，而不需要在复杂的依赖关系中寻找答案。"
2. **基于标准 API 的务实选择**——"OpenAI 的 API 已经成为了行业标准……我们选择在这个标准之上构建，而不是重新发明一套抽象接口。"（好处：兼容性保证 + 学习成本降低）
3. **渐进式学习路径的精心设计**——"我们将会把每一章的学习代码，保存为一个可以 pip 下载的历史版本。"每一步升级都自然而然，不产生概念跳跃。
4. **统一的"工具"抽象：万物皆为工具**——**"除了核心的 Agent 类，一切皆为 Tools。"** 在其他框架中需独立学习的 Memory、RAG、RL、MCP 等模块，在 HelloAgents 中**统一抽象为一种"工具"**。
   > "这种设计的初衷是消除不必要的抽象层，让学习者可以回归到最直观的'智能体调用工具'这一核心逻辑上。"

> **这是理解后面所有章节的钥匙**：记忆是工具、检索是工具、协议是工具、评估是工具、训练是工具。

### 6.1.3 目录结构（第 7.1.3 节）

```
hello-agents/
├── hello_agents/
│   │
│   ├── core/                     # 核心框架层
│   │   ├── agent.py              # Agent 基类
│   │   ├── llm.py                # HelloAgentsLLM 统一接口
│   │   ├── message.py            # 消息系统
│   │   ├── config.py             # 配置管理
│   │   └── exceptions.py         # 异常体系
│   │
│   ├── agents/                   # Agent 实现层
│   │   ├── simple_agent.py       # SimpleAgent 实现
│   │   ├── react_agent.py        # ReActAgent 实现
│   │   ├── reflection_agent.py   # ReflectionAgent 实现
│   │   └── plan_solve_agent.py   # PlanAndSolveAgent 实现
│   │
│   └── tools/                    # 工具系统层
│       ├── base.py               # 工具基类
│       ├── registry.py           # 工具注册机制
│       ├── chain.py              # 工具链管理系统
│       ├── async_executor.py     # 异步工具执行器
│       └── builtin/              # 内置工具集
│           ├── calculator.py     # 计算工具
│           └── search.py         # 搜索工具
```

**核心设计原则：分层解耦、职责单一、接口统一。**

### 6.1.4 快速开始（30 秒体验）

```bash
# Python 版本需要 >= 3.10
pip install "hello-agents==0.1.1"
```

```python
from hello_agents import SimpleAgent, HelloAgentsLLM
from dotenv import load_dotenv

load_dotenv()

# 创建 LLM 实例——框架自动检测 provider
llm = HelloAgentsLLM()
# 或手动指定： llm = HelloAgentsLLM(provider="modelscope")

# 创建 SimpleAgent
agent = SimpleAgent(
    name="AI助手",
    llm=llm,
    system_prompt="你是一个有用的AI助手"
)

response = agent.run("你好！请介绍一下自己")
print(response)
print(f"历史消息数: {len(agent.get_history())}")
```

**两种学习方式**：① **体验式**——直接 pip 安装跑示例；② **深度学习**——跟随章节从零实现每个组件。
> 建议"**先体验，后实现**"：先跑示例，再重写核心函数并运行测试文件（`test_*.py`）验证实现是否正确。

---

## 6.2 HelloAgentsLLM 扩展（第 7.2 节）

三条升级线：**多提供商支持、本地模型集成、自动检测机制**。

### 6.2.1 支持多提供商（通过继承，不改库源码）

```python
from hello_agents import HelloAgentsLLM
from openai import OpenAI
import os

class MyLLM(HelloAgentsLLM):
    """通过继承扩展 provider，而不是修改已安装的库源码。"""
    def __init__(self, model=None, api_key=None, base_url=None, provider=None, **kwargs):
        if provider == "modelscope":
            # 自行解析凭证
            self.model = model or "Qwen/Qwen2.5-VL-72B-Instruct"
            self._client = OpenAI(
                api_key=os.getenv("MODELSCOPE_API_KEY"),
                base_url="https://api-inference.modelscope.cn/v1/",
            )
        else:
            super().__init__(model=model, api_key=api_key,
                             base_url=base_url, provider=provider, **kwargs)
        # think 等方法从父类继承，无需重写
```

> ⚠️ **"直接修改已安装的库源码是一种不被推荐的做法，因为它会使后续的库升级变得困难。"** 要用继承 + `super().__init__(...)` 保留原有功能。

### 6.2.2 本地模型调用

```bash
# VLLM（生产级：连续批处理、PagedAttention）
pip install vllm
python -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen1.5-0.5B-Chat --host 0.0.0.0 --port 8000
# 服务地址：http://localhost:8000/v1

# Ollama（默认端口 11434）
ollama run llama3
# 服务地址：http://localhost:11434/v1
```

```python
llm = HelloAgentsLLM(provider="vllm", model="Qwen/Qwen1.5-0.5B-Chat",
                     base_url="http://localhost:8000/v1", api_key="vllm")
# 或只设 LLM_BASE_URL / LLM_API_KEY 后 HelloAgentsLLM() 自动检测
```

> ⚠️ Transformers 本地推理适合入门学习与功能验证，**但高并发性能有限，通常不作为生产环境首选**。

### 6.2.3 自动检测机制

`_auto_detect_provider` 与 `_resolve_credentials` 协同，检测优先级：
1. **最高**：检查特定服务商环境变量（`MODELSCOPE_API_KEY`、`OPENAI_API_KEY`、`ZHIPU_API_KEY`…）。
2. **次高**：根据 `base_url` 判断——**域名匹配**（`api-inference.modelscope.cn`、`open.bigmodel.cn` 等）；**端口匹配**（`:11434` → Ollama、`:8000` → VLLM、其他本地端口 → `local`）。
3. **辅助**：分析 API 密钥格式（如 `ms-` 前缀）——"由于这种方式可能存在模糊性（例如多个服务商的密钥格式相似），因此它的优先级较低，仅作为辅助手段"。
4. **默认**：返回 `'auto'`，使用通用配置。

```bash
# .env 无需配 provider 与 api_key，框架自动识别 Ollama
LLM_BASE_URL="http://localhost:11434/v1"
LLM_MODEL_ID="llama3"
```

> "如上表 7.1 所示，这种演进体现了框架设计的重要原则：**从简单开始，逐步完善**。"

---

## 6.3 框架接口实现（第 7.3 节）

### 6.3.1 Message 类

```python
from pydantic import BaseModel
from typing import Literal, Optional
import time

class Message(BaseModel):
    """基于 pydantic；role 严格限定取值，直接对应 OpenAI API 规范。"""
    content: str
    role: Literal["user", "assistant", "system", "tool"]
    timestamp: float = time.time()
    metadata: dict = {}

    def to_dict(self) -> dict:
        """输出 OpenAI 兼容格式——「对内丰富，对外兼容」。"""
        return {"role": self.role, "content": self.content}
```

> `MessageRole = Literal["user","assistant","system","tool"]` 严格限制取值；`to_dict()` 体现"**对内丰富，对外兼容**"的设计原则。

### 6.3.2 Config 类

```python
from dataclasses import dataclass, field
import os

@dataclass
class Config:
    """分组配置，均有合理默认值 → 零配置下也能工作。"""
    # LLM 配置
    default_model: str = "gpt-4o-mini"
    default_provider: str = "auto"
    temperature: float = 0.0
    max_tokens: int = 2048
    # 系统配置
    debug: bool = False
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> "Config":
        """环境变量可覆盖默认配置。"""
        return cls(
            default_model=os.getenv("LLM_MODEL_ID", cls.default_model),
            default_provider=os.getenv("LLM_PROVIDER", cls.default_provider),
            debug=os.getenv("DEBUG", "false").lower() == "true",
        )
```

### 6.3.3 Agent 抽象基类

```python
from abc import ABC, abstractmethod
from typing import List, Optional

class Agent(ABC):
    """抽象基类，不能直接实例化。"""
    def __init__(self, name: str, llm: HelloAgentsLLM,
                 system_prompt: str, config: Optional[Config] = None):
        self.name = name
        self.llm = llm
        self.system_prompt = system_prompt
        self.config = config or Config()
        self._history: List[Message] = []

    @abstractmethod
    def run(self, input_text: str, **kwargs) -> str:
        """强制所有子类实现此方法，保证所有智能体都有统一的执行入口。"""
        ...

    def add_message(self, message: Message):
        self._history.append(message)

    def get_history(self) -> List[Message]:
        return self._history.copy()

    def clear_history(self):
        self._history.clear()

    def __str__(self) -> str:
        return f"Agent(name={self.name}, history={len(self._history)})"
```

> `@abstractmethod` 的作用：**"强制所有子类必须实现此方法，从而保证了所有智能体都有统一的执行入口"**——这是"接口统一"原则的落点。

---

## 6.4 Agent 范式的框架化实现（第 7.4 节）

重构三目标：**提示词工程的系统性提升、接口与格式的标准化统一、高度可配置的自定义能力**。

### 6.4.1 SimpleAgent（工具调用循环）

`run(input_text, max_tool_iterations=3)` 流程：
1. 构建消息（系统提示 + 历史 + 当前用户消息）。
2. `_get_enhanced_system_prompt()` 在启用工具时把工具描述与调用格式写进系统提示：`` `[TOOL_CALL:{tool_name}:{parameters}]` ``。
3. 未启用工具 → 直接 `llm.invoke`；启用工具 → 进入 `_run_with_tools` 循环：
   - 调用 LLM → `_parse_tool_calls` 解析 → 执行所有工具并收集结果 → 从响应中移除调用标记 → 追加 assistant 消息与 `工具执行结果: ... 请基于这些结果给出完整的回答。` → 进入下一轮。
   - 直到无工具调用或达到最大迭代次数。

```python
import re

class SimpleAgent(Agent):
    def run(self, input_text: str, max_tool_iterations: int = 3) -> str:
        messages = self._build_messages(input_text)      # system + history + user
        system_prompt = self._get_enhanced_system_prompt()  # 含工具描述与格式

        if not self.has_tools():
            return self.llm.invoke(messages, system_prompt=system_prompt)

        for _ in range(max_tool_iterations):
            response = self.llm.invoke(messages, system_prompt=system_prompt)
            tool_calls = self._parse_tool_calls(response)   # 正则解析
            if not tool_calls:
                return response

            results = []
            for name, params in tool_calls:
                results.append(f"[{name}] {self._execute_tool_call(name, params)}")

            # 移除调用标记，追加结果，让 LLM 基于结果继续
            clean = self._remove_tool_markers(response)
            messages.append({"role": "assistant", "content": clean})
            messages.append({"role": "user",
                "content": "工具执行结果：\n" + "\n".join(results) +
                           "\n请基于这些结果给出完整的回答。"})
        return "已达到最大工具调用迭代次数。"

    def _parse_tool_calls(self, text: str):
        # 正则： [TOOL_CALL:tool_name:parameters]
        return re.findall(r'\[TOOL_CALL:([^:]+):([^\]]+)\]', text)
```

关键细节：`_execute_tool_call` 对 calculator 直接传表达式；其他工具走 `_parse_tool_parameters`（支持 `key=value`、`action=search,query=Python,limit=3`，或按工具类型智能推断为 `{'query': ...}` / `{'action':'search','query':...}` / `{'input': ...}`）。此外还有 `stream_run` 流式生成器和 `add_tool`/`has_tools`/`remove_tool`/`list_tools`。

### 6.4.2 ReActAgent

提示词 `MY_REACT_PROMPT` 保留原格式并强调"每次只能执行一个步骤"，明确两种 Action：`- {{tool_name}}[{{tool_input}}]` 与 `- Finish[最终答案]`。

```python
class ReActAgent(Agent):
    def run(self, input_text: str, max_steps: int = 5) -> str:
        current_history = ""
        for step in range(max_steps):
            prompt = MY_REACT_PROMPT.format(
                tools=self.tool_registry.get_tools_description(),
                question=input_text,
                history=current_history,
            )
            response = self.llm.invoke([{"role": "user", "content": prompt}])
            thought, action = self._parse_output(response)

            if action.startswith("Finish"):
                return self._parse_action_input(action)      # 返回最终答案

            tool_name, tool_input = self._parse_action(action)
            observation = self.tool_registry.execute_tool(tool_name, tool_input)
            current_history += f"\nThought: {thought}\nAction: {action}\nObservation: {observation}"
        return "抱歉，我无法在限定步数内完成这个任务。"
```

> 核心改进：**利用了统一的 `ToolRegistry` 接口**（而非自己管理工具）。

### 6.4.3 ReflectionAgent（通用化提示词）

```python
DEFAULT_PROMPTS = {
    "initial": "请完成以下任务：\n{task}",
    "reflect": "请审视以下回答，指出不足并给出改进建议。如果回答已经很好，请回答'无需改进'。\n任务：{task}\n回答：{answer}",
    "refine": "请根据反馈改进以下回答。\n任务：{task}\n原回答：{answer}\n反馈：{feedback}",
}

class ReflectionAgent(Agent):
    def __init__(self, name, llm, system_prompt, max_iterations=3, custom_prompts=None):
        super().__init__(name, llm, system_prompt)
        self.prompts = {**DEFAULT_PROMPTS, **(custom_prompts or {})}
        self.max_iterations = max_iterations
```

通过 `custom_prompts` 参数支持**深度定制**。

### 6.4.4 PlanAndSolveAgent

"**强制要求 Planner 以 Python 列表的格式输出计划，并提供了完整的异常处理机制。**"
- `DEFAULT_PLANNER_PROMPT` 要求输出形如 `["步骤1", "步骤2", ...]`。
- `DEFAULT_EXECUTOR_PROMPT` 要求"仅输出该步骤的最终答案，不要输出任何额外的解释或对话"。

### 6.4.5 FunctionCallAgent（0.2.8 之后引入）

基于 **OpenAI 原生函数调用**机制，能力方法：`_build_tool_schemas`（由工具 description 构建 schema）、`_extract_message_content`、`_parse_function_call_arguments`、`_convert_parameter_types`。

```python
class FunctionCallAgent(Agent):
    def _invoke_with_tools(self, messages):
        tools = self._build_tool_schemas()               # 由工具生成 OpenAI schema
        response = self.llm._client.chat.completions.create(
            model=self.llm.model, messages=messages,
            tools=tools, tool_choice="auto",
        )
        return response
```

> **"对比使用 prompt 约束的方式，具备更强的鲁棒性。"** —— 这是从"提示词约束格式"升级到"原生 Function Calling"的关键一步。

---

## 6.5 工具系统（第 7.5 节）

三个目标：统一的工具抽象与管理、实战驱动的工具开发、高级整合与优化策略。

### 6.5.1 工具基类与注册机制设计

```python
from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import List, Dict, Any

class ToolParameter(BaseModel):
    name: str
    type: str
    description: str
    required: bool = True
    default: Any = None

class Tool(ABC):
    """所有工具的统一抽象：字典进、字符串出 + 自描述。"""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, parameters: Dict[str, Any]) -> str:
        """接受字典参数并返回字符串结果——统一执行方式。"""
        ...

    @abstractmethod
    def get_parameters(self) -> List[ToolParameter]:
        """自描述能力——为自动化文档生成与参数验证提供基础。"""
        ...

class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Tool] = {}
        self._functions: Dict[str, callable] = {}

    def register_tool(self, tool: Tool):
        if tool.name in self._tools:
            print(f"警告：工具 '{tool.name}' 已存在，将被覆盖。")
        self._tools[tool.name] = tool

    def register_function(self, name: str, description: str, func: callable):
        """简单工具可直接注册函数。"""
        self._functions[name] = {"description": description, "func": func}

    def get_tools_description(self) -> str:
        """无工具时返回「暂无可用工具」；可直接用于构建 Agent 提示词。"""
        if not self._tools and not self._functions:
            return "暂无可用工具"
        return "\n".join(f"- {n}: {t.description}" for n, t in self._tools.items())

    def to_openai_schema(self) -> list:
        """转换为 OpenAI Function Calling schema。"""
        ...
```

**设计要点**：
- **两种注册方式**：Tool 对象（复杂工具，完整参数定义与验证） vs 函数直接注册（简单工具）。
- ⚠️ **`to_openai_schema()` 的坑**：**OpenAI schema 不支持 `default` 字段** → 需把默认值写进 description；`array` 类型要补 `items`。

### 6.5.2 自定义工具开发

以**安全计算器**为例（用 `ast` 白名单解析表达式，避免 `eval` 风险）：

```python
import ast, operator

class CalculatorTool(Tool):
    def __init__(self):
        super().__init__("my_calculator", "一个安全的计算器工具，支持基本数学运算")
        self._ops = {ast.Add: operator.add, ast.Sub: operator.sub,
                     ast.Mult: operator.mul, ast.Div: operator.truediv,
                     ast.Pow: operator.pow, ast.USub: operator.neg}

    def run(self, parameters: Dict[str, Any]) -> str:
        expr = parameters.get("expression", "")
        try:
            tree = ast.parse(expr, mode="eval")
            return str(self._eval(tree.body))
        except Exception as e:
            return f"计算错误：{e}"

    def _eval(self, node):
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.BinOp):
            return self._ops[type(node.op)](self._eval(node.left), self._eval(node.right))
        if isinstance(node, ast.UnaryOp):
            return self._ops[type(node.op)](self._eval(node.operand))
        raise ValueError("不支持的表达式")

    def get_parameters(self):
        return [ToolParameter(name="expression", type="string",
                              description="要计算的数学表达式，例如 (123+456)*789/12")]
```

### 6.5.3 多源搜索工具

`SearchTool` 支持三个后端：
- **hybrid**（智能选择）、**tavily**（专业 AI 搜索）、**serpapi**（传统 Google 搜索）。
- `_setup_backends` 根据可用 API 密钥与依赖库**自动选择**；`_search_hybrid` **优先 Tavily**，"如果 Tavily 失败，尝试 SerpApi"。

```bash
pip install "hello-agents[search]==0.1.1"
```

### 6.5.4 工具系统的高级特性

**（1）工具链（ToolChain）**

```python
class ToolChain:
    def __init__(self, name, description):
        self.steps = []
    def add_step(self, tool_name, input_template, output_key):
        self.steps.append({"tool": tool_name, "template": input_template, "key": output_key})
    def execute(self, registry, context):
        for step in self.steps:
            try:
                inp = step["template"].format(**context)     # 模板变量替换
            except KeyError as e:
                return f"❌ 工具链执行失败：模板变量 {e} 未找到"
            context[step["key"]] = registry.execute_tool(step["tool"], inp)
        return context

# 示例链 research_and_calculate：search → my_calculator
```

配合 `ToolChainManager`（`register_chain` / `execute_chain` / `list_chains`）。

**（2）异步工具执行器（AsyncToolExecutor）**

```python
from concurrent.futures import ThreadPoolExecutor
import asyncio

class AsyncToolExecutor:
    def __init__(self, max_workers=4):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    async def execute_tool_async(self, tool, params):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(self.executor, tool.run, params)

    async def execute_tools_parallel(self, tasks):
        return await asyncio.gather(*[self.execute_tool_async(t, p) for t, p in tasks])

    def __del__(self):
        self.executor.shutdown(wait=True)
```

> **设计理念**："每个工具都应该遵循单一职责原则……并将完善的异常处理和安全优先的输入验证作为基本要求"；性能上"利用异步执行提高并发处理能力，同时合理管理外部连接和系统资源"。

---

## 6.6 必须掌握 / 易踩的坑

- ✅ 演进主线：手写代码 → 低代码平台 → 成熟框架 → 自建框架，各自解决的痛点不同。
- ✅ HelloAgents 四条设计理念，尤其"**万物皆为工具**"。
- ✅ 目录三层：core / agents / tools。
- ✅ 三根柱子：`Agent` 抽象基类、`Tool` 抽象基类、`ToolRegistry`。
- ✅ Message 的"对内丰富、对外兼容"；Config 的"零配置也能工作"。
- ✅ 五种范式类：SimpleAgent、ReActAgent、ReflectionAgent、PlanAndSolveAgent、FunctionCallAgent。
- ⚠️ 别改库源码，用继承 + `super()` 扩展。
- ⚠️ OpenAI schema 不支持 `default` 字段，需写进 description；`array` 要补 `items`。
- ⚠️ 裸 transformers 不适合生产；生产用 VLLM/Ollama。
- ⚠️ 自动检测中密钥格式判断优先级低（可能模糊）。
- ⚠️ FunctionCallAgent 比 SimpleAgent 更鲁棒（用原生 Function Calling 而非提示词约束格式）。
- ⚠️ 异步执行器要记得 `shutdown(wait=True)` 释放资源。

## 6.7 一页速查（Q&A 自测）

1. 为什么要自建框架？→ 理解原理 + 完全控制 + 培养系统设计能力 + 满足定制需求。
2. HelloAgents 的核心设计理念一句话？→ 除了 Agent 类，一切皆为 Tools。
3. HelloAgents 的三根柱子？→ Agent 基类、Tool 基类、ToolRegistry。
4. 目录三层各是什么？→ core（核心）、agents（实现）、tools（工具）。
5. Message 的两种形态？→ 内部丰富（含 timestamp/metadata），对外 to_dict() 兼容 OpenAI。
6. Agent 为什么用抽象基类？→ 保证所有智能体都有统一的 run() 执行入口。
7. SimpleAgent 的工具调用标记格式？→ `[TOOL_CALL:tool_name:parameters]`。
8. 为什么要"先体验，后实现"？→ 先跑示例建立直觉，再重写并跑测试验证理解。
9. FunctionCallAgent 比 SimpleAgent 强在哪？→ 原生 Function Calling，格式更鲁棒。
10. 工具's 两个抽象方法？→ run(parameters)→str、get_parameters()→自描述。
11. to_openai_schema 的坑？→ OpenAI schema 不支持 default 字段，需写进 description。
