# streamlit_app.py
import streamlit as st
import os
from openai import AzureOpenAI

st.write('test')
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

# Azure OpenAI クライアントの作成
client = AzureOpenAI(
    azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"],
    api_key=st.secrets["AZURE_OPENAI_KEY"],
    api_version="2024-02-15-preview"
)

USER_NAME = "user"
ASSISTANT_NAME = "assistant"
model = "gpt-35-turbo"

# チャットのメッセージを送信する関数
def send_message(message):
    message_text = [{"role": "user", "content": message}]
    completion = client.chat.completions.create(
        model=model,
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    if completion.choices:
        response = completion.choices[0].message.content
        return response
    else:
        return "No response received"

# チャットログを保存したセッション情報を初期化
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# ユーザのメッセージに対する応答を生成する関数
def response_chatgpt(user_msg: str, chat_history: list = []):
    system_msg = """If the user is asked about a product, please include all information about each product.
                    The user is an excellent salesman.
                    Please advise according to the user's request.
                    The user talks in a friendly tone, but somewhat difficult to understand.
                    Be sure to conduct the conversation and evaluation in Japanese."""
    messages = [
        {"role": "system", "content": system_msg}
    ]

    # チャットログがある場合は、チャットログをmessagesリストに追加
    if len(chat_history) > 0:
        for chat in chat_history:
            messages.append({"role": chat["name"], "content": chat["msg"]})
    # ユーザメッセージをmessagesリストに追加
    messages.append({"role": USER_NAME, "content": user_msg})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response

# Streamlitアプリの作成
st.title("Chat with AI")

# ユーザのメッセージを入力
user_msg = st.chat_input("Enter your message")

if user_msg:
    # アシスタントのメッセージを生成
    assistant_msg = response_chatgpt(user_msg, chat_history=st.session_state.chat_log)

    # アシスタントのメッセージを表示
    assistant_text = assistant_msg.choices[0].message.content if assistant_msg.choices else "No response received"

    # チャットログにメッセージを追加
    if st.session_state.chat_log:  # チャットログが空でない場合
        if user_msg != st.session_state.chat_log[-1]["msg"] or assistant_text != st.session_state.chat_log[-1]["msg"]:
            st.session_state.chat_log.append({"name": USER_NAME, "msg": user_msg})
            st.session_state.chat_log.append({"name": ASSISTANT_NAME, "msg": assistant_text})
    else:  # チャットログが空の場合
        st.session_state.chat_log.append({"name": USER_NAME, "msg": user_msg})
        st.session_state.chat_log.append({"name": ASSISTANT_NAME, "msg": assistant_text})

# チャットログを表示
for chat in st.session_state.chat_log:
    st.write(chat["name"] + ": " + chat["msg"])

with st.sidebar:
    st.title("PKG ONE STOP")
