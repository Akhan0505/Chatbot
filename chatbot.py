import streamlit as st
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

# Set up Streamlit app title and introduction
st.title("Chat with Vortex!")
st.write("Hello! I'm your friendly Vortex chatbot. I can help answer your questions, provide information, or just chat.")

# Define conversational memory length
conversational_memory_length = 10
memory = ConversationBufferWindowMemory(k=conversational_memory_length)

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Save existing chat history to memory
for message in st.session_state.chat_history:
    memory.save_context({'input': message['human']}, {'output': message['AI']})

# Initialize the ChatGroq model
groq_chat = ChatGroq(
    groq_api_key='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',
    model_name='gemma2-9b-it'
)

# Initialize the ConversationChain
conversation = ConversationChain(
    llm=groq_chat,
    memory=memory
)

# Streamlit input form
user_question = st.text_input("Ask a question:")
if user_question:
    response = conversation({"input": user_question})
    st.write("Response:", response)  # Debugging line to check the response structure

    # Adjust based on actual response structure
    if 'output' in response:
        st.session_state.chat_history.append({'human': user_question, 'AI': response['output']})
    elif 'text' in response:
        st.session_state.chat_history.append({'human': user_question, 'AI': response['text']})
    else:
        st.write("Unexpected response structure:", response)
