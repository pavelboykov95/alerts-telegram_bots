#!/bin/bash

for SPAM in 1 2 3 4 5 6 7 8 9
do
    python3.9 send_message_from_terminal.py -m "Спам номер ${SPAM}" -n "Maks"
done
