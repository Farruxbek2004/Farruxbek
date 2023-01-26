def exceptins_func(exceptions, e):
    with open('exceptions.txt', 'w', encoding='utf-8') as file:
        exception = f'name : {exceptions} , meaning : {e}'
        file.write(f"{exception}\n")
