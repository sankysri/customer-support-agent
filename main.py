# customer_support_agent/main.py
import streamlit as st
from agent_config import agent_executor

st.set_page_config(page_title="Customer Support AI Bot")
st.title("🤖 Customer Support AI Assistant")

# Chat input
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("How can I help you today?")

if user_input:
    st.session_state.chat_history.append(("User", user_input))
    
    with st.spinner("Thinking..."):
        response = agent_executor.invoke({"input": user_input})
        st.session_state.chat_history.append(("Bot", response["output"]))

# Display chat history
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)
