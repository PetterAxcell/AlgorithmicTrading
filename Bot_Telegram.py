import telebot
from telebot import types
import time
import Bot_Binance
from Bot_Binance import BinanceBot 

TOKEN = '725147310:AAGZFMSWcSLTUS7nLBNsb-KYV0nFEg0c9ow'
YO = '864345672'

AYUDA = 'Información necesaria'

bot = telebot.TeleBot(TOKEN)
x = Bot_Binance.BinanceBot() 
   

@bot.message_handler(commands=["show"]) # Indicamos que lo siguiente va a controlar el comando '/ayuda'
def command_ayuda(m): # Definimos una función que resuleva lo que necesitemos.
    s='BTCUSDT' 
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    
    bot.send_chat_action(cid, 'typing') 
    # # Enviando ...
 
    time.sleep(1) 
    
    x.GetData(s)
    
    print(x.data)
    
    bot.send_message(cid, x.data) 
    
    
    

bot.polling()

