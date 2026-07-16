import os
import json
from pathlib import Path

# Save the config in the user's home folder (C:\Users\Name\.wizard_config)
CONFIG_FILE = Path.home() / ".wizard_config"

def get_api_key():
    # 1. Check if config file exists
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)
            return data.get("GROQ_API_KEY")
    return None

def save_api_key(api_key):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"GROQ_API_KEY": api_key}, f)

GROQ_API_KEY = get_api_key()