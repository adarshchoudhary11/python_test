# Q6. Create a Student Report System: (3 Marks)
# • Create 'report.txt' with 5 students
# and marks: Rahul-85, Priya-90, Rohan-78, Sneha-92, Amit-65
# • Read file and print only students with marks > 80
# • Handle FileNotFoundError with finally block.

try:
    
    with open("report.txt", "w") as file:
        file.write("Rahul-85\n")
        file.write("Priya-90\n")
        file.write("Rohan-78\n")
        file.write("Sneha-92\n")
        file.write("Amit-65\n")

    
    with open("report.txt", "r") as file:
        print("Students with marks > 80:")
        
        for line in file:
            name, marks = line.strip().split("-")
            marks = int(marks)

            if marks > 80:
                print(name, "-", marks)

except FileNotFoundError:
    print("File not found!")

finally:
    print("File operation completed.")