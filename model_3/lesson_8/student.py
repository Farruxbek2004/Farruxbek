from model_3.lesson_5.transliterate import  *
class Student:
    def __init__(self, fulname, chat_id):
        self.chat_id = chat_id
        self.fullname = fulname

    def get_attrs_for_csv_writer(self):
        return {
            "chat_id": self.chat_id,
            "fullname": self.fullname
        }


la = to_latin("салом")
print(la)
