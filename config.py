import os
import json
from pathlib import Path

# Saves the key in your user folder (C:\Users\YourName\.wizard_config)
CONFIG_FILE = Path.home() / ".wizard_config"

def get_api_key():
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                return data.get("GROQ_API_KEY")
        except:
            return None
    return None

def save_api_key(api_key):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"GROQ_API_KEY": api_key}, f)