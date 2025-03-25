class Employee:

    count=0
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.hra = self.basic_salary * 0.5
        self.pt = 200
        self.pf = 0.12 * self.basic_salary
        Employee.count+=1

    def __repr__(self): # toString like java
        return f"Emp is : { self.emp_id} name is : { self.name} basic_salary is : { self.basic_salary}"

    def __eq__(self,other): # define comparable logic if two objects are equal
        if self.emp_id == other.emp_id:
            return True
        else:
            return False

    def __gt__(self, other): # define comparable logic if two objects are greater then
        if self.emp_id > other.emp_id:
            return True
        else:
            return False

    def __lt__(self, other):# define comparable logic if two objects are less then
        if self.emp_id < other.emp_id:
            return True
        else:
            return False

    #Similar to operator overloading
    def __add__(self, other):
        return self.basic_salary + other.basic_salary

    def __sub__(self, other):
        return self.basic_salary - other.basic_salary

    def gross_salary(self):
        return self.basic_salary + self.hra + self.pt + self.pf

    def net_salary(self):
        return self.basic_salary + self.hra

    @staticmethod
    def count_instance():
        return Employee.count


class Manager(Employee):

    def __init__(self, emp_id, name, basic_salary):
        super().__init__(emp_id, name, basic_salary)
        self.other_allowance = self.basic_salary * 0.03
        self.food_allowance = self.basic_salary * 0.1
        self.manger_allowance = self.basic_salary * 0.05

    def gross_salary(self):
        return super().gross_salary() + self.food_allowance + self.manger_allowance + self.other_allowance

    def net_salary(self):
        manager_net_salary = self.gross_salary() - self.pf - self.pt
        return manager_net_salary


class Marketing_Executive(Employee):

    def __init__(self, emp_id, name, basic_salary, travel_km):
        super().__init__(emp_id, name, basic_salary, )
        self.phone_allowance = 1500
        self.travel_allowance = travel_km * 7

    def gross_salary(self) -> float:
        marketing_exec_gross_salary = super().gross_salary() + self.phone_allowance + self.travel_allowance
        return marketing_exec_gross_salary

    def net_salary(self) -> float:
        marketing_exec_net_salary = self.gross_salary() - self.pf - self.pt
        return marketing_exec_net_salary


Marketing_Executive1 = Marketing_Executive(1, "Bob", 1000, 50)
manager1 = Manager(2, "Martin", 2100)
emp1 = Employee(1, "Dan", 20000)
emp2 = Employee(2, "San", 40000)
c=Employee.count_instance()
print(f"Object created {c} times ")
a = int(input())
print("this is a ",a)






# create list of objects
l = [Marketing_Executive1, manager1, emp1]

print(l)
print(f"Employee Gross Salary: {emp1.gross_salary()}")
print(f"Employee Net Salary: {emp1.net_salary()}")
print(f"Manager Gross Salary: {manager1.gross_salary()}")
print(f"Manager Net Salary: {manager1.net_salary()}")
print(f"Marketing Executive Gross Salary: {Marketing_Executive1.gross_salary()}")
print(f"Marketing Executive Net Salary: {Marketing_Executive1.net_salary()}")
print(f"Marketing Executive Travel allowance: {Marketing_Executive1.travel_allowance}")


# Method 1: Using type function to segregate objects
# managers_list=[]
# Employees_list=[]
# Marketing_Executive_list=[]
# for i in l:
#     if "Manager" in str(type(i)):
#         managers_list.append(i)
#     elif  "Marketing_Executive" in str(type(i)):
#         Marketing_Executive_list.append(i)
#     else:
#         Employees_list.append(i)
#
# print(f" Empployee List : {Employees_list}")
# print(f" Manager List : {managers_list}")
# print(f" Marketing Executive List : {Marketing_Executive_list}")

# Method 2: using the isInstance function segregate objects
# employee_list = []
# manager_list = []
# marketing_exec_list = []
# for i in l:
#     if isinstance(i, Manager):
#         manager_list.append(i)
#     elif isinstance(i, Marketing_Executive):
#         marketing_exec_list.append(i)
#     else:
#         employee_list.append(i)
#
# print(f"Empployee List : {employee_list}")
# print(f"Manager List : {manager_list}")
# print(f"Marketing Executive List : {marketing_exec_list}")


# Multiple Inheritance /Diamond problem
class devmanus():
    def hello(self):
        print("This is Devmanus")


class dev(devmanus):
    def hello(self):
        print("This is Dev")


class test(devmanus):
    def hello(self):
        print("This is test")


class devtest(dev, test):
    def test_hello(self):
        test.hello(self)  # Using the hello from test

    def dev_hello(self):
        super().hello()  # Using the hello method from the dev class. super uses the hello from dev class due to MRO



devtest1 = devtest()
devtest1.dev_hello()
devtest1.test_hello()
