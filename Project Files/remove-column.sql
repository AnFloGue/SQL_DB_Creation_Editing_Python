-- remove MiddleName from Student table

-- inside of the transaction, either ALL of the SQL runs successfully, 
-- or our database rolls back to before the transaction
BEGIN TRANSACTION;

-- 1. Rename our table to a temp name
ALTER TABLE Student RENAME TO Student_Temp;

-- 2. Create a new table with the column removed
CREATE TABLE Student(
    StudentId INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Gpa REAL NOT NULL,
    Email TEXT NOT NULL UNIQUE
);

-- 3. Copy data from the old, temp table into the new table
INSERT INTO Student
    SELECT StudentId, FirstName, LastName, Gpa, Email
    FROM Student_Temp;

-- 4. Get rid of the old, temp table
DROP TABLE Student_Temp;

COMMIT;
