# from dotenv import load_dotenv
# import os
# from openai import OpenAI

# load_dotenv()
# client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
#                 base_url="https://api.deepseek.com")

# resp = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[{"role": "user", "content": "用一句话解释 list"}],
# )
# print(resp.choices[0].message.content)
# print(resp.usage)   # 看账单
# print(type(client))
# print(type(client.chat))
# print(type(client.chat.completions))
# print(type(client.chat.completions.create))
#第一次练习
# import os
# import sys
# from pathlib import Path

# import requests
# from dotenv import load_dotenv

# API_URL = "https://api.deepseek.com/chat/completions"
# MODEL = "deepseek-chat"   
# TIMEOUT = 60              

# SYSTEM_PROMPT = "你是一个简洁友好的中文助手，回答控制在 100 字以内。"


# def load_api_key():
#     """从本文件同目录的 .env 读取 DEEPSEEK_API_KEY。"""
   
#     env_path = Path(__file__).parent / ".env"
#     load_dotenv(env_path)

#     api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
#     if not api_key:
#         print("错误：没有读到 API Key。")
#         print("请在 chat_cli.py 同目录创建 .env 文件，内容如下（换成真实密钥）：")
#         print("  DEEPSEEK_API_KEY=sk-xxxxxxxx")
#         print("密钥申请地址：https://platform.deepseek.com")
#         sys.exit(1)
#     return api_key


# def chat(messages, api_key):
#     """调用 DeepSeek 接口，返回 (回复文本, usage 字典)。

#     注意：messages 是整个对话历史，每次请求都全量发送——
#     LLM 本身无状态，服务器不记得上一轮说过什么。
#     """
#     payload = {
#         "model": MODEL,
#         "messages": messages,
#     }
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json",
#     }

#     try:
#         resp = requests.post(API_URL, json=payload, headers=headers, timeout=TIMEOUT)
#     except requests.ConnectionError:
#         print("[网络错误] 连不上 api.deepseek.com，检查网络或代理后重试。")
#         return None, None
#     except requests.Timeout:
#         print(f"[网络错误] 超过 {TIMEOUT} 秒没有响应，已放弃本次请求。")
#         return None, None

#     # ---- HTTP 状态码分类处理 ----
#     if resp.status_code == 401:
#         print("[401] API Key 无效：检查 .env 里的密钥是否复制完整，修好后重新运行。")
#         return None, None
#     if resp.status_code == 402:
#         print("[402] 账户余额不足：去 https://platform.deepseek.com 充值。")
#         return None, None
#     if resp.status_code == 429:
#         print("[429] 请求太频繁：等几秒再发。")
#         return None, None
#     if resp.status_code != 200:
#         print(f"[HTTP {resp.status_code}] 意外响应：{resp.text[:200]}")
#         return None, None

#     # ---- 响应结构检查----
#     try:
#         data = resp.json()
#     except ValueError:
#         print(f"[解析失败] 响应不是 JSON：{resp.text[:200]}")
#         return None, None

#     choices = data.get("choices")
#     if not choices:
#         print("[空回复] 接口通了但 choices 为空，原始响应：")
#         print(data)
#         return None, None

#     content = choices[0].get("message", {}).get("content", "").strip()
#     if not content:
#         print(f"[空回复] finish_reason={choices[0].get('finish_reason')}，原始响应：")
#         print(data)
#         return None, None

#     usage = data.get("usage", {})
#     return content, usage


# def print_stats(messages, usage, round_no):
#     """每轮打印 messages 增长情况和 token 用量。"""
#     role_count = {}
#     for m in messages:
#         role_count[m["role"]] = role_count.get(m["role"], 0) + 1

#     detail = " + ".join(f"{role} {n} 条" for role, n in role_count.items())
#     print(f"--- [第 {round_no} 轮] messages 共 {len(messages)} 条（{detail}）")
#     if usage:
       
#         print(f"--- [用量] 本轮发送 prompt_tokens={usage.get('prompt_tokens')}"
#               f"，回复 completion_tokens={usage.get('completion_tokens')}")


# def main():
#     api_key = load_api_key()

    
#     messages = [{"role": "system", "content": SYSTEM_PROMPT}]

#     print("=" * 50)
#     print("DeepSeek CLI 聊天机器人（Day 21）")
#     print("输入 exit / quit / 退出 结束对话")
#     print("=" * 50)

