# memory/recorder.py

import json
from datetime import datetime

MEMORY_FILE = "memory/memory_log.json"

def record_memory(user_input, response):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "input": user_input,
        "response": response
    }

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def read_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []
