import os

from langchain.document_loaders import PyMuPDFLoader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.redis import Redis
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from utils import *

# ------------------------------------ <Load Data> -----------------------------------
loader = TextLoader(
    os.path.join(DATA_DIR, "raw_data\\KU_rules.txt"),
    encoding="utf-8")
documents = loader.load()

# ---------------------------------- <Create VectorStore> ----------------------------
text_splitter = CharacterTextSplitter(separator = "\n", chunk_size=300, chunk_overlap=0, length_function=len)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(texts, embeddings)

retriever = db.as_retriever()

# ----------------------------------- <Make Query> -----------------------------------
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever)

query = '군 휴학에 대해 알려줘'
print(qa.run(query))