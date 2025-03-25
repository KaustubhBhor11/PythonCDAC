class Employee:
    def __init__(self,emp_id: int,name: str,basic_salary:int)->None:
        self.emp_id=emp_id
        self.name=name
        self.basic_salary=basic_salary
        self.hra=basic_salary*0.05
        self.pf=basic_salary*0.12
        self.pt=200
    
    def gross_salary(self)->float:
        gross_salary=self.basic_salary+self.hra+self.pt+self.pf
        return gross_salary
    
    def net_salary(self)->float:
        net_salary=self.gross_salary()-self.pf-self.pt
        return net_salary

class Manager(Employee):
    def __init__(self, emp_id: int, name: str, basic_salary: int)->None:
        super().__init__(emp_id, name, basic_salary)
        self.food_allowance=self.basic_salary*0.1
        self.manager_allowance=self.basic_salary*0.05
        self.other_allowance=self.basic_salary*0.03
    
    def gross_salary(self)->float:
        manager_gross_salary=super().gross_salary()+self.food_allowance+self.manager_allowance+self.other_allowance
        return manager_gross_salary

    def net_salary(self)->float:
        manager_net_salary=self.gross_salary()-self.pf-self.pt
        return manager_net_salary

class MarketingExecutive(Employee):
    def __init__(self, emp_id: int, name: str, basic_salary: int,traveled_km: int)-> None:
        super().__init__(emp_id, name, basic_salary)
        self.phone_allowance=1500
        self.travel_allowance=traveled_km*33

    def gross_salary(self)-> float:
        marketing_exec_gross_salary=super().gross_salary()+self.phone_allowance+self.travel_allowance
        return marketing_exec_gross_salary
    
    def net_salary(self)-> float:
        marketing_exec_net_salary=self.gross_salary()-self.pf-self.pt
        return marketing_exec_net_salary
    
employee_obj=Employee(562,"om",60000)
manager_obj=Manager(891,"Tim",120000)
marketing_exec_obj=MarketingExecutive(424,"ram",70000,134)

print(f"Employee Gross Salary: {employee_obj.gross_salary()}")
print(f"Employee Net Salary: {employee_obj.net_salary()}")
print(f"Manager Gross Salary: {manager_obj.gross_salary()}")
print(f"Manager Net Salary: {manager_obj.net_salary()}")
print(f"Marketing Executive Gross Salary: {marketing_exec_obj.gross_salary()}")
print(f"Marketing Executive Net Salary: {marketing_exec_obj.net_salary()}")
