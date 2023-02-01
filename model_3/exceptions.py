from datetime import datetime


def exceptins_func(exceptions):
    with open('exceptions.txt', 'a', encoding='utf-8') as file:
        file.write(f"{exceptions}  {value}\n")


format_ = "%H:%M:%S %m/%d/%Y"
value = datetime.now().strftime(format_)
