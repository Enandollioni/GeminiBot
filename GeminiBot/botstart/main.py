import telebot
import os
from dotenv import load_dotenv
import google.generativeai as genai
import handlers.message_handlers as msg_handlers


def start():
    bot.infinity_polling()


load_dotenv()
Token = str(os.getenv('TOKEN'))  # Токен телеграм бота
bot = telebot.TeleBot(Token, parse_mode=None)

api_key = os.getenv("GEMINI_API_KEY")  # API ключ от нейросети
genai.configure(api_key=api_key)

# Настройка модели
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])
msg_handlers.register_handlers(bot, convo)  # регистрация хендлеров
start()  # пуллинг бота

