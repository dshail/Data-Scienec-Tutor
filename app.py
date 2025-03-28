import streamlit as st
from utils.session_manager import initialize_session_state, get_llm_chain_from_session
from utils.llm_utils import get_llm_response
from utils.data_classes import Message
from components.sidebar import create_sidebar
from components.chat_interface import display_chat_messages, handle_chat_input

# ✅ Set page title and logo
st.set_page_config(
    page_title="DS Tutor Chat",
    page_icon="static/images/ds_tutor.ico",  # Set the page icon
    layout="wide"  # Improve layout visibility
)

# ✅ Initialize session state and LLM chain
initialize_session_state()

# ✅ Create sidebar
create_sidebar()

# ✅ Main chat interface
tab1, tab2 = st.tabs(["Chat", "Quiz"])

with tab1:
    st.title("🤖 Data Science Tutor Chat")
    display_chat_messages(st.session_state["messages"])

with tab2:
    st.header("Test Your Knowledge")
    
    questions = [
        {"q": "What is overfitting?", "a": "When a model learns noise in the training data."},
        {"q": "What does PCA stand for?", "a": "Principal Component Analysis"}
    ]
    
    for i, q in enumerate(questions):
        with st.form(f"quiz_{i}"):
            st.write(q["q"])
            user_answer = st.text_input("Your answer:", key=f"answer_{i}")
            submit = st.form_submit_button("Submit")
            
            if submit:
                if user_answer.lower() in q["a"].lower():
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Wrong. Correct answer: {q['a']}")
                
                feedback = get_llm_response(f"Explain why '{q['a']}' is the answer to '{q['q']}'")
                st.write(f"💡 Tutor: {feedback}")

# ✅ Move chat input outside tabs (fixes Streamlit error)
handle_chat_input(st.session_state["messages"], get_llm_chain_from_session())