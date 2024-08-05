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


your_options = int(input('Choose an option: 1: "Insert Student", 2: "Insert Professor", 3: "Exit"'))
if your_options == 1:
    # Example usage for inserting a student
    student_id = input("Enter the student ID: ")
    first_name = input("Enter the first name of the student: ")
    middle_name = input("Enter the middle name of the student (if any): ")
    last_name = input("Enter the last name of the student: ")
    gpa = float(input("Enter the GPA of the student: "))
    email = input("Enter the email address of the student: ")
    insert_student(student_id, first_name, middle_name, last_name, gpa, email)

elif your_options == 2:
    # Example usage for inserting a professor
    employee_id = input("Enter the employee ID of the professor: ")
    first_name = input("Enter the first name of the professor: ")
    last_name = input("Enter the last name of the professor: ")
    email = input("Enter the email address of the professor: ")
    insert_professor(employee_id, first_name, last_name, email)
elif your_options == 3:
    exit()
