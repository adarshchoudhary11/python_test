# Q1. Create a class Employee
# with: (3 Marks) 
# • Private variable __salary = 50000
# • Method increment() → salary += 10000 
# • Method deduct() → salary -= 5000
# • Method get_salary() → print salary 
# Create 2 objects and call all methods on both.



class employee:
    def __init__(self):
        self.__salary = 50000
    def increament(self):
        self.__salary += 10000
    def duduct_salary(self):
        self.__salary -= 5000 
    def get_salary(self):
        print("total salary:",self.__salary)
    
emp1=employee()
emp2=employee()

emp1.increament()
emp1.get_salary()
emp1.duduct_salary()


emp2.duduct_salary()
emp2.get_salary()
emp2.increament()
















