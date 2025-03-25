class Employee():
    def __init__(self, emp_id: int, emp_name: str, emp_salary: int) -> None:
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def __gt__(self, other):
        return self.emp_id > other.emp_id

    def __lt__(self, other):
        return self.emp_id < other.emp_id

    def __eq__(self, other):
        return self.emp_id == other.emp_id

    def __repr__(self):
        return f" Employee id: {self.emp_id} Employee Name :{self.emp_name} Employee Salary: {self.emp_salary} "

    @staticmethod
    def sort_by_salary(emp_list: list) -> list:
        emp_list.sort(key=lambda x: x.emp_salary)
        return emp_list

class invalid_id(Exception):
    def __init__(self,msg):
        self.msg=msg

emp_id=input("Please enter Employee ID")
try:
    if not emp_id.isnumeric():
        raise invalid_id("Please input only numbers")

except invalid_id as e:
    print(e)

else:
    print(emp_id)