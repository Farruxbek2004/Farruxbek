from datetime import datetime

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from model_3.lesson_8.utils import get_weather_days

days_btn = ReplyKeyboardMarkup(row_width=True)

for day in get_weather_days():
    formatted_day = datetime.strptime(day, "%Y.%m.%d").strftime("%b %d %Y")
    days_btn.add(
        KeyboardButton(formatted_day)
    )
