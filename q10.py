
# Q10. Perform the following Dictionary operations: (2 Marks)
# • Create a dictionary of 3 students: {'name': ..., 'age': ..., 'marks': ...} 
# • Add a new student and update marks of an existing student
# • Delete a student using del and check if a key exists using 'in'
# • Loop through the dictionary and print all keys, values, and items
# • Convert all student names to a list using dict.keys()


students = {
    "Rahul": {"age": 20, "marks": 85},
    "Priya": {"age": 21, "marks": 90},
    "Rohan": {"age": 19, "marks": 78}
}

students["Sneha"] = {"age": 22, "marks": 92}

students["Rahul"]["marks"] = 88


del students["Rohan"]


if "Priya" in students:
    print("Priya exists in the dictionary")
else:
    print("Priya does not exist")

print("\nKeys:")
for key in students.keys():
    print(key)


print("\nValues:")
for value in students.values():
    print(value)

print("\nItems:")
for item in students.items():
    print(item)


student_names = list(students.keys())
print("\nStudent Names List:", student_names)