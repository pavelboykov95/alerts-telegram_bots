#!/bin/bash
# pwd
# for VAR in {1..10}
# do
#     python3.9 /usr/src/app/model_data/alerts-telegram_bots/send_message_from_terminal.py -m "$VAR"
# done
# pwd

# for PREPARE_CONFIG_TYPE in baseline_cfproj_7 dropbf_cf_cfproj_7 baseline_ood_7_cfproj_7 dropbf_cf_ood_7_cfproj_7
# do
#     if [ "$PREPARE_CONFIG_TYPE" == baseline_cfproj_7 ] || [ "$PREPARE_CONFIG_TYPE" == baseline_ood_7_cfproj_7 ]; then

#         CONFIG_TYPE="baseline_1_notnanfixed_ood_7_cfproj_7"
#         CLS_CONFIG_TYPE="baseline"
#     else
#         CONFIG_TYPE="dropbf_cf_notnanfixed_ood_7_cfproj_7"
#         CLS_CONFIG_TYPE="dropbf"
#     fi
#     echo "CONFIG_TYPE: $CONFIG_TYPE"
#     echo "CLS_CONFIG_TYPE: $CLS_CONFIG_TYPE"
# done
python3.9 /usr/src/app/model_data/alefrts-telegram_bots/send_message_from_terminal.py -m "1"
echo $?
python3.9 /usr/src/app/model_data/alerts-telegram_bots/send_message_from_terminal.py -m "1"
echo $?
python3.9 /usr/src/app/model_data/alerts-telegram_bots/send_message_from_terminal.py -m "SEP"
send_message ()
{
    if [ "$?" == 0 ]; then
        python3.9 /usr/src/app/model_data/alerts-telegram_bots/send_message_from_terminal.py -m "[Completed] ${1} (${2})"
    else
        python3.9 /usr/src/app/model_data/alerts-telegram_bots/send_message_from_terminal.py -m "[FAILED!!!] ${1} (${2})"
    fi
}

python3.9 /usr/src/app/model_data/alefrts-telegram_bots/send_message_from_terminal.py -m "1"
send_message "test1" "test2"
python3.9 /usr/src/app/model_data/alerts-telegram_bots/send_message_from_terminal.py -m "1"
send_message "test3" "test4"
