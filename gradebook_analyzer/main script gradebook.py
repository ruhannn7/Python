import statistics
# ----------------------------------------------------------------------
# Name : Ruhan Dogra
# Date : 5 November 2025
# Title : GradeBook Analyzer
# ----------------------------------------------------------------------

def display_menu():
    print("\n--- Menu ---")
    print("1. Start Grade Analysis.")
    print("2. Exit.")
    print("--------------")

def student_data():
    marks_dict = {}
    
    while True:
        try:
            num_students = int(input("\nEnter the total number of students in the class: "))
            if num_students > 0:
                break
            else:
                print(" Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"\n----Entering data for {num_students} student(s)----")

    for i in range(num_students):
        print(f"\n Student {i+1}")
        name = input("Enter Student Name: ").strip().title()
        
        while True:
            try:
                # Used f-string for name in prompt and int() for marks
                marks = int(input(f"Enter Marks For {name} (0-100): ")) 
                if 0 <= marks <= 100:
                    break
                else:
                    print("Marks Must Be Between 0 and 100.")
            except ValueError:
                print("Invalid Input. Please Enter a whole number.")

        marks_dict[name] = marks 
    
    print("\n Data Entry Complete.")
    return marks_dict

def calc(marks_dict):
    if not marks_dict:
        print("\nNo student data available to analyze.")
        return
    
    marks_list = list(marks_dict.values())
    
    avg = sum(marks_list) / len(marks_list)
    median = statistics.median(marks_list)
    max_score= max(marks_list)
    min_score = min(marks_list)

#display
    print("\n---- Statistical Analysis ----")
    print(f"Total Students : {len(marks_dict)}")     
    print(f"Average Score : {avg:.2f}")
    print(f"Median Score : {median:.2f}")
    print(f"Highest Score : {max_score}")
    print(f"Lowest Score : {min_score}")
    print("----------------------------------")

    grades_dict = {}
    grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

    for name, mark in marks_dict.items():
        if mark >= 90:
            grade = 'A'
        elif mark >= 80:
            grade = 'B'
        elif mark >= 70:
            grade = 'C'
        elif mark >= 60:
            grade = 'D'
        else: # Mark < 60
            grade = 'F'

        grades_dict[name] = grade
        grade_counts[grade] += 1

    # Grade Distribution Display
    print("\n---- Grade Distribution Summary ----")
    for grade in ['A', 'B', 'C', 'D', 'F']:
        count = grade_counts.get(grade, 0)
        print(f"Grade {grade}: {count} student(s)")
    print("--------------------------------------")

    # --- Task 5: Pass/Fail Filter with List Comprehension ---
    passed_stu = [name for name , m in marks_dict.items() if m >= 40]
    failed_stu = [name for name , m in marks_dict.items() if m < 40]

    # Pass/Fail Display
    print("\n---- Pass/Fail Analysis ----")
    # Corrected 'none' to 'None' for proper case
    print(f"Passed Students ({len(passed_stu)}): {', '.join(passed_stu) if passed_stu else 'None'} ")
    print(f"Failed Students ({len(failed_stu)}): {', '.join(failed_stu) if failed_stu else 'None'} ")
    print("----------------------------------")

    # --- Task 6: Results Table ---
    print("\n===================================")
    print("|          FINAL RESULTS          |")
    print("===================================")

    print(f"{'Name':<15}{'Marks':<10}{'Grade':<5}")
    print("-"*30)

    for name,marks in marks_dict.items():
        grade = grades_dict.get(name, 'N/A')
        print(f"{name:<15}{marks:<10}{grade:<5}")

    print("=======================================")


if __name__ == "__main__":
    print("*"*50)
    print("     Welcome to the Python GradeBook Analyzer   ")
    print("*"*50)

    while True:
        display_menu()
        choice = input("Enter Your Choice: ").strip()

        if choice =='1':
            marks = student_data()
            calc(marks)
            print("\nAnalysis Complete. Returning to main menu.")

        elif choice =='2':
            print("Thank You for using the GradeBook Analyzer. Goodbye!")
            break
        else:
            print("\nInvalid Choice. Please enter 1 or 2.")
