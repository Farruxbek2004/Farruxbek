import telebot
import csv
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand, ReplyKeyboardRemove
from model_3.lesson_8.keyboards import share_phone_btn, get_language_btn, get_csv_file_path
from model_3.lesson_8.todo.messages import messages
from model_3.lesson_8.todo.states import StudentRegistrationForm
from model_3.lesson_8.todo.task import Chat
from model_3.lesson_8.utils import write_row_to_csv, get_fullname
from model_3.lesson_8.todo.Save import Save

BOT_TOKEN = "6093522078:AAF1M1C1a-cCMHWnOPnan5B4B0NEmQ6PCnI"

state_storage = StateMemoryStorage()

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html", state_storage=state_storage)


# /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = get_fullname(user.first_name, user.last_name)
    bot.send_message(chat_id, f"Assalomu alaykum, {fullname} ro'yxatdan o'tish uchun /register buyrug'ini yuboring")


@bot.callback_query_handler(lambda call: call.data.startswith("_language_"))
def set_language_query_handler(call):
    message = call.message
    lang_code = call.data.split("_")[1]
    print(lang_code)
    chat = message.chat
    new_chat = Chat(
        chat.id,
        get_fullname(chat.first_name, chat.last_name),
        lang_code
    )
    write_row_to_csv(
        "chats.csv",
        list(new_chat.get_attrs_as_dict().keys()),
        new_chat.get_attrs_as_dict()
    )
    bot.delete_message(chat.id, message.id)
    bot.send_message(chat.id, messages[lang_code].get("add_task"))


@bot.message_handler(commands=["register"])
def register_student_handler(message):
    bot.send_message(message.chat.id, "Ismingizni kiriting:")
    bot.set_state(message.from_user.id, StudentRegistrationForm.first_name, message.chat.id)


@bot.message_handler(state=StudentRegistrationForm.first_name)
def first_name_get(message):
    bot.send_message(message.chat.id, 'Familyangizni kiriting:')
    bot.set_state(message.from_user.id, StudentRegistrationForm.last_name, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['first_name'] = message.text


@bot.message_handler(state=StudentRegistrationForm.last_name)
def last_name_get(message):
    bot.send_message(message.chat.id, 'Telefon raqaminingizni yuboring:', reply_markup=share_phone_btn)
    bot.set_state(message.from_user.id, StudentRegistrationForm.phone, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['last_name'] = message.text


@bot.message_handler(state=StudentRegistrationForm.phone, content_types=["contact"])
def phone_get(message):
    bot.send_message(message.chat.id, 'Yoshingizni kiriting:', reply_markup=ReplyKeyboardRemove())
    bot.set_state(message.from_user.id, StudentRegistrationForm.age, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['phone'] = message.contact.phone_number


@bot.message_handler(state=StudentRegistrationForm.age)
def age_get(message):
    bot.send_message(message.chat.id, 'Tilni tanlang:', reply_markup=get_language_btn("course"))
    bot.set_state(message.from_user.id, StudentRegistrationForm.language, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = message.text


@bot.callback_query_handler(lambda call: call.data.startswith("course_language_"),
                            state=StudentRegistrationForm.language)
def language_get(call):
    message = call.message
    lang_code = call.data.split("_")[2]
    bot.send_message(message.chat.id, 'Kursni kiriting:')
    bot.set_state(message.from_user.id, StudentRegistrationForm.course, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['language'] = lang_code
        print(lang_code)


@bot.message_handler(content_types=['text'])
def get_task_handler(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['course'] = message.text
        msg = f"Quyidagi ma'lumotlar qa'bul qilindi:\n"
        msg += f"First name: {data.get('first_name')}\n"
        msg += f"Last name: {data.get('last_name')}\n"
        msg += f"Phone: {data.get('phone')}\n"
        msg += f"Age: {data.get('age')}\n"
        msg += f"Language: {data.get('language')}\n"
        msg += f"Course: {data.get('course')}\n"
        msg += "ushbu malumotlar saqlansinmi ?\n"
        msg += "ha -> ✅\n"
        msg += "yo'q -> ❌"
        bot.send_message(message.chat.id, msg, reply_markup=get_csv_file_path('save'))


@bot.callback_query_handler(func=lambda call: call.data.startswith("save"))
def callback(call):
    message = call.message
    text = call.data.split("_")[1]
    if text == "yes":
        with bot.retrieve_data(call.from_user.id, message.chat.id) as data:
            save_info = Save(
                data.get('first_name'),
                data.get('last_name'),
                data.get("phone"),
                data.get("age"),
                data.get("language"),
                data.get("course")
            )

        write_row_to_csv(
            "registration.csv",
            save_info.get_save_func().keys(),
            save_info.get_save_func()
        )

    elif text == "no":
        bot.send_message(message.chat.id, "Ma'lumotlar saqlanmadi qaytadan /register")
    bot.delete_state(message.from_user.id, message.chat.id)


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/register", "Register student")
    ]


bot.add_custom_filter(custom_filters.StateFilter(bot))

if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
