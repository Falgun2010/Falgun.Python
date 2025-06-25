print("welcome to the student data organizer")
students = []
subjects_offered = set()

while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    choice = input("Enter your choice [1 to 6] : ")

    if choice == "1":
        print("\nEnter student details:")
        std_id = input("Enter Student ID : ")
        name = input("Enter Student Name : ")
        age = int(input("Enter Student Age : "))
        grade = input("Enter your Greade : ")
        dob = input("Enter DOB [ YYYY-MM-DD] : ")
        subjects = input("Enter Your Subject ( comma - separated ): ").split(",")

        id_dob = (std_id, dob) 
        student = {
            "id_dob": id_dob,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(student)
        subjects_offered.update(subjects)
        print("Student added successfully!!")

    elif choice == "2":
        if not students:
            print("No student records.")
        else:
            print("\n--- Display All Students ---")
            for i in students:
                s_id, dob = i["id_dob"]
                print(f"ID: {s_id} | Name: {i['name']} | Age: {i['age']} | Grade: {i['grade']} | Subjects: {', '.join(i['subjects'])}")

    elif choice == "3":
        s_id = input("Enter Student ID to update: ")
        found = False
        for i in students:
            if i["id_dob"][0] == s_id:
                i["age"] = int(input("Enter your new age: "))
                new_subjects = input("Enter your New subjects (comma-separated): ").split(",")
                i["subjects"] = [sub for sub in new_subjects]
                subjects_offered.update(i["subjects"])
                print("Student updated successfully!!.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        s_id = input("Enter Student ID to delete: ")
        for i in range(len(students)):
            if students[i]["id_dob"][0] == s_id:
                del students[i]
                print("Student deleted successfully!!.")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("\n--- Subjects Offered ---")
        
        print(subjects)

    elif choice == "6":
        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice. Try again.")