from database import DatabaseConnection


class StudentOperations:
    def __init__(self, db_path):
        self.db_path = db_path
    
    def insert_student(self, student_id, first_name, middle_name, last_name, gpa, email):
        query = """
        INSERT INTO Student (StudentId, FirstName, MiddleName, LastName, Gpa, Email)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        db = DatabaseConnection(self.db_path)
        cursor = db.connect()
        cursor.execute(query, (student_id, first_name, middle_name, last_name, gpa, email))
        db.disconnect()
        print("Student inserted successfully.")
    
    def delete_student(self, student_id):
        query = "DELETE FROM Student WHERE StudentId = ?"
        db = DatabaseConnection(self.db_path)
        cursor = db.connect()
        cursor.execute(query, (student_id,))
        db.disconnect()
        print("Student deleted successfully.")
    
    def edit_student(self, student_id, first_name=None, middle_name=None, last_name=None, gpa=None, email=None):
        query = """
        UPDATE Student
        SET FirstName = COALESCE(?, FirstName),
            MiddleName = COALESCE(?, MiddleName),
            LastName = COALESCE(?, LastName),
            Gpa = COALESCE(?, Gpa),
            Email = COALESCE(?, Email)
        WHERE StudentId = ?
        """
        db = DatabaseConnection(self.db_path)
        cursor = db.connect()
        cursor.execute(query, (first_name, middle_name, last_name, gpa, email, student_id))
        db.disconnect()
        print("Student updated successfully.")
