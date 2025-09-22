print("--- Python OPP Project: Employee Management System---")

print("Choose a operation")
print("1.Create a person")
print("2.Create an employee")
print("3.Create a manager")
print("4.Show details")
print("5.Compare salaries")
print("6.Exit")

class Person:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

class employee(Person):
    def __init__(self, Name, age, employee, salary):
        self.name=Name
        self.age=age
        self.employee=employee
        self.salary=salary

class manager(Person):
    def __init__(self, Name, age, employeeID, salary,department):
        self.name=Name
        self.age=age
        self.employeeID=employeeID
        self.salary=salary
        self.department=department

person=[]

choice=int(input("enter your choice:"))
Name=input("Enter Name:")
Age=int(input("Enter Age:"))
print(f"person created with name:{Name} and age:{Age}")

print("---chooose another operation---")

print("Choose a operation")
print("1.Create a person")
print("2.Create an employee")
print("3.Create a manager")
print("4.Show details")
print("5.Compare salaries")
print("6.Exit")

choice=int(input("enter your choice:"))
Name=input("Enter Name:")
Age=int(input("Enter Age:"))
EmployeeID=input("Enter Employee ID:")
Salary= int(input("Enter salary:"))
print(f"Employee created with name:{Name}, age:{Age},EmployeeID:{EmployeeID},Salary:{Salary}")

print("---chooose another operation---")

print("Choose a operation")
print("1.Create a person")
print("2.Create an employee")
print("3.Create a manager")
print("4.Show details")
print("5.Compare salaries")
print("6.Exit")
 
choice=int(input("enter your choice:"))
Name=input("Enter Name:")
Age=int(input("Enter Age:"))
EmployeeID=input("Enter Employee ID:")
Salary=int(input("Enter salary:"))
Department=input("Enter Department:")
print(f"Manager created with name:{Name}, age:{Age},EmployeeID:{EmployeeID},Salary:{Salary} and Department:{Department}")

print("---chooose another operation---")

print("Choose a operation")
print("1.Create a person")
print("2.Create an employee")
print("3.Create a manager")
print("4.Show details")
print("5.Compare salaries")
print("6.Exit")

choice=int(input("enter your choice:"))

print("Choose details to show:")
print("1.person")
print("2.Employee")
print("3.Manager")
choice=int(input("enter your choice:"))

print("Employee details:")

# print(f"Employee created with name:{Name}, age:{Age},EmployeeID:{EmployeeID},Salary:{Salary}")
Name=input("Name:") 
Age=int(input(" Age:"))
EmployeeID=input(" Employee ID:")
Salary=input("salary:")

print("---chooose another operation---")

print("Choose a operation")
print("1.Create a person")
print("2.Create an employee")
print("3.Create a manager")
print("4.Show details")
print("5.Compare salaries")
print("6.Exit")

choice=int(input("enter your choice:"))

print("Exiciting the system. All resources have been freed.")

print("Goodbye")