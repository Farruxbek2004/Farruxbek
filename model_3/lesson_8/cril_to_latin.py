import telebot
from model_3.lesson_5.transliterate import to_latin, to_cyrillic

BOT_TOKEN = "6007107558:AAECgl62J7wTRo_tpGP6aw3HgWo5lG3D3EU"
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id, f"Assalomu Aleykum {user.first_name}")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    msg = message.text
    value = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, value(msg))


if __name__ == "__main__":
    print("Started...")
    bot.infinity_polling()
