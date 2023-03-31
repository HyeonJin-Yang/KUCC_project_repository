import os

import jsonlines
import openai

from utils import *
# --------------------------------------------- <OpenAI API Key Setting> -----------------------------------------
with open(os.path.join(ROOT_DIR, "openai_key.txt"), 'r') as f:
    key = f.readline().strip()
    openai.api_key = key

# --------------------------------------------- <Few-Shot Learning?> ----------------------------------------------
with jsonlines.open(os.path.join(DATA_DIR, "train_data/train.jsonl"), 'r') as f:
        messages = []
        for prompt in f:
             messages.append(prompt)
             if len(messages) == 40: break
# ------------------------------------------------- <Chat-bot> ---------------------------------------------------
model_name = "gpt-3.5-turbo-0301"

while True:
    user_content = input("user : ")
    messages.append({"role": "assistant", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(
        model=model_name,
        messages=messages)

    assistant_content = completion.choices[0].message["content"]

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT: {assistant_content}")