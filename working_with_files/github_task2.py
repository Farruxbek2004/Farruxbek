import csv


class Country:
    def __init__(self, file):
        self.file = file

    def get_info_uzbekistan(self):
        result = []
        try:
            with open(self.file, "r", encoding="utf8") as f:
                read_file = csv.DictReader(f)
                for i in read_file:
                    if i.get("country") == "Uzbekistan":
                        result.append(i)
        except FileNotFoundError as e:
            print(e)
        return result

    def get_lat_long(self):

        try:
            with open("lat_long.txt", "w", encoding="utf8") as file:
                for i in self.get_info_uzbekistan():
                    file.write(f"location = https: // my - location.org /?lat = {i.get('lat')} & "
                               f"lng = {i.get('lng')}\n ")
        except FileNotFoundError as e:
            return e
        return file

    def get_uzbekistan(self):
        try:
            with open("uzbekistan.txt", "w", encoding="utf8") as file:
                for i in self.get_info_uzbekistan():
                    # print(i)
                    file.writelines(f"city: {i.get('city')}, lat: {i.get('lat')}, lng: {i.get('lng')}\n")
        except FileNotFoundError as e:
            return e
        return file


country = Country("worldcities.csv")
country.get_lat_long()
country.get_uzbekistan()
