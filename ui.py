import streamlit as st

# Set page title
st.title('PolicyPro')

with st.sidebar:
    st.title("PolicyPro")
    st.markdown("PolicyPro GuideBot is an AI-powered chatbot designed to demystify complex government policies, starting with financial regulations. Our goal is to empower users by providing clear and understandable explanations of policies and their implicationsPolicyPro GuideBot is an AI-powered chatbot designed to demystify complex government policies.")
    st.header(' Ask PolicyPro like:')
    st.markdown("What Education policies india have ")
    st.markdown("Top 5 Edu Policies")
    st.markdown("Scholarship policies")
# Sidebar with predefined prompts

if 'messages' not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt= st.chat_input('Enter your query here:')

if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role':'user','content':prompt})
    responce = agent.query(prompt)
    st.chat_message('assitant').markdown(responce)
    st.session_state.messages.append({'role':'assistant','content':responce})
