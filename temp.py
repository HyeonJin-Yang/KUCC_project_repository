import os, json
import openai

from utils import complete_gpt3

# --------------------------------------------- <PATH Configuration> ---------------------------------------------
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
SAVE_DIR = os.path.join(ROOT_DIR, 'saved_results')
if not os.path.exists(SAVE_DIR):
    os.mkdir(SAVE_DIR)

INPUT_DIR = os.path.join(ROOT_DIR, 'data')
# --------------------------------------------- <API Configuration> ----------------------------------------------
openai.organization = 'org-8w2Q5rrtsD6p2nuBE9joo89R'
with open(os.path.join(ROOT_DIR, "openai_key.txt"), 'r') as f:
    key = f.readline().strip()
    openai.api_key = key

# --------------------------------------------- <Model Configuration> --------------------------------------------
"""
models = openai.Model.list()
for model in models["data"]: print(model["id"])
"""
model_name = "gpt-3.5-turbo-0301"

# --------------------------------------------- <Few-Shot Learning> ----------------------------------------------

with open(os.path.join(INPUT_DIR, 'train_prepared.jsonl'), 'r') as f:
    prompt = f.readline()
    print(complete_gpt3(prompt, 0, model_name))

    
