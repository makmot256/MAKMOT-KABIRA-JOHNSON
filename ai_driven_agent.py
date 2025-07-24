import requests
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")     

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Message sent!")
    else:
        print(f"Failed: {response.text}")

if __name__ == "__main__":
    send_telegram_message("Hello from my Python Telegram bot!")
    