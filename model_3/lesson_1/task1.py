import csv
from ..exceptions import exceptins_func


class EmployeeDepartment:
    def __init__(self, employee_file, department_file):
        self.employee_file = employee_file
        self.department_file = department_file

    def employee_department_get_info(self):
        employee_info = []
        department_info = []
        try:
            with open(self.employee_file, "r", encoding="utf8") as f:
                csv_reader = csv.DictReader(f)
                for i in csv_reader:
                    employee_info.append(i)

        except FileNotFoundError as e:
            print(e)

        try:
            with open(self.department_file, "r", encoding="utf8") as file2:
                csv_reader_2 = csv.DictReader(file2)
                for j in csv_reader_2:
                    department_info.append(j)
        except FileNotFoundError as e:
            print(e)
        return employee_info, department_info

    def new_employee_department_cdv(self):
        data_employee = self.employee_department_get_info()[0]
        data_department = self.employee_department_get_info()[1]
        data_calendar = {
            '01': "Yanvar",
            '02': "Fevral",
            '03': "Mart",
            '04': "Aprel",
            '05': "May",
            '06': "Iyun",
            '07': "Iyul",
            '08': "Avgust",
            '09': "Sentyabr",
            '10': "Oktyabr",
            '11': "Noyabr",
            '12': "Dekabr",
        }

        try:
            with open('new_file.csv', 'w') as f:
                f.write('Employee ID,DOB,DOJ,Department_Name\n')
                for i in data_employee:
                    for j in data_department:
                        f.write(
                            f'{i.get("Employee ID")},{i.get("DOB")[:10]},{i.get("DOJ")},{j.get("Department_Name")}\n')
        except Exception as e:
            print(e)

        return ''


employee_obj = EmployeeDepartment("Employee_Information.csv", "Department_Information.csv")
print(employee_obj.new_employee_department_cdv())
