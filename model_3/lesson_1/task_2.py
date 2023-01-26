import csv


class ListOfAccount:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def get_info(self):
        result = []
        try:
            with open(self.csv_file) as files:
                file = csv.DictReader(files)
                for i in file:
                    result.append(i)
        except FileNotFoundError as e:
            write_exceptions(e)
        return result

    def most_followed_instagram_accounts(self):
        country_data_name = {}
        data = self.get_info()
        header = list(data[0].keys())
        for i in data:
            country_name = i.get('Country/Continent')

            if country_name not in list(country_data_name.keys()):
                country_data_name[country_name] = i
            else:
                country_data_name.get(country_name).append(i)
        return country_data_name


list_of_account = ListOfAccount("List of most-followed Instagram accounts.csv")
print(list_of_account.most_followed_instagram_accounts())
