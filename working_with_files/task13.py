def add_student(admission: int, student: str, percentage: int) -> None:
    with open('Student.dat', 'a') as file:
        file.write(f'{admission}-{student}-{percentage}\n')


def get_students(percentage: int) -> list:
    with open('Student.dat') as file:
        data = file.readlines()
        students = [list(map(str, x.strip('\n').split('-'))) for x in data]

        return [x for x in students if int(x[2]) >= percentage]


add_student(5, 'Ibrohim', 100)
add_student(6, 'Farrux', 99)
add_student(7, 'Sardor', 40)
add_student(8, 'Bunyod', 66)

for student in get_students(75):
    print(' '.join(student))
