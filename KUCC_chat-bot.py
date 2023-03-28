import os, sys
import json, jsonlines
import openai

# --------------------------------------------- <PATH Configuration> ---------------------------------------------
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
# SAVE_DIR = os.path.join(ROOT_DIR, 'saved_results')
# if not os.path.exists(SAVE_DIR):
#     os.mkdir(SAVE_DIR)

INPUT_DIR = os.path.join(ROOT_DIR, 'data')
# --------------------------------------------- <API Configuration> ----------------------------------------------
with open(os.path.join(ROOT_DIR, "openai_key.txt"), 'r') as f:
    key = f.readline().strip()
    openai.api_key = key

# --------------------------------------------- <Model Configuration> --------------------------------------------
model_name = "gpt-3.5-turbo-0301"

# --------------------------------------------- <Few-Shot Learning> ----------------------------------------------
with jsonlines.open(os.path.join(INPUT_DIR, 'meta_train.jsonl'), 'r') as f:
    messages = list(f)

# ------------------------------------------------- <Chat-bot> ---------------------------------------------------
while True:
    user_content = input("user : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(
        model=model_name,
        messages=messages)

    assistant_content = completion.choices[0].message["content"]

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT: {assistant_content}")