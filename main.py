from flask import Flask
import os
import telebot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я Оля Ассистент 🚀\nГотов помогать с продажами."
    )

@app.route("/")
def home():
    return "Bot is running 🚀"

if __name__ == "__main__":
    bot.polling(none_stop=True)
