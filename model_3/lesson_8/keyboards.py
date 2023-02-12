from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

languages_btn = ReplyKeyboardMarkup(resize_keyboard=True)
result_btn = ReplyKeyboardMarkup(resize_keyboard=True)
registratsion_btn = ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGES = {
    "UZ 🇺🇿": "uz",
    "RU 🇷🇺": "ru",
    "EN 🇬🇧": "en"
}

languages_btn.add(
    KeyboardButton(list(LANGUAGES.keys())[0]),
    KeyboardButton(list(LANGUAGES.keys())[1]),
    KeyboardButton(list(LANGUAGES.keys())[2])
)

languages_inline_btn = InlineKeyboardMarkup()

languages_inline_btn.add(
    InlineKeyboardButton(list(LANGUAGES.keys())[0], callback_data=f"language_{list(LANGUAGES.values())[0]}"),
    InlineKeyboardButton(list(LANGUAGES.keys())[1], callback_data=f"language_{list(LANGUAGES.values())[1]}"),
    InlineKeyboardButton(list(LANGUAGES.keys())[2], callback_data=f"language_{list(LANGUAGES.values())[2]}"),
)

share_phone_btn = ReplyKeyboardMarkup(resize_keyboard=True)
share_phone_btn.add(KeyboardButton("Share phone", request_contact=True))


RESULT = {
    "❌": "no",
    "✅": "yes"
}

result_btn.add(
    KeyboardButton(list(RESULT.keys())[0]),
    KeyboardButton(list(RESULT.keys())[1])
)

result_inline_btn = InlineKeyboardMarkup()
result_inline_btn.add(
    InlineKeyboardButton(list(RESULT.keys())[0], callback_data=f'result_{list(RESULT.values())[0]}'),
    InlineKeyboardButton(list(RESULT.keys())[1], callback_data=f'result_{list(RESULT.values())[1]}')
)
REGISTRATSION = {
    "UZ 🇺🇿": "uz",
    "RU 🇷🇺": "ru",
    "EN 🇬🇧": "en"
}

registratsion_btn.add(
    KeyboardButton(list(REGISTRATSION.keys())[0]),
    KeyboardButton(list(REGISTRATSION.keys())[1]),
    KeyboardButton(list(REGISTRATSION.keys())[2])
)
languages_registratsion_btn = InlineKeyboardMarkup()

languages_registratsion_btn.add(
    InlineKeyboardButton(list(REGISTRATSION.keys())[0], callback_data=f"registratsion_{list(REGISTRATSION.values())[0]}"),
    InlineKeyboardButton(list(REGISTRATSION.keys())[1], callback_data=f"registratsion_{list(REGISTRATSION.values())[1]}"),
    InlineKeyboardButton(list(REGISTRATSION.keys())[2], callback_data=f"registratsion_{list(REGISTRATSION.values())[2]}")
)

