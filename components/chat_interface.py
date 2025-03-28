import streamlit as st
from utils.data_classes import Message

USER = "user"
ASSISTANT = "ai"

def display_chat_messages(messages):
  """Displays the message in the streamlit chat interface."""
  for msg in messages:
    st.chat_message(msg.actor).write(msg.payload)

def handle_chat_input(messages, llm_chain):
  """Display the chat and handles it."""
  prompt = st.chat_input("Ask a data science question")
  if prompt:
    messages.append(Message(actor=USER, payload=prompt))
    st.chat_message(USER).write(prompt)
    with st.spinner("Please wait.."):
      response = llm_chain({"question": prompt})["text"]
      messages.append(Message(actor=ASSISTANT, payload=response))
      st.chat_message(ASSISTANT).write(response)