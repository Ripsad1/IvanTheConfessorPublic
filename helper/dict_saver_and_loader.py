import json
import os

def load_dict(save_file):
    if not os.path.exists(save_file):
        return {}

    with open(save_file, "r", encoding="utf-8") as file:
        return json.load(file)

def save_dict(save_file, msg):
    with open(save_file, "w", encoding="utf-8") as file:
        json.dump(msg, file, ensure_ascii=False, indent=4)