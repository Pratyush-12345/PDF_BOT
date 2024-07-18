# PDF Chatbot

This Streamlit-based chatbot provides information about PDF using the Gemini AI model.

## Features

- Interactive chat interface
- Context-aware responses
- PDF corpus integration
- Conversation history tracking

## Requirements

- Python 3.7+
- Streamlit
- PyMuPDF (fitz)
- Google GenerativeAI

## Setup

1. Clone the repository:
git clone 'https://github.com/your-username/jechatbot.git cd jessup-cellars-chatbot'


2. Install dependencies:
'pip install -r requirements.txt'


3. Set up your Gemini API key:
- Obtain an API key from Google AI Studio
- Replace the placeholder in the code with your actual API key

4. Prepare the corpus:
- Replace The pdf Path from your path

5. Change the Streamlit Title of your choice

6. Change the full_prompt(You are a helpful assistant for Change_with_title),change accordingly

7. change streamlit inside st.input prompt accordingly

## Usage

Run the Streamlit app:
'streamlit run chatbot.py'


Visit the provided local URL in your web browser to interact with the chatbot.

## Customization

- Modify the `extract_text_from_pdf` function to adjust PDF parsing
- Update the `get_gemini_response` function to fine-tune the AI's behavior
- Adjust the conversation history and message pruning as needed

