from database import DatabaseConnection

class ProfessorOperations:
    def __init__(self, db_path):
        self.db_path = db_path

    def insert_professor(self, employee_id, first_name, last_name, email):
        query = """
        INSERT INTO Professor (EmployeeId, FirstName, LastName, Email)
        VALUES (?, ?, ?, ?)
        """
        db = DatabaseConnection(self.db_path)
        cursor = db.connect()
        cursor.execute(query, (employee_id, first_name, last_name, email))
        db.disconnect()
        print("Professor inserted successfully.")

    def delete_professor(self, employee_id):
        query = "DELETE FROM Professor WHERE EmployeeId = ?"
        db = DatabaseConnection(self.db_path)
        cursor = db.connect()
        cursor.execute(query, (employee_id,))
        db.disconnect()
        print("Professor deleted successfully.")

    def update_professor(self, employee_id, first_name=None, last_name=None, email=None):
        query = """
        UPDATE Professor
        SET FirstName = COALESCE(?, FirstName),
            LastName = COALESCE(?, LastName),
            Email = COALESCE(?, Email)
        WHERE EmployeeId = ?
        """
        db = DatabaseConnection(self.db_path)
        cursor = db.connect()
        cursor.execute(query, (first_name, last_name, email, employee_id))
        db.disconnect()
        print("Professor updated successfully.")