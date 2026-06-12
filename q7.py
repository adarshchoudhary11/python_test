# Q7. Create an Employee File System: (3 Marks) 
# • Create 'employees.txt' with 3 employees 
# • Read the file and print • Append 2 more employees
# • Read updated file • Delete the file and 
# verify using os.path.exists()

import os

with open("employees.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Rohan\n")


print("Initial Employees:")
with open("employees.txt", "r") as file:
    print(file.read())

with open("employees.txt", "a") as file:
    file.write("Sneha\n")
    file.write("Amit\n")


print("Updated Employees:")
with open("employees.txt", "r") as file:
    print(file.read())

os.remove("employees.txt")

if not os.path.exists("employees.txt"):
    print("File deleted successfully!")
else:
    print("File still exists!")