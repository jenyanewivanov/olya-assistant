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
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            bot.send_message(chat_id, "Привет! Я Оля Ассистент 🚀")
        else:
            bot.send_message(chat_id, "Я на связи 👋 Напишите ваш вопрос.")

    return "OK", 200
