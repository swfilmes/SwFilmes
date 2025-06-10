import os
import telebot
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Sou o bot SwFilmes. Postagens automáticas às 07h e 20h.")

def enviar_postagem_automatica():
    agora = datetime.now().strftime("%H:%M")
    if agora == "07:00":
        bot.send_message(GROUP_ID, "🌞 Bom dia! Aqui vai o filme/série do dia!")
    elif agora == "20:00":
        bot.send_message(GROUP_ID, "🌙 Boa noite! Prepare a pipoca! Aqui vai o conteúdo da noite!")

if __name__ == "__main__":
    enviar_postagem_automatica()