#     round_no = 0
#     while True:
#         try:
#             user_input = input("\n你> ").strip()
#         except (KeyboardInterrupt, EOFError):
#             print("\n再见！")
#             break

#         if not user_input:
#             continue
#         if user_input.lower() in ("exit", "quit", "退出"):
#             print("再见！")
#             break

#         round_no += 1

       
#         messages.append({"role": "user", "content": user_input})

       
#         reply, usage = chat(messages, api_key)

#         if reply is None:
            
#             messages.pop()
#             round_no -= 1
#             continue

        
#         messages.append({"role": "assistant", "content": reply})

#         print(f"\nAI> {reply}")
#         print_stats(messages, usage, round_no)


# if __name__ == "__&#8203;main__":
#     main()






#第二次聊天机器人练习
# import os
# from pathlib import Path
#
# import openai
# from openai import OpenAI
# from dotenv import load_dotenv
#
# BASE_DIR = Path(__file__).resolve().parent
# ENV_PATH = BASE_DIR / ".env"
#
# DEFAULT_BASE_URL = "https://api.deepseek.com"
# DEFAULT_MODEL = "deepseek-chat"
#
# SYSTEM_PROMPT = "你是一个简洁、准确的 Python 助手。"
#
# #从 .env 读取 SDK 配置。
# def load_config():
#
#     load_dotenv(ENV_PATH)
#
#     api_key = (os.getenv("DEEPSEEK_API_KEY") or "").strip()
#     base_url = (
#         os.getenv("DEEPSEEK_BASE_URL") or DEFAULT_BASE_URL
#     ).strip()
#     model = (
#         os.getenv("DEEPSEEK_MODEL") or DEFAULT_MODEL
#     ).strip()
#
#     return api_key, base_url, model
#
#
# def create_client(api_key, base_url):
#     """创建 DeepSeek 兼容的 OpenAI SDK 客户端"""
#     return OpenAI(
#         api_key=api_key,
#         base_url=base_url,
#         timeout=60.0,
#         max_retries=0,
#     )
#
#
# def make_system_message():
#     """创建 system 消息。"""
#     return {
#         "role": "system",
#         "content": SYSTEM_PROMPT,
#     }
#
#
# def send_message(client, messages, model):
#     """通过 chat.completions 发送完整消息历史。"""
#     try:
#         response = client.chat.completions.create(
#             model=model,
#             messages=messages,
#             stream=False,
#         )
#
#     except openai.AuthenticationError as error:
#         print("认证失败：请检查 DEEPSEEK_API_KEY 是否正确")
#         print(f"错误信息：{error}")
#         return None
#
#     except openai.APITimeoutError as error:
#         print("请求超时：请检查网络或适当增大 timeout")
#         print(f"错误信息：{error}")
#         return None
#
#     except openai.APIConnectionError as error:
#         print("连接失败：请检查网络和 DEEPSEEK_BASE_URL")
#         print(f"错误信息：{error}")
#         return None
#
#     except openai.APIStatusError as error:
#         message = getattr(error, "message", str(error))
#         print(
#             f"API 返回错误状态码 {error.status_code}："
#             f"{message}"
#         )
#         return None
#
#     except openai.OpenAIError as error:
#         print(f"SDK 请求失败：{error}")
#         return None
#
#     if not response.choices:
#         print("API 没有返回任何候选回答")
#         return None
#
#     message = response.choices[0].message
#     reply = message.content
#
#     if not isinstance(reply, str) or not reply.strip():
#         print("API 返回了空回答")
#         return None
#
#     return reply, response.usage
#
#
# def print_usage(usage):
#     """输出 Token 使用量。"""
#     if usage is None:
#         print("Token 使用量：暂无数据")
#         return
#
#     prompt_tokens = getattr(usage, "prompt_tokens", "未知")
#     completion_tokens = getattr(
#         usage,
#         "completion_tokens",
#         "未知",
#     )
#     total_tokens = getattr(usage, "total_tokens", "未知")
#
#     print(
#         "Token 使用量："
#         f"输入 {prompt_tokens}，"
#         f"输出 {completion_tokens}，"
#         f"总计 {total_tokens}"
#     )
#
#
# def print_history(messages):
#     """显示当前消息历史。"""
#     print(f"当前历史共 {len(messages)} 条消息")
#
#     for index, message in enumerate(messages, start=1):
#         role = message.get("role", "unknown")
#         content = str(message.get("content", ""))
#         preview = content.replace("\n", " ")[:80]
#
#         print(f"{index}. {role}: {preview}")
#
#
# def run_chat():
#     """运行命令行多轮聊天。"""
#     api_key, base_url, model = load_config()
#
#     if not api_key:
#         print(f"API Key 未配置，请检查：{ENV_PATH}")
#         return
#
#     client = create_client(api_key, base_url)
#
#     print("SDK 配置加载成功")
#     print(f"Base URL：{base_url}")
#     print(f"模型：{model}")
#     print("命令：/reset、/history、/usage、/exit")
#     print()
#
#     messages = [
#         make_system_message(),
#     ]
#
#     last_usage = None
#
#     while True:
#         try:
#             user_input = input("你：").strip()
#         except (EOFError, KeyboardInterrupt):
#             print("\nBye")
#             break
#
#         if not user_input:
#             continue
#
#         command = user_input.lower()
#
#         if command in {"/exit", "/quit", "exit", "quit"}:
#             print("Bye")
#             break
#
#         if command == "/reset":
#             messages.clear()
#             messages.append(make_system_message())
#             last_usage = None
#             print("对话历史已重置，只保留 system 消息")
#             continue
#
#         if command == "/history":
#             print_history(messages)
#             continue
#
#         if command == "/usage":
#             print_usage(last_usage)
#             continue
#
#         user_message = {
#             "role": "user",
#             "content": user_input,
#         }
#
#         # 本轮发送：
#         # 之前完整历史 + 当前用户消息
#         request_messages = messages + [user_message]
#
#         print(
#             f"[INFO] 本轮将发送 "
#             f"{len(request_messages)} 条消息"
#         )
#
#         result = send_message(
#             client,
#             request_messages,
#             model,
#         )
#
#         if result is None:
#             print("本轮请求失败，历史没有发生修改")
#             continue
#
#         reply, usage = result
#
#         # 请求成功后，追加 user 和 assistant
#         messages.append(user_message)
#         messages.append({
#             "role": "assistant",
#             "content": reply,
#         })
#
#         last_usage = usage
#
#         print(f"AI：{reply}")
#         print_usage(last_usage)
#         print()
#
#
# if __name__ == "__main__":
#     run_chat()

