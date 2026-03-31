# AI Agent 智能助手
基于 **本地大模型 + LangChain + Streamlit** 构建的 AI 智能体，纯本地运行、无 API 依赖，支持工具调用与交互式网页界面。

## 项目特性
- 本地大模型驱动（qwen3:4b）
- AI自主工具调用
- 读取本地文本文件
- 查询当前日期、时间、星期
- 美观流畅的网页交互界面
- 多轮对话记忆功能

## 快速启动
### 1. 安装依赖
```
pip install -r requirements.txt
```
### 2. 启动 Ollama 服务
```
ollama pull qwen3:4b
ollama serve
```
### 3. 运行网页版 AI Agent
```
streamlit run app.py
```
## 支持功能
- 查询时间 — 实时获取当前日期、时间、星期
- 读取文件 — 读取本地 .txt/.md 等文本文件
- 智能对话 — 多轮记忆 + 工具调度
## 技术栈
- LangChain：AI Agent 核心框架
- Ollama：本地大模型运行环境
- Streamlit：快速构建网页交互界面
- Python：核心开发语言
## 说明
本项目为纯本地部署的 AI 智能体，无需联网即可使用基础功能，适合学习 AI Agent 工作原理、工具调用机制与交互式界面开发
