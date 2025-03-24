import os

def init_dev_mode():
    api_key = os.getenv("API_KEY")
    if api_key:
        print("Developer Mode Active: API Key Detected")
    else:
        print("Developer Mode Inactive. No API Key found.")
