import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Titanic Chat Agent", layout="centered")

st.title("🚢 Titanic Dataset Chatbot")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask a question about the Titanic dataset...")

if user_input:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend
    try:
        response = requests.post(
            f"{BACKEND_URL}/ask",
            json={"question": user_input}
        )

        data = response.json()

        if data["success"]:
            answer = data["answer"]
        else:
            answer = f"Error: {data['error']}"

    except Exception as e:
        answer = f"Backend connection error: {str(e)}"

    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Try to load plot
    try:
        plot_response = requests.get(f"{BACKEND_URL}/plot")

        if plot_response.status_code == 200:
            st.image(plot_response.content)

    except:
        pass