import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools import tool
from datetime import datetime

llm = ChatOllama(
    model="qwen3:4b",
    temperature=0.1
)

@tool
def read_file(file_path: str) -> str:
    """读取本地文本文件（.txt/.md等），返回文件内容"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return f"✅ 读取文件成功：{file_path}\n内容：\n{content}"
    except Exception as e:
        return f"❌ 读取失败：{str(e)}"

@tool
def get_current_time(info: str = "now") -> str:
    """获取当前日期、时间、星期几，info参数仅用于格式匹配，可留空"""
    now = datetime.now()
    weekday_map = {
        0: "星期日", 1: "星期一", 2: "星期二", 3: "星期三",
        4: "星期四", 5: "星期五", 6: "星期六"
    }
    return (
        f"📅 当前时间：{now.strftime('%Y年%m月%d日 %H:%M:%S')}\n"
        f"📆 星期：{weekday_map[now.weekday()]}"
    )


tools = [read_file, get_current_time]


prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个智能助手，会调用工具回答问题。"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)



st.title("🤖 AI Agent 智能助手（网页版）")
st.subheader("✅ 功能：文件操作 | 查询时间 | 联网搜索")


if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.chat_history = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_input = st.chat_input("请输入你的问题...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    res = agent_executor.invoke({
        "input": user_input,
        "chat_history": st.session_state.chat_history
    })

    with st.chat_message("assistant"):
        st.markdown(res["output"])

    st.session_state.messages.append({"role": "assistant", "content": res["output"]})
    st.session_state.chat_history.extend([
        ("user", user_input),
        ("assistant", res["output"])
    ])