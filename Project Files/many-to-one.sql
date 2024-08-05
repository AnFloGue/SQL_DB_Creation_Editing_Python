-- turn on support for foreign keys in SQLite
PRAGMA foreign_keys = ON;

-- many-to-one: a course is taught by one professor but a professor may teach many courses
CREATE TABLE Course(
    CourseId INTEGER PRIMARY KEY,
    Department TEXT NOT NULL,
    CourseNumber INTEGER NOT NULL,
    CourseName TEXT NOT NULL,
    EmployeeId INTEGER,
    FOREIGN KEY (EmployeeId) REFERENCES Professor(EmployeeId) -- create the foreign key constraint
);
