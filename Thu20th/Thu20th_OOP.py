class Employee:
    # Parametrize Constructor - one constructor is enough as py does not support overloading
    def __init__(self, emp_id=1, salary=None, name=None):
        self.emp_id = emp_id
        self.salary = salary
        self.name = name

    def print_salary(self):
        print(f"Salary {self.salary}")
        print(f"Name {self.name}")
        print(f"Emp ID {self.emp_id}")

    # @staticmethod
    def hello(self):
        print("Hello employee this is static method")


# Sub class
class Coder(Employee):
    def __init__(self, emp_id, salary, name, coder_id=1):
        super().__init__(emp_id, salary)
        self.coder_id = coder_id

    def printCoder(self):
        super().print_salary()
        print("this coder ")


coder1 = Coder(178, 7000, "om")
coder1.printCoder()
