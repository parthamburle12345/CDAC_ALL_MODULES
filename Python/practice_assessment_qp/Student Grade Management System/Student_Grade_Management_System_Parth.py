"""
STUDENT GRADE & ASSESSMENT MODULE
(JSON File Persistence & Modular Analytics)
"""

import json

students = [
    {"id": 1, "name": "Aarav Sharma", "course": "Python Core", "marks": 88.5, "grade": "A"},
    {"id": 2, "name": "Diya Patel",   "course": "Data Science", "marks": 74.0, "grade": "B"}
]
counter = len(students)
#========================================================================================
def calculate_grade(marks):
    if marks >= 85:
        return 'A'
    elif marks >=70:
        return 'B'
    elif marks >=50:
        return 'C'
    else:
        return 'F'
#========================================================================================
def menu():
    print("\n*** STUDENT GRADE MANAGEMENT SYSTEM ***")
    print("=======================================")

    print("[1] Enroll Student  \n  [2] Cohort Directory  \n  [3] Query Records  \n  [4] Revise Evaluation  \n  [5] Purge Record  \n  [6] Save to JSON  \n  [7] Load from JSON  \n  [8] Terminate")

    try:
        choice = int(input("Enter your choice:"))
        if choice < 1 or choice >8:
            choice -1
    except ValueError:
        print("enter a valid choice.")
        choice -1
    return choice
#========================================================================================
def enroll_student():
    global counter 

    try:
        name = input("Enter name:").title().strip()

        if name == "":
            print("name cannot be empty.")
            return

        course = input("Enter course name:").title().strip()
        if course == "":
            print("course cannot be empty.")
            return

        marks = float(input("Enter Marks:"))
        if marks < 0.0 or marks >=100.0:
            print("marks should be between 0.0 ≤ marks ≤ 100.0.")
            return
        
        grade = calculate_grade(marks)

        counter +=1

        students.append({"id": counter, "name": name, "course": course, "marks": marks, "grade": grade})

    except ValueError:
        print("Invalid numerical value. Please try again.")
#========================================================================================
def print_one_student(s):
    print("----------------------------------------")
    print(f"ID       : {s['id']}")
    print(f"Name     : {s['name']}")
    print(f"Course   : {s['course']}")
    print(f"Marks    : {s['marks']:.2f}")
    print(f"Grade    : {s['grade']}")
    print("----------------------------------------")
#========================================================================================
def print_many_students(student_list):         #revise
    print("-" * 85)

    print(                            
        f"{'ID':^5}"
        f"{'Name':<22}"
        f"{'Course':<22}"
        f"{'Marks':>10}"
        f"{'Grade':>8}"
    )

    print("-" * 85)

    for s in student_list:
        print(
            f"{s['id']:^5}"
            f"{s['name']:<22}"
            f"{s['course']:<22}"
            f"{s['marks']:>10.2f}"
            f"{s['grade']:>8}"
        )

    print("-" * 85)
#=================================================================
def cohort_directory():
    if len(students) == 0:
        print("no student found.")

    if len(students) == 1:
        print_one_student(students[0])
    else:
        print_many_students(students)
#=================================================================
def search_by_id(student_id):
    result=[]
    for s in students:
        if s["id"] == student_id:
            result.append(s)

    if not result:
        print(f"No student found with id {student_id}.")
        return None

    print_one_student(result[0])
    return result[0]
#==============================================================================
def search_by_name_or_course(search_term):
    
    result=[]

    for s in students:
        if (search_term.lower() in s["name"].lower() or search_term.lower() in s["course"].lower()):
            result.append(s)
           
        if not result():
            print("no matching record found.")
            return None

        if len(result) == 1:
            print_one_student(result[0])
        else:
            print_many_students(result)

        return result
#==============================================================================
def query_record():
    print("1.seacrh by ID.")
    print("2.search by name/course:")

    try:
        choice = int(input("enter choice 1/2:"))

        if choice == 1:
            student_id = int(input("enter ID:"))
            search_by_id(student_id)

        elif choice == 2:
            search_term = input("enter course name to be search:").strip()

            if search_term == "":
                print("course cannot be empty.")
                return
            
            search_by_name_or_course(search_term)

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid value. Please try again.")
#==============================================================================
def purge_record():
    try:
        student_id = int(input("enter a student id to be deleted:"))
        student = search_by_id(student_id)

        if student is None:
            return

        answer = input("are you sure you wanna delete recode?(y/n)")
        if answer == 'y':
            students.remove(student)
            print("student record is deleted successfully!!")
        else:
            print("delete operation is cancelled.")
        

    except ValueError:
        print("invalid student id . retry")
#=================================================================
def save_to_json():
    try:
        with open("students.json", "w") as file:
            json.dump(students,file, indent=4)
        print("Records saved to students.json successfully.")
    except Exception:
        print("error while saving records.")
#=================================================================
def load_from_file():
    global students 
    global counter

    try:
        with open("students.json", "r") as file:
            new_students = json.load(file)

        students = new_students

        if len(students) > 0:
            max_id = students[0]["id"]

            for s in students:
                if s["id"] > max_id:
                    max_id = s["id"]

            counter = max_id
        else:
            counter = 0

        print("Records loaded from students.json successfully.")

    except FileNotFoundError:
        print("students.json file not found.")

    except json.JSONDecodeError:
        print("Invalid data found in students.json.")

    except Exception:
        print("Error while loading records.")        
#========   =========================================================
def revise_evaluation():        #Update/change a student's marks or evaluation.
    try:
        student_id = int(input("Enter student id to update: "))

        student = search_by_id(student_id)

        if student is None:
            return

        # --- Name ---
        name_input = input(f"Enter new name ({student['name']}): ").strip()

        if name_input == "":
            name = student["name"]
        else:
            name = name_input

        # --- Course ---
        course_input = input(f"Enter new course ({student['course']}): ").strip()

        if course_input == "":
            course = student["course"]
        else:
            course = course_input

        # --- Marks ---
        marks_input = input(f"Enter new marks ({student['marks']}): ").strip()

        if marks_input == "":
            marks = student["marks"]
            grade = student["grade"]

        else:
            try:
                marks = float(marks_input)

                if marks < 0.0 or marks > 100.0:
                    print("Invalid marks. Marks remain unchanged.")
                    marks = student["marks"]
                    grade = student["grade"]
                else:
                    grade = calculate_grade(marks)

            except ValueError:
                print("Invalid marks. Marks remain unchanged.")
                marks = student["marks"]
                grade = student["grade"]

        student["name"] = name
        student["course"] = course
        student["marks"] = marks
        student["grade"] = grade

        print("Student record updated successfully.")
    except ValueError:
        print("invalid student id.please enter an integer.")
#=================================================================
def main():
    while True:

        choice = menu()

        match choice:

            case 1:
                enroll_student()

            case 2:
                cohort_directory()

            case 3:
                query_record()

            case 4:
                revise_evaluation()

            case 5:
                purge_record()

            case 6:
                save_to_json()

            case 7:
                load_from_file()

            case 8:
                print("Terminating program...")
                break

            case _:
                print("Invalid choice. Please retry.")
#=================================================================

if __name__ == "__main__":
    main()