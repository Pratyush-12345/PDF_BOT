import streamlit as st
import fitz  # PyMuPDF
import google.generativeai as genai
import asyncio

# Configure the Gemini API
genai.configure(api_key="Your_API_key")

# Load the PDF and extract text
@st.cache_data
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Load corpus at startup
corpus = extract_text_from_pdf("Path_of_your_pdf")

# Function to get response from Gemini
async def get_gemini_response(prompt, corpus, conversation_history):
    model = genai.GenerativeModel('gemini-pro')
    context = "\n".join(conversation_history)
    full_prompt = f"You are a helpful assistant for Change_with_title. Use the following information to answer questions in detail, providing comprehensive explanations and examples when possible. Aim for longer, paragraph-style responses. Conversation history:\n{context}\n\nCorpus: {corpus}\n\nUser: {prompt}\n\nAssistant:"
    
    response = await model.generate_content_async(full_prompt)
    
    if "I don't have information about that" in response.text:
        response.text += " For more specific information, please contact Company directly."
    
    return response.text

st.title("Title_of_your_chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

async def get_and_display_response(prompt):
    response = await get_gemini_response(prompt, corpus, st.session_state.conversation_history)
    response_placeholder.markdown(response)
    st.session_state.conversation_history.append(f"User: {prompt}")
    st.session_state.conversation_history.append(f"Assistant: {response}")
    return response

if prompt := st.chat_input("What would you like to know about our_pdf_name?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        with st.spinner("Thinking..."):
            response = asyncio.run(get_and_display_response(prompt))

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Prune chat history to keep only last 10 messages
st.session_state.messages = st.session_state.messages[-10:]
st.session_state.conversation_history = st.session_state.conversation_history[-20:]  # Keep last 20 exchanges
