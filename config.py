import os
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
chat_id = int(os.getenv("CHAT_ID"))

