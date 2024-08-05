-- turn on support for foreign keys in SQLite
PRAGMA foreign_keys = ON;

-- many-to-many: students can attend many courses and courses can be attended by many students
CREATE TABLE Attends(
    AttendsId INTEGER PRIMARY KEY,
    StudentId INTEGER,
    CourseId INTEGER,
    FOREIGN KEY (StudentId) REFERENCES Student(StudentId),
    FOREIGN KEY (CourseId) REFERENCES Course(CourseId)
);

