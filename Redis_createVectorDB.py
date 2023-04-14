import os

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.redis import Redis as RedisVectorStore

from utils import *

# ------------------------------------ <Load Data> -----------------------------------
loader = TextLoader(
    os.path.join(DATA_DIR, "raw_data\\KU_rules.txt"),
    encoding="utf-8")
documents = loader.load()

# ---------------------------------- <Create VectorStore> ----------------------------
text_splitter = CharacterTextSplitter(separator = "\n", chunk_size=300, chunk_overlap=0, length_function=len)
texts = text_splitter.split_documents(documents)

# ------------------------------- <VectorStore Configuration> -------------------------------
texts = [text.page_content for text in texts]
metadatas = []
embedding = OpenAIEmbeddings()
index_name = "ku_rule"
redis_url = "redis://localhost:6379"

# ------------------------------- <Create VectorStore DataBase> -------------------------------
vectorstore = RedisVectorStore.from_texts(
    texts=texts,
    metadatas=metadatas,
    embedding=embedding,
    index_name=index_name,
    redis_url=redis_url
)

print("Created VectorDB Successfully")