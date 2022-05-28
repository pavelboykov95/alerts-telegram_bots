from argparse import ArgumentParser
import os
from pathlib import Path
import sys

import requests

ROOT_DIR = Path(os.getcwd()).resolve()
if ROOT_DIR not in sys.path:
    sys.path.append(str(ROOT_DIR))

from auth_data import ML_ALERT_BOT_TOKEN, MY_CHAT_ID
from constants import API_URL, METHOD_SEND_MESSAGE

# TODO(BoykovPV): To integrate storing user names and chat ids with sqlite
def send_message(text: str, recipient_name:int = MY_CHAT_ID):
    r = requests.get(f'{API_URL}{ML_ALERT_BOT_TOKEN}{METHOD_SEND_MESSAGE}',
                     data = {'chat_id': recipient_name, 'text': text})
    print("Message sent successfully")
    if r.status_code != 200:
        print("Sending message error")
    print(r.json())


if __name__ == '__main__':
    parser = ArgumentParser(description="""Parses model feature importances files, calculates days
                                        importances for all model f-e files, plots the heatmap.""")

    parser.add_argument(
        '-m',
        '--message',
        metavar='MESSAGE_TEXT',
        type=str,
        help='The text of the message to be sent by the bot'
    )

    # TODO(BoykovPV): Make it a working option
    parser.add_argument(
        '-n',
        '--name',
        metavar='RECIPIENT_NAME',
        type=str,
        help="""Name of the registered message recipient.
             Supported values:
             "ALL": The message will be send to all of registered users
             "<Rubius login>": Recipient Rubius login in case <first name>.<last name>""",
        default=MY_CHAT_ID
    )

    args = parser.parse_args()
    send_message(args.message, args.name)
