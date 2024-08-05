from student_operations import StudentOperations
from professor_operations import ProfessorOperations


def main():
    db_path = 'Project Files/university.db'
    student_ops = StudentOperations(db_path)
    professor_ops = ProfessorOperations(db_path)
    
    main_action = int(
        input('Choose an action: \n    1: Insert Data \n    2: Delete Data \n    3: Update Data \n    4: Exit\n'))
    
    if main_action == 1:
        insert_option = int(input('Choose an option: \n    1: Insert Student \n    2: Insert Professor\n'))
        if insert_option == 1:
            student_id = input("Enter the student ID: ")
            first_name = input("Enter the first name of the student: ")
            middle_name = input("Enter the middle name of the student (if any): ")
            last_name = input("Enter the last name of the student: ")
            gpa = float(input("Enter the GPA of the student: "))
            email = input("Enter the email address of the student: ")
            student_ops.insert_student(student_id, first_name, middle_name, last_name, gpa, email)
        elif insert_option == 2:
            employee_id = input("Enter the employee ID of the professor: ")
            first_name = input("Enter the first name of the professor: ")
            last_name = input("Enter the last name of the professor: ")
            email = input("Enter the email address of the professor: ")
            professor_ops.insert_professor(employee_id, first_name, last_name, email)
    
    elif main_action == 2:
        delete_option = int(input('Choose an option:  \n    1: Delete Student  \n    2: Delete Professor\n'))
        if delete_option == 1:
            student_id = input("Enter the student ID to delete: ")
            student_ops.delete_student(student_id)
        elif delete_option == 2:
            employee_id = input("Enter the employee ID to delete: ")
            professor_ops.delete_professor(employee_id)
    
    elif main_action == 3:
        edit_option = int(input('Choose an option: \n    1: Edit Student \n    2: Edit Professor\n'))
        if edit_option == 1:
            student_id = input("Enter the student ID to edit: ")
            first_name = input("Enter the new first name of the student (leave blank to keep current): ") or None
            middle_name = input("Enter the new middle name of the student (leave blank to keep current): ") or None
            last_name = input("Enter the new last name of the student (leave blank to keep current): ") or None
            gpa = input("Enter the new GPA of the student (leave blank to keep current): ")
            gpa = float(gpa) if gpa else None
            email = input("Enter the new email address of the student (leave blank to keep current): ") or None
            student_ops.edit_student(student_id, first_name, middle_name, last_name, gpa, email)
        elif edit_option == 2:
            employee_id = input("Enter the employee ID to edit: ")
            first_name = input("Enter the new first name of the professor (leave blank to keep current): ") or None
            last_name = input("Enter the new last name of the professor (leave blank to keep current): ") or None
            email = input("Enter the new email address of the professor (leave blank to keep current): ") or None
            professor_ops.update_professor(employee_id, first_name, last_name, email)
    
    elif main_action == 4:
        exit()


if __name__ == "__main__":
    main()
