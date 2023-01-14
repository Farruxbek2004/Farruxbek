def add_employer(empcode: int, name: str, salary: int) -> None:
    with open('Employee.dat', 'a') as file:
        file.write(f'{empcode}-{name}-{salary}\n')


def get_by_salary(salary: int) -> list:
    with open('Employee.dat') as file:
        data = file.readlines()
        emplyees = [list(map(str, x.strip('\n').split('-'))) for x in data]

        return [x for x in emplyees if int(x[2]) >= salary]


add_employer(6, 'Maksim', 9009)
add_employer(7, 'Lola', 4000)
add_employer(8, 'Tola', 6006)

for employee in get_by_salary(3000):
    print(' '.join(employee))
