import sqlite3


def insert_student(student_id, first_name, middle_name, last_name, gpa, email):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('Project Files/university.db')
        cursor = conn.cursor()
        
        # Create the INSERT INTO SQL query
        query = """
        INSERT INTO Student (StudentId, FirstName, MiddleName, LastName, Gpa, Email)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        
        # Execute the query with the provided data
        cursor.execute(query, (student_id, first_name, middle_name, last_name, gpa, email))
        
        # Commit the transaction
        conn.commit()
        
        print("Student inserted successfully.")
    
    except sqlite3.IntegrityError as error:
        print("Integrity error: ", error)
    except sqlite3.Error as error:
        print("Error while inserting student: ", error)
    
    finally:
        # Close the database connection
        if conn:
            conn.close()


def insert_professor(employee_id, first_name, last_name, email):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('Project Files/university.db')
        cursor = conn.cursor()
        
        # Create the INSERT INTO SQL query
        query = """
        INSERT INTO Professor (EmployeeId, FirstName, LastName, Email)
        VALUES (?, ?, ?, ?)
        """
        
        # Execute the query with the provided data
        cursor.execute(query, (employee_id, first_name, last_name, email))
        
        # Commit the transaction
        conn.commit()
        
        print("Professor inserted successfully.")
    
    except sqlite3.IntegrityError as error:
        print("Integrity error: ", error)
    except sqlite3.Error as error:
        print("Error while inserting professor: ", error)
    
    finally:
        # Close the database connection
        if conn:
            conn.close()


def delete_student(student_id):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('Project Files/university.db')
        cursor = conn.cursor()
        
        # Create the DELETE FROM SQL query
        query = "DELETE FROM Student WHERE StudentId = ?"
        
        # Execute the query with the provided data
        cursor.execute(query, (student_id,))
        
        # Commit the transaction
        conn.commit()
        
        print("Student deleted successfully.")
    
    except sqlite3.Error as error:
        print("Error while deleting student: ", error)
    
    finally:
        # Close the database connection
        if conn:
            conn.close()


def delete_professor(employee_id):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('Project Files/university.db')
        cursor = conn.cursor()
        
        # Create the DELETE FROM SQL query
        query = "DELETE FROM Professor WHERE EmployeeId = ?"
        
        # Execute the query with the provided data
        cursor.execute(query, (employee_id,))
        
        # Commit the transaction
        conn.commit()
        
        print("Professor deleted successfully.")
    
    except sqlite3.Error as error:
        print("Error while deleting professor: ", error)
    
    finally:
        # Close the database connection
        if conn:
            conn.close()

def edit_student(student_id, first_name=None, middle_name=None, last_name=None, gpa=None, email=None):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('Project Files/university.db')
        cursor = conn.cursor()

        # Create the UPDATE SQL query
        query = """
        UPDATE Student
        SET FirstName = COALESCE(?, FirstName),
            MiddleName = COALESCE(?, MiddleName),
            LastName = COALESCE(?, LastName),
            Gpa = COALESCE(?, Gpa),
            Email = COALESCE(?, Email)
        WHERE StudentId = ?
        """

        # Execute the query with the provided data
        cursor.execute(query, (first_name, middle_name, last_name, gpa, email, student_id))

        # Commit the transaction
        conn.commit()

        print("Student updated successfully.")

    except sqlite3.Error as error:
        print("Error while updating student: ", error)

    finally:
        # Close the database connection
        if conn:
            conn.close()


def edit_professor(employee_id, first_name=None, last_name=None, email=None):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('Project Files/university.db')
        cursor = conn.cursor()

        # Create the UPDATE SQL query
        query = """
        UPDATE Professor
        SET FirstName = COALESCE(?, FirstName),
            LastName = COALESCE(?, LastName),
            Email = COALESCE(?, Email)
        WHERE EmployeeId = ?
        """

        # Execute the query with the provided data
        cursor.execute(query, (first_name, last_name, email, employee_id))

        # Commit the transaction
        conn.commit()

        print("Professor updated successfully.")

    except sqlite3.Error as error:
        print("Error while updating professor: ", error)

    finally:
        # Close the database connection
        if conn:
            conn.close()

# First step: Choose the main action


# First step: Choose the main action
main_action = int(input(f'Choose an action: \n    1: Insert Data \n    2: Delete Data \n    3: Edit Data \n    4: Exit'))

if main_action == 1:
    # Second step: Choose the type of data to insert
    insert_option = int(input(f'Choose an option: \n    1: Insert Student \n    2: Insert Professor'))
    if insert_option == 1:
        # insert a student information
        student_id = input("Enter the student ID: ")
        first_name = input("Enter the first name of the student: ")
        middle_name = input("Enter the middle name of the student (if any): ")
        last_name = input("Enter the last name of the student: ")
        gpa = float(input("Enter the GPA of the student: "))
        email = input("Enter the email address of the student: ")
        insert_student(student_id, first_name, middle_name, last_name, gpa, email)
    elif insert_option == 2:
        # insert a professor information
        employee_id = input("Enter the employee ID of the professor: ")
        first_name = input("Enter the first name of the professor: ")
        last_name = input("Enter the last name of the professor: ")
        email = input("Enter the email address of the professor: ")
        insert_professor(employee_id, first_name, last_name, email)

elif main_action == 2:
    # Second step: Choose the type of data to delete
    delete_option = int(input(f'Choose an option:  \n    1: Delete Student  \n    2: Delete Professor'))
    if delete_option == 1:
        # delete a student information
        student_id = input("Enter the student ID to delete: ")
        delete_student(student_id)
    elif delete_option == 2:
        # delete a professor information
        employee_id = input("Enter the employee ID to delete: ")
        delete_professor(employee_id)

elif main_action == 3:
    # Second step: Choose the type of data to edit
    edit_option = int(input(f'Choose an option: \n    1: Edit Student \n    2: Edit Professor'))
    if edit_option == 1:
        # edit a student information
        student_id = input("Enter the student ID to edit: ")
        first_name = input("Enter the new first name of the student (leave blank to keep current): ") or None
        middle_name = input("Enter the new middle name of the student (leave blank to keep current): ") or None
        last_name = input("Enter the new last name of the student (leave blank to keep current): ") or None
        gpa = input("Enter the new GPA of the student (leave blank to keep current): ")
        gpa = float(gpa) if gpa else None
        email = input("Enter the new email address of the student (leave blank to keep current): ") or None
        edit_student(student_id, first_name, middle_name, last_name, gpa, email)
    elif edit_option == 2:
        # edit a professor information
        employee_id = input("Enter the employee ID to edit: ")
        first_name = input("Enter the new first name of the professor (leave blank to keep current): ") or None
        last_name = input("Enter the new last name of the professor (leave blank to keep current): ") or None
        email = input("Enter the new email address of the professor (leave blank to keep current): ") or None
        edit_professor(employee_id, first_name, last_name, email)

elif main_action == 4:
    exit()