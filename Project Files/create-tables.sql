-- create a table Student
CREATE TABLE IF NOT EXISTS Student(
    StudentId INTEGER PRIMARY KEY, -- unique, not null value used to uniquely identify a row in this table
    FirstName TEXT NOT NULL, -- do not allow NULL values when inserting into this column
    MiddleName TEXT,
    LastName TEXT NOT NULL,
    Gpa REAL NOT NULL, -- floating point, decimal number
    Email TEXT NOT NULL UNIQUE
);

-- create a table Professor(EmployeeId, FirstName, LastName, Email)
CREATE TABLE IF NOT EXISTS Professor(
    EmployeeId INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE
);
