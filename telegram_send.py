
import requests

def telegram_bot_sendtext(bot_message):
    bot_token = '5407342879:AAHlDpvpvtoiwl1EpIX1cfPVzzBCGkQdeKM'
    bot_chatID= '862882175'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=' + bot_message
    return requests.get(send_text)
    return respond.json
    telegram_bot_sendtext("data") #data should be in string 