# import os
# from pathlib import Path

# import openai
# from openai import OpenAI
# from dotenv import load_dotenv

# # 读取当前目录下的 .env
# load_dotenv(Path(__file__).with_name(".env"))

# api_key = (os.getenv("DEEPSEEK_API_KEY") or "").strip()
# base_url = (
#     os.getenv("DEEPSEEK_BASE_URL")
#     or "https://api.deepseek.com"
# ).strip()
# model = (
#     os.getenv("DEEPSEEK_MODEL")
#     or "deepseek-chat"
# ).strip()

# if not api_key:
#     raise SystemExit("DEEPSEEK_API_KEY 未配置")

# client = OpenAI(
#     api_key=api_key,
#     base_url=base_url,
#     timeout=60,
#     max_retries=0,
# )

# system_message = {
#     "role": "system",
#     "content": "你是一个简洁、准确的 Python 助手。",
# }

# messages = [system_message]

# while True:
#     user_input = input("你：").strip()

#     if not user_input:
#         continue

#     if user_input.lower() in {"exit", "/exit", "quit", "/quit"}:
#         print("Bye")
#         break

#     if user_input == "/reset":
#         messages = [system_message]
#         print("对话已重置")
#         continue

#     messages.append({
#         "role": "user",
#         "content": user_input,
#     })

#     try:
#         response = client.chat.completions.create(
#             model=model,
#             messages=messages,
#             stream=False,
#         )

#     except openai.OpenAIError as error:
#         # 请求失败时，不要让失败的 user 消息留在历史里
#         messages.pop()
#         print(f"请求失败：{error}")
#         continue

#     if not response.choices:
#         messages.pop()
#         print("模型没有返回回答")
#         continue

#     reply = response.choices[0].message.content

#     if not reply:
#         messages.pop()
#         print("模型返回了空回答")
#         continue

#     messages.append({
#         "role": "assistant",
#         "content": reply,
#     })

#     print(f"AI：{reply}")

#     if response.usage:
#         print(
#             f"Token：输入 {response.usage.prompt_tokens}，"
#             f"输出 {response.usage.completion_tokens}，"
#             f"总计 {response.usage.total_tokens}"
#         )