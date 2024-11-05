# Programmer: Hershey Marbeda
# Last Date Modified: 11.05.2024
# Program: Case Study: If...Else and While loops
# Program Purpose: To determine if a student qualifies for the Dean's List or the Honor Roll.

# Main Prompt
print("\nWelcome to the Student Qualification Program!")

while True:
    student_last_name = input("\nPlease enter the student's Last Name (type 'exit' to end the program): ")

    if student_last_name == "ZZZ" or student_last_name == "zzz":
       print("\nYou have entered ZZZ. Exiting the program.")
       exit()
    elif student_last_name == "exit" or student_last_name == "Exit" or student_last_name == "EXIT":
       print("\nYou have entered Exit. Exiting the program.")
       exit()
    
    student_first_name = input("Please enter the student's First Name: ")

    student_GPA = float(input("Please enter the student's GPA: "))

    # To Determine the Student's Qualification for the Dean's List
    if student_GPA >= 3.5:
        print(f"\n{student_first_name} {student_last_name} has made the Dean's List!")
    elif student_GPA >= 3.25:
        print(f"\n{student_first_name} {student_last_name} has made the Honor Roll!")
    elif student_GPA < 3.25:
        print(f"\n{student_first_name} {student_last_name} has not qualified for the Dean's List or the Honor Roll.\n")