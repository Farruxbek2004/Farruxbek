# worldometer_data.csv faylda Covid19 davlatlardagi holatlar keltirilgan quyidagi vazifalarni bajaring.
# a) TotalCases ustunda 100000 va 1000000 orasidagi holatlarni alohida csv faylga yozing.
# b) Country/Region dagi davlatlarni kiritiganda ActiveCases qiymatini qaytarish uchun funksiya yarating.
# c) Continent dagi mintaqa kiritiganda umumiy TotalCases qaytini qaytarish uchun funksiya yarating.
import csv
import math


class Worldometer:
    def __init__(self, file):
        self.file = file

    def worldemeter_info(self):
        result = []
        try:
            with open(self.file, 'r', encoding='utf8') as f:
                new_file = csv.DictReader(f)
                for i in new_file:
                    result.append(i)
        except Exception as e:
            print(e)
        return result

    def totalcases(self):
        read_file = self.worldemeter_info()
        result = []
        try:
            with open('totalcases.csv', 'w', encoding='utf8') as f:
                writer = csv.writer(f, delimiter=',')
                for i in read_file:
                    temp_price = math.floor(float(i.get('TotalCases')))
                    if 100000 <= temp_price <= 1000000:
                        writer.writerow(i.values())

        except FileNotFoundError as e:
            print(e)
        return ''


worldemeter = Worldometer('worldometer_data_1.csv')
print(worldemeter.totalcases())
