import telebot
import os
import csv
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand, ReplyKeyboardRemove
from datetime import datetime
from model_3.lesson_8.keyboards import languages_inline_btn, share_phone_btn, result_inline_btn, languages_registratsion_btn
from model_3.lesson_8.todo.messages import messages, result
from model_3.lesson_8.todo.states import StudentRegistrationForm
from model_3.lesson_8.todo.task import Chat, Task
from model_3.lesson_8.utils import write_row_to_csv, get_fullname, get_language_code_by_chat_id

BOT_TOKEN = "6093522078:AAF1M1C1a-cCMHWnOPnan5B4B0NEmQ6PCnI"

state_storage = StateMemoryStorage()

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html", state_storage=state_storage)


# /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = get_fullname(user.first_name, user.last_name)
    bot.send_message(chat_id, f"Assalomu alaykum, {fullname}", reply_markup=languages_inline_btn)


@bot.callback_query_handler(lambda call: call.data.startswith("language_"))
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
    bot.send_message(message.chat.id, 'Tilni tanlang:', reply_markup=languages_registratsion_btn)
    bot.set_state(message.from_user.id, StudentRegistrationForm.language, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = message.text


@bot.callback_query_handler(lambda call: call.data.startswith("registratsion_"))
def language_query_handler(call):
    message = call.message
    lang_code = call.data.split("_")[1]
    chat = message.chat
    # bot.delete_message(chat.id, message.id)
    bot.send_message(chat.id, result[lang_code].get('res'))


@bot.message_handler(state=StudentRegistrationForm.language)
def language_get(message):
    bot.send_message(message.chat.id, 'Kursni kiriting:')
    bot.set_state(message.from_user.id, StudentRegistrationForm.course, message.chat.id)
    print(message.text)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['language'] = message.text


@bot.message_handler(state=StudentRegistrationForm.course)
def course_get(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['course'] = message.text
        msg = "Quyidagi ma'lumotlar qa'bul qilindi:\n"
        msg += f"Fullname: {data.get('first_name')} {data.get('last_name')}\n"
        msg += f"Phone: {data.get('phone')}\n"
        msg += f"Age: {data.get('age')}\n"
        msg += f"Language: {data.get('language')}\n"
        msg += f"Course: {data.get('course')}\n"
        msg += "ushbu malumotlar saqlansinmi ?\n"
        msg += "ha -> ✅\n"
        msg += "yo'q -> ❌"
        bot.send_message(message.chat.id, msg, parse_mode="html", reply_markup=result_inline_btn)
        with open("registratsion.csv", 'a', newline="\n") as f:
            header = ['first_name', 'last_name', "phone", "age", "language", "course"]
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            phone = data.get('phone')
            age = data.get('age')
            language = data.get('language')
            course = data.get('course')
            dict_writer = csv.writer(f)
            if os.path.getsize('registratsion.csv') == 0:
                dict_writer.writerow(header)
            dict_writer.writerow([first_name, last_name, phone, age, language, course])
    # bot.delete_state(message.from_user.id, message.chat.id)


@bot.callback_query_handler(lambda call: call.data.startswith("result_"))
def set_result(call):
    message = call.message
    lang_code = call.data.split('_')[1]
    print(lang_code)
    chat = message.chat
    bot.delete_message(chat.id, message.id)
    bot.send_message(message.chat.id, value[lang_code].get("res"))


value = {
    'no': {
        "res": "/register"
    },
    "yes": {
        "res": "Sizning ma'lumotlaringgiz csv file ga saqlandi"
    }
}


# /add
@bot.message_handler(commands=["add"])
def add_task_handler(message):
    chat_id = message.chat.id
    lang_code = get_language_code_by_chat_id(chat_id, "chats.csv")
    msg = messages[lang_code].get("send_task")
    bot.send_message(message.chat.id, msg)


@bot.message_handler(content_types=["text"])
def get_task_handler(message):
    chat_id = message.chat.id
    if message.content_type != "text":
        bot.send_message(chat_id, "Invalid format.")

    new_task = Task(chat_id, message.text, datetime.now())
    write_row_to_csv(
        "tasks.csv",
        list(new_task.get_attrs_as_dict().keys()),
        new_task.get_attrs_as_dict()
    )

    bot.send_message(chat_id, "Add successfully.")


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/add", "Add new task"),
        BotCommand("/register", "Register student")
    ]


bot.add_custom_filter(custom_filters.StateFilter(bot))

if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
