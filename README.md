# Agent Communication Skill

<div align="center">

一个通用的 **Agent间沟通技能**，解决多Agent团队协作中的沟通问题

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://clawhub.ai/skills/agent-communication)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Test](https://img.shields.io/badge/test-passing-brightgreen.svg)](#测试报告)

</div>

---

## 🎯 解决的问题

| 问题 | 解决方案 |
|------|---------|
| `sessions_send` 超时 | 文件驱动消息队列 |
| Agent 无法直接沟通 | 标准化消息 API |
| 团队协作效率低 | 共享工作空间 |

---

## ✨ 核心功能

- 📨 **消息传递** - Agent之间快速发送消息
- 📢 **广播消息** - 一次发送给多个Agent
- 🗂️ **共享工作空间** - 文件驱动的协作
- 🟢 **状态同步** - Agent在线状态检测

---

## 📦 安装

```bash
# 通过 ClawHub 安装
openclaw skill install agent-communication

# 或手动安装
git clone https://github.com/momoflowers/agent-communication.git
cd agent-communication
```

---

## 🚀 快速开始

### 发送消息

```bash
python3 scripts/send.py --from pm --to dev --message "开始开发任务" --priority high
```

### 广播消息

```bash
python3 scripts/broadcast.py --from main --message "项目启动" --agents pm,dev,test
```

### 查询状态

```bash
python3 scripts/status.py --agent dev
python3 scripts/status.py --list
```

### 共享工作空间

```bash
python3 scripts/workspace.py --write --key task --value '{"id":1}'
python3 scripts/workspace.py --read --key task
```

---

## 📋 测试报告

| 测试项 | 状态 |
|--------|------|
| 消息发送 | ✅ 通过 |
| 广播消息 | ✅ 通过 |
| 双向沟通 | ✅ 通过 |
| 状态同步 | ✅ 通过 |
| 共享工作空间 | ✅ 通过 |

**通过率: 100%**

---
