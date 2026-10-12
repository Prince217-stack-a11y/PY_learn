"""Day 21 - Mini Project 2：DeepSeek 多轮对话命令行聊天机器人

练习目标：
1. 从 .env 加载 API Key（python-dotenv）
2. 用 HTTP 直接调用 DeepSeek 的 chat/completions 接口（requests）
3. 维护 messages 列表，实现多轮连续对话
4. 观察 messages 如何增长，理解 LLM 无状态、每轮全量重发

运行前准备：
1. 在本文件同级目录创建 .env 文件，写入一行（换成你的真实密钥）：
   DEEPSEEK_API_KEY=sk-xxxxxxxx
2. 运行：python chat_cli.py
退出方式：输入 exit / quit / 退出，或按 Ctrl+C
"""

import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"   # DeepSeek-V3 对话模型
TIMEOUT = 60              # 秒

SYSTEM_PROMPT = "你是一个简洁友好的中文助手，回答控制在 100 字以内。"


def load_api_key():
    """从本文件同目录的 .env 读取 DEEPSEEK_API_KEY。"""
    # 用 Path(__file__).parent 定位脚本所在目录，
    # 这样无论从哪个文件夹启动 python 命令，都能找到 .env
    env_path = Path(__file__).parent / ".env"
    load_dotenv(env_path)

    api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        print("错误：没有读到 API Key。")
        print("请在 chat_cli.py 同目录创建 .env 文件，内容如下（换成真实密钥）：")
        print("  DEEPSEEK_API_KEY=sk-xxxxxxxx")
        print("密钥申请地址：https://platform.deepseek.com")
        sys.exit(1)
    return api_key


def chat(messages, api_key):
    """调用 DeepSeek 接口，返回 (回复文本, usage 字典)。

    注意：messages 是整个对话历史，每次请求都全量发送——
    LLM 本身无状态，服务器不记得上一轮说过什么。
    """
    payload = {
        "model": MODEL,
        "messages": messages,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    try:
        resp = requests.post(API_URL, json=payload, headers=headers, timeout=TIMEOUT)
    except requests.ConnectionError:
        print("[网络错误] 连不上 api.deepseek.com，检查网络或代理后重试。")
        return None, None
    except requests.Timeout:
        print(f"[网络错误] 超过 {TIMEOUT} 秒没有响应，已放弃本次请求。")
        return None, None

    # ---- HTTP 状态码分类处理 ----
    if resp.status_code == 401:
        print("[401] API Key 无效：检查 .env 里的密钥是否复制完整，修好后重新运行。")
        return None, None
    if resp.status_code == 402:
        print("[402] 账户余额不足：去 https://platform.deepseek.com 充值。")
        return None, None
    if resp.status_code == 429:
        print("[429] 请求太频繁：等几秒再发。")
        return None, None
    if resp.status_code != 200:
        print(f"[HTTP {resp.status_code}] 意外响应：{resp.text[:200]}")
        return None, None

    # ---- 响应结构检查（练习要求：返回为空时检查密钥/网络/请求结构）----
    try:
        data = resp.json()
    except ValueError:
        print(f"[解析失败] 响应不是 JSON：{resp.text[:200]}")
        return None, None

    choices = data.get("choices")
    if not choices:
        print("[空回复] 接口通了但 choices 为空，原始响应：")
        print(data)
        return None, None

    content = choices[0].get("message", {}).get("content", "").strip()
    if not content:
        print(f"[空回复] finish_reason={choices[0].get('finish_reason')}，原始响应：")
        print(data)
        return None, None

    usage = data.get("usage", {})
    return content, usage


def print_stats(messages, usage, round_no):
    """每轮打印 messages 增长情况和 token 用量。"""
    role_count = {}
    for m in messages:
        role_count[m["role"]] = role_count.get(m["role"], 0) + 1

    detail = " + ".join(f"{role} {n} 条" for role, n in role_count.items())
    print(f"--- [第 {round_no} 轮] messages 共 {len(messages)} 条（{detail}）")
    if usage:
        # prompt_tokens = 本轮实际发送的全部历史大小，
        # 就是"每轮全量重发"的直接证据：轮数越多它越大
        print(f"--- [用量] 本轮发送 prompt_tokens={usage.get('prompt_tokens')}"
              f"，回复 completion_tokens={usage.get('completion_tokens')}")


def main():
    api_key = load_api_key()

    # messages 是这个对话的唯一"记忆"，开局只放一条 system 设定
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    print("=" * 50)
    print("DeepSeek CLI 聊天机器人（Day 21）")
    print("输入 exit / quit / 退出 结束对话")
    print("=" * 50)

    round_no = 0
    while True:
        try:
            user_input = input("\n你> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n再见！")
            break

        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "退出"):
            print("再见！")
            break

        round_no += 1

        # 1. 把用户这轮的话追加进历史
        messages.append({"role": "user", "content": user_input})

        # 2. 全量重发整个历史，拿回复
        reply, usage = chat(messages, api_key)

        if reply is None:
            # 本轮失败：撤回刚追加的 user 消息，避免历史里留脏数据
            messages.pop()
            round_no -= 1
            continue

        # 3. 回复也追加进历史，下一轮模型才能"记得"它说过什么
        messages.append({"role": "assistant", "content": reply})

        print(f"\nAI> {reply}")
        print_stats(messages, usage, round_no)


if __name__ == "__main__":
    main()
