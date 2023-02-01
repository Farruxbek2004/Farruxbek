class Hotel:
    def __init__(self, fullname, age, address, lenghth_of_stay,summa, country):
        self.fullname = fullname
        self.age = age
        self.address = address
        self.lenghth_of_stay = lenghth_of_stay
        self.summa = summa
        self.country = country

    def get_attrs(self, as_dict=False):
        if as_dict:
            return {
                "Fullname": self.fullname,
                "Age": self.age,
                "Address": self.address,
                "Lenghth of stay": self.lenghth_of_stay,
                "Summa": self.summa,
                "Country": self.country
            }
        return [
            self.fullname,
            self.age,
            self.address,
            self.lenghth_of_stay,
            self.summa,
            self.country
        ]
