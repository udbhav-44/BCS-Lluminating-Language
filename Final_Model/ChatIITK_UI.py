import torch
import subprocess
import streamlit as st
from run_ChatIITK import load_model
from langchain.vectorstores import Chroma
from constants import CHROMA_SETTINGS, EMBEDDING_MODEL_NAME, PERSIST_DIRECTORY, MODEL_ID, MODEL_BASENAME
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.chains import RetrievalQA
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
import os

os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'

def model_memory():
    # Adding history to the model.
    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer,\
    just say that you don't know, don't try to make up an answer.

    {context}

    {history}
    Question: {question}
    Helpful Answer:"""

    prompt = PromptTemplate(input_variables=["history", "context", "question"], template=template)
    memory = ConversationBufferMemory(input_key="question", memory_key="history")

    return prompt, memory

# Sidebar contents
with st.sidebar:
    st.title("ChatIITK - IITK's own Chatbot")
    st.markdown(
        """
    ## About
    This app is an RAG Based LLM-powered chatbot designed to help the IITK Janta in their day to day life.
    """
    )
    add_vertical_space(5)
    st.write("Made with ❤️ by [BCS](https://bcs-iitk.github.io/)")

if torch.backends.mps.is_available():
    DEVICE_TYPE = "mps"
elif torch.cuda.is_available():
    DEVICE_TYPE = "cuda"
else:
    DEVICE_TYPE = "cpu"

# Define the retriever
# Load the vectorstore
if "EMBEDDINGS" not in st.session_state:
    EMBEDDINGS = HuggingFaceInstructEmbeddings(model_name=EMBEDDING_MODEL_NAME, model_kwargs={"device": DEVICE_TYPE})
    st.session_state.EMBEDDINGS = EMBEDDINGS

if "DB" not in st.session_state:
    DB = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=st.session_state.EMBEDDINGS,
        client_settings=CHROMA_SETTINGS,
    )
    st.session_state.DB = DB

if "RETRIEVER" not in st.session_state:
    RETRIEVER = st.session_state.DB.as_retriever()
    st.session_state.RETRIEVER = RETRIEVER

if "LLM" not in st.session_state:
    LLM = load_model(device_type=DEVICE_TYPE, model_id=MODEL_ID, model_basename=MODEL_BASENAME)
    st.session_state["LLM"] = LLM

if "QA" not in st.session_state:
    prompt, memory = model_memory()
    QA = RetrievalQA.from_chain_type(
        llm=LLM,
        chain_type="stuff",
        retriever=RETRIEVER,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt, "memory": memory},
    )
    st.session_state["QA"] = QA

if "history" not in st.session_state:
    st.session_state.history = []

st.title("ChatIITK App 💬")
# Create a text input box for the user
prompt = st.text_input("Input your prompt here")

# If the user hits enter
if prompt:
    # Then pass the prompt to the LLM
    response = st.session_state["QA"](prompt)
    answer, docs = response["result"], response["source_documents"]
    # Update conversation history
    st.session_state.history.append({"prompt": prompt, "answer": answer})

    # Write out the answer to the screen
    st.write(answer)

    # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant pages
        search = st.session_state.DB.similarity_search_with_score(prompt)
        # Write out the first
        for i, doc in enumerate(search):
            st.write(f"Source Document # {i+1} : {doc[0].metadata['source'].split('/')[-1]}")
            st.write(doc[0].page_content)
            st.write("--------------------------------")

# Display conversation history
st.header("Conversation History")
for i, exchange in enumerate(st.session_state.history):
    st.write(f"**Prompt {i+1}:** {exchange['prompt']}")
    st.write(f"**Answer {i+1}:** {exchange['answer']}")
    st.write("--------------------------------")

# To show the rest of the chat 
