CREATE DATABASE PROJECT3;
USE PROJECT3;

-- #departments table 
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

INSERT INTO Departments (DepartmentID, DepartmentName) VALUES 
(1, 'Computer Science'),
(2, 'Mathematics');



-- #students table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    BirthDate DATE,
    EnrollmentDate DATE
);

INSERT INTO Students (StudentID, FirstName, LastName, Email, BirthDate, EnrollmentDate) VALUES 
(1, 'John', 'Doe', 'john.doe@email.com', '2000-01-15', '2022-08-01'),
(2, 'Jane', 'Smith', 'jane.smith@email.com', '1999-05-25', '2021-08-01');

-- #instructor table
CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

INSERT INTO Instructors (InstructorID, FirstName, LastName, Email, DepartmentID) VALUES 
(1, 'Alice', 'Johnson', 'alice.johnson@univ.com', 1),
(2, 'Bob', 'Lee', 'bob.lee@univ.com', 2);

-- #courses table
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    DepartmentID INT,
    Credits INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

INSERT INTO Courses (CourseID, CourseName, DepartmentID, Credits) VALUES 
(101, 'Introduction to SQL', 1, 3),
(102, 'Data Structures', 2, 4);


-- #enrollments table 
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID, EnrollmentDate) VALUES 
(1, 1, 101, '2022-08-01'),
(2, 2, 102, '2021-08-01');

-- #queries

-- 1)CRUD OPERATIONS
INSERT INTO Students (StudentID, FirstName, LastName, Email, BirthDate, EnrollmentDate) 
VALUES (3, 'Robert', 'Brown', 'robert.b@email.com', '2002-06-10', '2023-09-01');

-- View all students
SELECT * FROM Students;

-- View specific student by ID
SELECT * FROM Students WHERE StudentID = 1;

UPDATE Students 
SET Email = 'john.newemail@email.com' 
WHERE StudentID = 1;

DELETE FROM Students 
WHERE StudentID = 3;

-- 2) RETRIVE STUDENTS WHO ENROLLED AFTER 2022
SELECT * FROM Students 
WHERE EnrollmentDate > '2022-12-31';

-- 3)RETRIVE COURSES OFFERED BY THE MATHEMATICS DEPARTMENTS(LIMIT5)
SELECT c.CourseName 
FROM Courses c
JOIN Departments d ON c.DepartmentID = d.DepartmentID
WHERE d.DepartmentName = 'Mathematics'
LIMIT 5;

-- 4)GET THE NUMBER OF THE STUDENTS ENROLLED IN EACH COURSE .
SELECT CourseID, COUNT(StudentID) AS StudentCount
FROM Enrollments
GROUP BY CourseID
HAVING COUNT(StudentID) > 5;

-- 5)FIND STUDENTS ENROLLED IN BOTH "INTRO TO SQL" & "DATA STRUCTURE"
SELECT s.FirstName, s.LastName
FROM Students s
JOIN Enrollments e1 ON s.StudentID = e1.StudentID
JOIN Courses c1 ON e1.CourseID = c1.CourseID
JOIN Enrollments e2 ON s.StudentID = e2.StudentID
JOIN Courses c2 ON e2.CourseID = c2.CourseID
WHERE c1.CourseName = 'Introduction to SQL' 
  AND c2.CourseName = 'Data Structures';

-- 6)FIND STUDENTS ENROLLED IN EITHER "INTRO TO SQL" & "DATA STRUCTURE"
SELECT DISTINCT s.FirstName, s.LastName
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
JOIN Courses c ON e.CourseID = c.CourseID
WHERE c.CourseName IN ('Introduction to SQL', 'Data Structures');

-- 7)CALCULATE THE AVERAGE NUMBER OF CREDITS OF ALL COURSES.
SELECT AVG(Credits) AS AverageCredits 
FROM Courses;

-- 8)FIND THE MAX SALARY OF INSTRUCTOR IN THE COMPUTER SCIENCE DEPARTMENT.
SELECT MAX(Salary) 
FROM Instructors i
JOIN Departments d ON i.DepartmentID = d.DepartmentID
WHERE d.DepartmentName = 'Computer Science';

-- 9)COUNT THE NUMBER OF STUDENTS ENROLLED IN  EACH DEPARTMNENTS
SELECT d.DepartmentName, COUNT(DISTINCT e.StudentID) AS TotalStudents
FROM Departments d
JOIN Courses c ON d.DepartmentID = c.DepartmentID
JOIN Enrollments e ON c.CourseID = e.CourseID
GROUP BY d.DepartmentName;

-- 10) INNER JOIN RETRIVE STUDENTS AND THEIR CORROSPONDING COURSES.
SELECT s.FirstName, s.LastName, c.CourseName
FROM Students s
INNER JOIN Enrollments e ON s.StudentID = e.StudentID
INNER JOIN Courses c ON e.CourseID = c.CourseID;

-- 11)) LEFT JOIN RETRIVE ALL  STUDENTS AND THEIR CORROSPONDING COURSES IF ANY.
SELECT s.FirstName, s.LastName, c.CourseName
FROM Students s
LEFT JOIN Enrollments e ON s.StudentID = e.StudentID
LEFT JOIN Courses c ON e.CourseID = c.CourseID;

-- 12)SUBQUERY FIND STUDENTS ENROLLED IN COURSES TAHT HAVE MORE THAN 10 STUDENTS.
SELECT DISTINCT FirstName, LastName
FROM Students
WHERE StudentID IN (
    SELECT StudentID 
    FROM Enrollments 
    WHERE CourseID IN (
        SELECT CourseID FROM Enrollments GROUP BY CourseID HAVING COUNT(StudentID) > 10
    )
);

-- 13) EXTRACT THE YEAR FROM THE ENROLLMENTS DATE OF STUDENTS.
SELECT FirstName, LastName, EXTRACT(YEAR FROM EnrollmentDate) AS EnrollmentYear 
FROM Students;

-- 14)CONCATENATE THE INSTRUCTORS FIRST AND LAST NAME.
SELECT CONCAT(FirstName, ' ', LastName) AS FullName FROM Instructors;

-- 15)CALCULATE THE RUNNING TOTAL OF STUDENTS ENROLLED IN COURSES.
SELECT EnrollmentDate, 
       COUNT(StudentID) OVER (ORDER BY EnrollmentDate) AS RunningTotal
FROM Enrollments;

-- 16)LABEL STUDENTS AS SENOIR OR JUNIOUR BASED ON ENROLLMENTS. 
SELECT FirstName, LastName,
CASE 
    WHEN EnrollmentDate <= CURRENT_DATE - INTERVAL '4 years' THEN 'Senior'
    ELSE 'Junior'
END AS StudentStatus
FROM Students;


