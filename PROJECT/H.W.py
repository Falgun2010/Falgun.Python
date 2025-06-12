# # Python Program to Accept Subject Names and Marks, Then Calculate and Display Grade

# # Input: Subject names and marks
# subjects = []
# marks = []

# print("Enter details for 3 subjects:")
# for i in range(3):
#     subject = input(f"Enter name of subject {i+1}: ")
#     mark = float(input(f"Enter marks for {subject}: "))
#     subjects.append(subject)
#     marks.append(mark)

# # Calculate total and average
# total_marks = sum(marks)
# average_marks = total_marks / 3

# # Determine grade based on average
# if average_marks >= 90:
#     grade = 'A'
# elif average_marks >= 75:
#     grade = 'B'
# elif average_marks >= 60:
#     grade = 'C'
# elif average_marks >= 40:
#     grade = 'D'
# else:
#     grade = 'F'

# # Print result
# print("\n------ Result ------")
# for i in range(3):
#     print(f"{subjects[i]}: {marks[i]} marks")
# print(f"Total Marks: {total_marks}")
# print(f"Average Marks: {average_marks:.2f}")
# print(f"Grade: {grade}")