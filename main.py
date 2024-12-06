#pip install python-dotenv
#pip install langchain-openai
#pip install streamlit

# from dotenv import load_dotenv
# load_dotenv()

# 기존 코드 (잘못된 모듈 이름)
# from langchain_openai import ChatOpenAI

# 수정된 코드
from langchain.chat_models import ChatOpenAI

# subject = "AI"
# result = chat_model.invoke(subject + "에 대한 시를 써줘.")
# print(result.content)

import streamlit as st

st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        result = chat_model.invoke(subject + "에 대한 시를 써줘")
        st.write(result.content)
