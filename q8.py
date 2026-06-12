# # Q8. Perform the following List operations: (2 Marks) 
# • Create a list of 5 student names • Add 2 more names using append() and insert()
#  • Remove a name using remove() and delete by index using pop() 
#  • Sort the list alphabetically and print it in reverse order 
#  • Slice the list to print only the first 3 elements

students = ["Rahul", "Priya", "Rohan", "Sneha", "Amit"]

students.append("Neha")      # append()
students.insert(2, "Karan")  # insert()

print("After adding names:", students)


students.remove("Amit")

students.pop(3)

print("After removing names:", students)

students.sort()
print("Sorted List:", students)


students.reverse()
print("Reverse Order:", students)


print("First 3 Elements:", students[:3])