from flask import Flask, request
import os
import telebot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running 🚀"

@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    json_data = request.get_data().decode("utf-8")

    update = telebot.types.Update.de_json(json_data)
    bot.process_new_updates([update])

    return "OK", 200


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я Оля Ассистент 🚀"
    )


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(
        message.chat.id,
        "Я на связи 👋 Напишите ваш вопрос."
    )
