## Employee Salary Management

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary

    def increment_salary(self, amount):
        self.salary += amount


    def anual_salary(self):
        return self.salary * 12

    def display(self):
        print(f"ID: {self.emp_id}, name: {self.name}, Monthly_salary: {self.salary}, Annual_Salary: {self.anual_salary()} ")

emp1 = Employee(101, "Roshani", 85000)
emp2 = Employee(102, "Shubham", 75000)
emp3 = Employee(103, "Rushi", 80000)

emp1.increment_salary(2000)
emp2.increment_salary(5000)
emp3.increment_salary(4000)


emp1.display()
emp2.display()
emp3.display()