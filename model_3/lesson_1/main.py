# SQLite bilan ishlash
# iterator va generators
# Decorotors
import csv


class CSVManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self):
        try:
            with open(self.file_path) as csv_file:
                csv_reader = csv.reader(csv_file)
                return [row for row in csv_reader]
        except (FileNotFoundError, UnicodeDecodeError) as e:
            print(e)

    def get_data_with_dict(self):
        try:
            with open(self.file_path) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                return [row for row in csv_reader]
        except (FileNotFoundError, UnicodeDecodeError) as e:
            print(e)

    def get_language_info(self, programming_lang):
        """
        # Python
        # Avgust 2004: 30
        # Avgust 2005: 31
        # Avgust 2006: 32
        :param programming_lang:
        :return:
        """
        data = self.get_data()
        header = [item.lower() for item in data.pop(0)]
        if programming_lang.lower() not in header:
            return "Language not found."

        target_index = None
        for index, item in enumerate(header):
            if programming_lang == item:
                target_index = index

        result = f"{programming_lang.title()}\n"
        for row in data:
            result += f"{row[0]}: {row[target_index]}\n"

        return result

    def info(self):
        data = self.get_language_info("python")
        count = 0
        a = 3
        res = []
        try:
            with open("new.csv", "w", encoding='utf8') as f:
                for i in data.split():
                    count += 1
                    f.write(f"{i}\n")
                    if count == a:
                        a += 3
                        for j in i.split():
                            print(j)
        except FileNotFoundError as e:
            print(e)
        return ''

    # def get_language_info_with_dict(self, programming_lang):
    #     data = self.get_data_with_dict()
    #     for row in data:
    #         print("row", row.get(programming_lang))
    #
    # def writer(self, data):
    #     with open(self.file_path, "w") as f:
    #         csv_writer = csv.writer(f)
    #         # csv_writer.writerows(data)
    #         for row in data:
    #             csv_writer.writerow(row)

    # def writer_with_dict(self, data, header):
    #     mode = "a"
    #     with open(self.file_path, mode, newline="\n") as f:
    #         csv_writer = csv.DictWriter(f, header)
    #         if mode == "w":
    #             csv_writer.writeheader()
    #         csv_writer.writerows(data)


csv_obj = CSVManager("Most Popular Programming Languages from 2004 to 2022.csv")
# print(csv_obj.get_language_info("python"))
csv_obj.info()
# csv_obj.get_language_info_with_dict("Python")
