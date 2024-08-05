import sqlite3


def check_student_table_schema():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('Project Files/university.db')
        cursor = conn.cursor()
        
        # Query to check the schema of the Student table
        cursor.execute("PRAGMA table_info(Student)")
        student_columns = cursor.fetchall()
        
        print("Current schema of Student table:")
        for column in student_columns:
            print(column)
        
        # Query to check the schema of the Professor table
        cursor.execute("PRAGMA table_info(Professor)")
        professor_columns = cursor.fetchall()
        
        print("\nCurrent schema of Professor table:")
        for column in professor_columns:
            print(column)
    
    except sqlite3.Error as error:
        print("Error while checking table schema: ", error)
    
    finally:
        # Close the database connection
        if conn:
            conn.close()


# Check the schema of the Student and Professor tables
check_student_table_schema()


def drop_and_create_tables():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('Project Files/university.db')
        cursor = conn.cursor()
        
        # Drop the existing Student table if it exists
        cursor.execute("DROP TABLE IF EXISTS Student")
        
        # Drop the existing Professor table if it exists
        cursor.execute("DROP TABLE IF EXISTS Professor")
        
        # Create the Student table with the correct schema
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Student(
            StudentId INTEGER PRIMARY KEY,
            FirstName TEXT NOT NULL,
            MiddleName TEXT,
            LastName TEXT NOT NULL,
            Gpa REAL NOT NULL,
            Email TEXT NOT NULL UNIQUE
        )
        """)
        
        # Create the Professor table with the correct schema
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Professor(
            EmployeeId INTEGER PRIMARY KEY,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            Email TEXT NOT NULL UNIQUE
        )
        """)
        
        # Commit the transaction
        conn.commit()
        
        print("Student and Professor tables created successfully.")
    
    except sqlite3.Error as error:
        print("Error while creating tables: ", error)
    
    finally:
        
        # Close the database connection
        if conn:
            conn.close()


# Drop and recreate the Student and Professor tables
drop_and_create_tables()
