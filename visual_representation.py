import matplotlib.pyplot as plt

def visual_data_display():
    while True:
        print("\nVisual Data Display:")
        print("1. Bar Graph")
        print("2. Histogram")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            plot_bargraph()
        elif choice == "2":
            plot_histogram()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def plot_bargraph():
    try:
        with open("std.txt","r") as f:
            data=f.readlines()
            rolls=[]
            marks=[]
            for line in data:
                roll_no, mark = line.strip().split(",")
                rolls.append(int(roll_no))
                marks.append(int(mark)) 

            plt.figure(figsize=(10, 6))  
            plt.bar(rolls, marks, color='blue')
            plt.xlabel('Roll Number')
            plt.ylabel('Marks')
            plt.title('Bar Graph of Student Marks')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
    except FileNotFoundError:
        print("File not found.")  

def plot_histogram():
    try:
        with open("std.txt", "r") as f:
            data = f.readlines()
            marks = []
            for line in data:
                mark = int(line.strip().split(",")[1])
                marks.append(mark)

            plt.hist(marks, bins=10, alpha=0.5, color='blue', edgecolor='black')
            plt.xlabel('Marks')
            plt.ylabel('NUmber of students')
            plt.title('Histogram of Marks')
            plt.grid(True)
            plt.show()
    except FileNotFoundError:
        print("File not found.")
