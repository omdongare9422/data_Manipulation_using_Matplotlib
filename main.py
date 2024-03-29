import file_operation
import visual_representation

while True:
    print("\nMenu:")
    print("1. Add Data")
    print("2. View All Data")
    print("3. Update Data")
    print("4. View Particular Record (by roll no)")
    print("5. Visual Data Display")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        file_operation.add()
    elif choice == "2":
        file_operation.view_all_data()
    elif choice == "3":
        file_operation.update_data()
    elif choice == "4":
        file_operation.view_data()
    elif choice == "5":
        visual_representation.visual_data_display()
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
