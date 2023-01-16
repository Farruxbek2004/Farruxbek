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


def get_population_gt_20M():
    """
    Population greater than or equal 20M
    return = []
    """
    result = []
    with open("countries of the world.csv") as f:
        lines = f.readlines()

    for line in lines[1:]:
        try:
            name, count = (line.split(",")[0].strip()), int(line.split(",")[2].strip())
        except  ValueError as e:
            print(e)
        else:
            if count > 20000000:
                result.append(f"{name}: {count}")

    return result


def get_countries_with_c():
    result = []
    with open("countries of the world.csv") as f:
        lines = f.readlines()

    # for line in lines[1:]:
    #     name = line.splitt(",")[0].strip()
    #     if name.startswith("C"):
    #         result.append()
    result = [
        line.split(",")[0].strip()
        for line in lines[1:]
        if line.split(",")[0].strip().startswith("C")
    ]

    return result


print(get_countries_with_c())
