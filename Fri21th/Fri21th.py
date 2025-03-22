# # 1. Sort employee based on the salary
# class Employee():
#     def __init__(self, emp_id: int, emp_name: str, emp_salary: int) -> None:
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.emp_salary = emp_salary
#
#     def __gt__(self, other):
#         return self.emp_id > other.emp_id
#
#     def __lt__(self, other):
#         return self.emp_id < other.emp_id
#
#     def __eq__(self, other):
#         return self.emp_id == other.emp_id
#
#     def __repr__(self):
#         return f" Employee id: {self.emp_id} Employee Name :{self.emp_name} Employee Salary: {self.emp_salary} "
#
#     @staticmethod
#     def sort_by_salary(emp_list: list) -> list:
#         emp_list.sort(key=lambda x: x.emp_salary)
#         return emp_list
#
#
# emp1 = Employee(1, "Sam", 5000)
# emp2 = Employee(2, "Ram", 8000)
# emp3 = Employee(3, "Sham", 7000)
#
# emp_list = [emp1, emp2, emp3]
# print(Employee.sort_by_salary(emp_list))


# Arithmatic error without exception handling
def divide(n1: int, n2: int):
    if n2 != 0:
        return n1 / n2
    else:
        print("Please enter non zero denominator")


# check number without exception handling
def number_format(s: str):
    if not s.isnumeric():
        print("Enter valid number")
    else:
        print("number is valid")
# number_format("5a")


# Access element in array without exception handling
def index_out_of_bound(list, index):
    if len(list) > index:
        print(list[index])
    else:
        print("index_out_of_bound")
# list1=[1,2,3,4,5,6]
# index_out_of_bound(list1,5)
