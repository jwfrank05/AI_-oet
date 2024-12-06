
import openai
#from dotenv import load_dotenv
#load_dotenv()

openai.api_key='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'

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()
result = chat_model.invoke("AI 에 대한 시를 써줘.")
print(result.content)

import streamlit as st
st.title(" 인공지능 시인")
subject = st.text_input('시의 주제를 입력해 주세요')
st.write('시의 주제 : ' +  subject)
if st.button('시 작성'):
    with st.spinner('시')
    result = chat_model.invoke(subject +' 에 대한 시를 써줘')
    st.write(result.content)