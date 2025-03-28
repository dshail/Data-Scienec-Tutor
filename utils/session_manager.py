import streamlit as st
from utils.llm_utils import get_llm, get_llm_chain
from utils.data_classes import Message

USER = "user"
ASSISTANT = "ai"
MESSAGES = "messages"


def initialize_session_state():
    """Initializes the session state for messages and the LLM chain."""
    if MESSAGES not in st.session_state:
        st.session_state[MESSAGES] = [
            Message(
                actor=ASSISTANT,
                payload="Hi! I'm your data science tutor. Ask me anything!",
            )
        ]
    if "llm_chain" not in st.session_state:
        st.session_state["llm_chain"] = get_llm_chain()


def get_llm_chain_from_session():
    """Retrieves the LLM chain from the session state."""
    return st.session_state["llm_chain"]