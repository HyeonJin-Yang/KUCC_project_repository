import os, copy

import openai
from langchain.vectorstores.redis import Redis as RedisVectorStore
from langchain.embeddings import OpenAIEmbeddings

# ------------------------------- <Connect to RedisDB> -------------------------------
rds = RedisVectorStore.from_existing_index(
    embedding=OpenAIEmbeddings(),
    redis_url="redis://localhost:6379",
    index_name="ku_rule")

# ------------------------------ <ChatBot Using Redis> ------------------------------
messages = []
while True:
    # Receive user query
    user_content = input("user : ")

    # Extract Related Docs from RedisDB
    relatedDocs = rds.similarity_search(query=user_content)
    
    # Construct prompt
    messages.append({"role": "user", "content": f"{user_content}"})
    Temp = copy.deepcopy(messages)
    Temp.append({"role": "user", "content": f"{relatedDocs}"})
    
    assistant_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=Temp
    )

    assistant_content = assistant_completion.choices[0].message["content"]

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT: {assistant_content}")