# Sales_April_2019.csv faylda berilgan ma'lumotlar orqali quyidagilarni bajaring.
# a) Macbook Pro Laptop mahsulotdan nechta buyurtma bo'lganini aniqlang.
# b) Price Each ustun orqali 300 dan katta bo'lgan buyurtmalarni txt faylga yozing.
# c) 04/10/19 sanadan keyingi buyurmalarni boshqa csv faylga yozing
import csv
import math


class Sales:
    def __init__(self, file):
        self.file = file

    def sales_get_info(self):
        result = []
        try:
            with open(self.file, "r", encoding="utf8") as f:
                read_file = csv.DictReader(f)
                for i in read_file:
                    result.append(i)
        except FileNotFoundError as e:
            print(e)
        return result

    def macbook_pro_laptop_count(self):
        count = 0
        try:
            with open(self.file, "r", encoding="utf8") as f:
                read_file = csv.DictReader(f)
                for i in read_file:
                    if i.get("Product") == "Macbook Pro Laptop":
                        count += 1
        except FileNotFoundError as e:
            print(e)
        return f"Macbook Pro Laptop lar soni - {count}  ta"

    def price_each(self):
        res = self.sales_get_info()
        with open("price_each.txt", "w", encoding="utf8") as file:
            for i in res:
                try:
                    temp_price = math.floor(float(i.get('Price Each')))
                except Exception as e:
                    print(e)
                else:
                    if temp_price > 300:
                        file.writelines(f"Product: {i.get('Product')},"
                                        f" ID: {i.get('ID')}, Price Each: {i.get('Price Each')}\n")
        return ''

    def get_data(self):
        res = self.sales_get_info()
        data = ["04/10/19"]
        try:
            with open("new_date.csv", "w") as file:
                for i in res:
                    if data < i.get("Order Date"):
                        file.write(i.get("Order Data"))
        except Exception as e:
            print(e)
        return file


sales = Sales("Sales_April_2019.csv")
# print(sales.macbook_pro_laptop_count())
# print(sales.sales_get_info())
# print(sales.price_each())
print(sales.get_data())
