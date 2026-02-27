#!/usr/bin/env python3
"""
Agent消息发送工具
用法: python3 send.py --to <agent_id> --message <message>
"""

import argparse
import json
import os
import time
import uuid
from datetime import datetime
from pathlib import Path

# 配置
SKILL_DIR = Path(__file__).parent.parent
DATA_DIR = SKILL_DIR / "data"
MESSAGES_DIR = DATA_DIR / "messages"
CONFIG_FILE = SKILL_DIR / "templates" / "config.json"

def load_config():
    """加载配置"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {
        "workspace": str(DATA_DIR),
        "timeout": 300,
        "retry": 3,
        "agents": ["pm", "dev", "test", "main"]
    }

def send_message(to: str, message: str, priority: str = "normal", from_agent: str = "main") -> dict:
    """
    发送消息给指定Agent
    
    Args:
        to: 目标Agent ID
        message: 消息内容
        priority: 优先级 (urgent, high, normal, low)
        from_agent: 发送者Agent ID
    
    Returns:
        发送结果
    """
    # 确保目录存在
    MESSAGES_DIR.mkdir(parents=True, exist_ok=True)
    
    # 生成消息ID
    msg_id = f"msg_{uuid.uuid4().hex[:12]}"
    
    # 构建消息
    msg_data = {
        "id": msg_id,
        "from": from_agent,  # 发送者Agent
        "to": to,
        "message": message,
        "priority": priority,
        "timestamp": datetime.now().isoformat(),
        "status": "pending",
        "read": False
    }
    
    # 写入目标Agent的inbox
    inbox_dir = MESSAGES_DIR / to / "inbox"
    inbox_dir.mkdir(parents=True, exist_ok=True)
    
    msg_file = inbox_dir / f"{msg_id}.json"
    with open(msg_file, "w") as f:
        json.dump(msg_data, f, indent=2, ensure_ascii=False)
    
    return {
        "success": True,
        "message_id": msg_id,
        "to": to,
        "timestamp": msg_data["timestamp"]
    }

def main():
    parser = argparse.ArgumentParser(description="Agent消息发送工具")
    parser.add_argument("--to", required=True, help="目标Agent ID")
    parser.add_argument("--message", required=True, help="消息内容")
    parser.add_argument("--from", dest="from_agent", default="main", help="发送者Agent ID")
    parser.add_argument("--priority", default="normal", 
                       choices=["urgent", "high", "normal", "low"],
                       help="消息优先级")
    
    args = parser.parse_args()
    
    result = send_message(args.to, args.message, args.priority, args.from_agent)
    
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()