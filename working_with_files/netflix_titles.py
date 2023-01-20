# netflix_titles.csv ushbu faylda Netflix kinolari malumotlari mavjud, quyidagi vazifalarni bajaring:
# a) release_year da 2020 va 2021 yildagi kinolar ma'lumotlari bilan birga alohida csv faylga yozing
# b) listed_in ustunidan Comedies bo'lgan filmlarni alohida csv faylga yozing.
# c) type Movie va country United States bo'lgan filmalarni alohida csv faylga yozing.
import csv
import math


class Netflix:
    def __init__(self, file):
        self.file = file

    def netflix_info(self):
        res = []
        try:
            with open(self.file, "r", encoding="utf8") as f:
                read_file = csv.DictReader(f)
                for i in read_file:
                    res.append(i)
        except FileNotFoundError as e:
            print(e)
        return res

    def release_year_info(self):
        read_file = self.netflix_info()
        try:
            with open("new_date.csv", "w", encoding="utf8") as f:
                read_wirite = csv.writer(f, delimiter=',')
                for i in read_file:
                    try:
                        temp_price = math.floor(float(i.get('release_year')))
                    except FileNotFoundError as e:
                        print(e)
                    else:
                        if 2020 <= temp_price <= 2021:
                            read_wirite.writerow(i.values())
        except Exception as e:
            print(e)
        return ''

    def listed_in(self):
        res = []
        read_file = self.netflix_info()
        temp = 'Comedies'
        try:
            with open("listed_in.csv", "w", encoding="utf8") as f:
                writer = csv.writer(f, delimiter=',')
                for i in read_file:
                    temp_listed = (i.get('listed_in')).split()
                    if temp in temp_listed:
                        writer.writerow(i.values())
        except Exception as e:
            print(e)
        return ''

    def type_movie_and_countr(self):
        file = self.netflix_info()
        try:
            with open('movie_united_states.csv', 'w', encoding='utf8') as f:
                writer = csv.writer(f, delimiter=',')
                for i in file:
                    if i.get("country") == "United States":
                        if i.get("type") == "Movie":
                            writer.writerow(i.values())

        except Exception as e:
            print(e)
        return ''


neftlix_file = Netflix("netflix_titles.csv")
# print(neftlix_file.netflix_info())
# print(neftlix_file.release_year_info())
# print(neftlix_file.listed_in())
# print(neftlix_file.type_movie_and_countr())
