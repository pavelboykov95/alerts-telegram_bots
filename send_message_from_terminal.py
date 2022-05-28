import requests

from auth_data import ML_ALERT_BOT_TOKEN, MY_CHAT_ID
from constants import API_URL, METHOD_SEND_MESSAGE


def send_message(text: str):
    r = requests.get(f'{API_URL}{ML_ALERT_BOT_TOKEN}{METHOD_SEND_MESSAGE}',
                     data = {'chat_id': MY_CHAT_ID, 'text': text})
    print("Message sent successfully")
    if r.status_code != 200:
        print("Sending message error")
    print(r.json())


if __name__ == '__main__':
    send_message("gf")
