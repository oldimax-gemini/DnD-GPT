from fastapi import FastAPI, Request
import telebot
from app.config import TELEGRAM_TOKEN, WEBHOOK_URL

bot = telebot.TeleBot(TELEGRAM_TOKEN)
app = FastAPI()

@app.on_event("startup")
def startup():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)

@app.post("/")
async def webhook(request: Request):
    data = await request.json()
    update = telebot.types.Update.de_json(data)
    bot.process_new_updates([update])
    return {"ok": True}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "?? RPG стартовала!")