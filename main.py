import tabula
import os


import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
from llama_index.core import PromptTemplate

instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression."""

new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

context = """Purpose: The primary role of this agent is to assist users by providing accurate
            information about world population statistics and details about a country. """
os.environ["OPENAI_API_KEY"] = "your-ai-key"


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index


pdf_path = os.path.join("C:/Users/Fuzlan/OneDrive/Documents/AI-myhem/datasetai1c.pdf")
pdf = PDFReader().load_data(file=pdf_path)
index = get_index(pdf, "Policies")
engine = index.as_query_engine()

tools = [
    QueryEngineTool(
        query_engine=engine,
        metadata=ToolMetadata(
            name="data",
            description="this gives detailed information about Policies ",
        ),
    ),
]


llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)


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
