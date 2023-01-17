import csv

#
#
# class Country:
#     def __init__(self, file):
#         self.file = file
#
#     def get_lines(self):
#         try:
#             open(self.file, 'r')
#         except FileNotFoundError as e:
#             print(e)
#         else:
#             with open(self.file, "r") as file:
#                 return file.readlines()
#
#     def get_countries_names(self):
#         data = self.get_lines()[0].split(",")
#         print(data)
#         result = {}
#         for i in range(len(data)):
#             result[i + 1] = data[i]
#         return result
#
#     def get_column_values(self, column_index):
#
#         # column_index =
#
#         column_values = []
#         data = self.get_lines()
#         for i in range(1, len(data)):
#             column_values.append(data[i].split(',')[column_index - 1].strip('""').strip())
#         return column_values
#
#     def get_column_names(self):
#         return self.get_lines()[3].split(",")
#
#
# def countr_GDP(countries, countries_popultions):
#     for i in range(len(countries)):
#         try:
#             if int(countries[i]) > 1000:
#                 print(countries_popultions[i], countries[i])
#         except ValueError:
#             pass
#
#
# def countr_populations(population, countries_popultions_2):
#     for i in range(len(population)):
#         try:
#             if int(population[i]) > 20000000:
#                 print(countries_popultions_2[i], population[i])
#         except ValueError:
#             pass
#
#
# country = Country("countries of the world.csv")
#
# countries = country.get_column_values(13)
# countries_popultions = country.get_column_values(1)
# countries_popultions_2 = country.get_column_values(1)
# population = country.get_column_values(3)
# print("------------GDP 1000 --------- ")
# print(countr_GDP(countries, countries_popultions))
# print("----------populations 20000000 -------------\n\n\n ")
# print(countr_populations(population, countries_popultions_2))


import csv


def get_countries_data(file_path):
    with open(file_path) as f:
        data = [[value.strip() for value in row] for row in csv.reader(f)]
    return data


print(get_countries_data("../solutions/custom_data.csv"))


def custom_csv_writer(file_path, columns, data):
    with open(file_path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(columns)
        csv_writer.writerows(data)


def custom_csv_writer_with_dict(file_path, columns, data):
    with open(file_path, "w") as f:
        csv_writer = csv.DictWriter(f, columns)
        csv_writer.writeheader()
        csv_writer.writerows(data)


header = ['Country', 'Region', 'Population', 'Area (sq. mi.)', 'GDP ($ per capita)']
data = [
    ['Afghanistan ', 'ASIA (EX. NEAR EAST)', '31056997', '647500', '700'],
    ['Albania ', 'EASTERN EUROPE                     ', '3581655', '28748', '4500'],
    ['Algeria ', 'NORTHERN AFRICA                    ', '32930091', '2381740', '6000'],
]

dict_header = ['name', 'area', 'country_code2', 'country_code3']

rows = [
    {
        'name': 'Albania',
        'area': 28748,
        'country_code2': 'AL',
        'country_code3': 'ALB'
    },
    {
        'name': 'Algeria',
        'area': 2381741,
        'country_code2': 'DZ',
        'country_code3': 'DZA'
    },
    {
        'name': 'American Samoa',
        'area': 199,
        'country_code2': 'AS',
        'country_code3': 'ASM'
    }
]

custom_csv_writer_with_dict("../solutions/custom_data.csv", dict_header, rows)
