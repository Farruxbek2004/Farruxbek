import telebot
from translate import Translator
from telebot.types import BotCommand

BOT_TOKEN = "5799385082:AAFka7bvW8CKIX1Jf_fd6HlAVuodkeF8QmU"
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "👋 Assalomu alaykum ......\n"
                              "Botdan foydalanmoqchi bo'lganinggiz uchun raxmat!\n"
                              "Bironta xatolik yuz bersa https://t.me/Yunusboyev_Farruxbek")



@bot.message_handler(commands=["enuz"])
def translate_english_uzbek(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id,
                       "English - O'zbek holatiga o'tildi. 'O'zbek - Rus holatiga o'tish uchun /uzru buyrug'ini bering.")
    bot.register_next_step_handler(msg, tarjima_en_uz)

def tarjima_en_uz(message):
    trans = Translator(from_lang='en', to_lang='Uzb')
    translation = trans.translate(message.text)
    bot.reply_to(message, translation)




@bot.message_handler(commands=["uzru"])
def translate_uzbek_rus(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id,
                     "'O'zbek - Rus' holatiga o'tildi. 'English - O'zbek' holatiga o'tish uchun /enuz buyrug'ini bering.")

    bot.register_next_step_handler(msg, translate_uz_ru)


@bot.message_handler(func=lambda message: True)
def translate_uz_ru(message):
    trans = Translator(from_lang='Uzb', to_lang='ru')
    translation = trans.translate(message.text)
    bot.reply_to(message, translation)
def my_command():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/enuz", "English - Uzbek"),
        BotCommand("/uzru", "Uzbek - Russian")
    ]


if __name__ == "__main__":
    print("started...")
    bot.set_my_commands(commands=my_command())
    bot.infinity_polling()
