from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")

# Set title and sidebar
st.title("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input text box
input_text = st.text_input("Input:", key="input")

# Submit button
submit_button = st.button("Ask the question")

# Display response
if submit_button and input_text:
    response = get_gemini_response(input_text)
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Chat history section
st.subheader("Chat History")

# Adding animations to chat history
st.markdown("""
<style>
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
@keyframes slideInFromLeft {
  from { transform: translateX(-100%); }
  to { transform: translateX(0); }
}
.chat-item {
  animation: fadeIn 0.5s ease, slideInFromLeft 0.5s ease;
}
</style>
""", unsafe_allow_html=True)

for role, text in st.session_state['chat_history']:
    if role == "You":
        st.markdown(f"<div class='chat-item' style='color: blue;'><strong>You:</strong> {text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-item' style='color: green;'><strong>Bot:</strong> {text}</div>", unsafe_allow_html=True)
