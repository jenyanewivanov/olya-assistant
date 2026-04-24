from flask import Flask, request
import os
import telebot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Olya is working 🚀"

@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    json_data = request.get_json()
    if json_data:
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я Оля Ассистент 🚀\nГотова помогать с продажами."
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(
        message.chat.id,
        "Я на связи 👋 Напишите, пожалуйста, для кого песня и к какой дате нужна?"
    )
