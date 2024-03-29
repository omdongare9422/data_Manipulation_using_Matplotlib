def add():
    try:
        with open("std.txt", "a") as f:
            roll = input("Enter the Roll no: ")
            marks = input("Enter the marks of the student: ")
            f.write(roll + "," + marks + "\n")
        print("Data Added Successfully....!")
    except IOError:
        print("Error: Unable to write to the file!")

def view_all_data():
    try:
        with open("std.txt", "r") as f:
            data = f.readlines()
            if len(data) == 0:
                print("NO Data In the file")
            else:
                print("Student data:\nRoll\tMarks")
                for line in data:
                    roll, marks = line.strip().split(",")
                    print(roll + "\t" + marks)
    except FileNotFoundError:
        print("File not found...!")

def view_data():
    try:
        with open("std.txt", "r") as f:
            r = input("Enter the roll number of the student to get data: ")
            data = f.readlines()
            if len(data) == 0:
                print("NO Data In the file")
            else:
                print("Student data:")
                for line in data:
                    roll, marks = line.strip().split(",")
                    if r == roll:
                        print("Roll:", roll, "\nMarks:", marks)
    except FileNotFoundError:
        print("File not found...!")

def update_data():
    roll_to_update = input("Enter the roll number of the student to update: ")
    new_marks = input("Enter the updated marks: ")
    updated = False
    try:
        with open("std.txt", "r") as file:
            lines = file.readlines()
        with open("std.txt", "w") as file:
            for line in lines:
                roll, marks = line.strip().split(",")
                if roll == roll_to_update:
                    file.write(roll + "," + new_marks + "\n")
                    updated = True
                else:
                    file.write(line)
        if updated:
            print("Data updated successfully.")
        else:
            print("No record found for the provided roll number.")
    except FileNotFoundError:
        print("File not found.")
