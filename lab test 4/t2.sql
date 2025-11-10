-- Insert Students
INSERT INTO Students (StudentID, FirstName, LastName, Email, DateOfBirth, EnrollmentDate)
VALUES
(1, 'Aarav', 'Mehta', 'aarav.mehta@example.com', '2003-05-10', '2022-08-01'),
(2, 'Diya', 'Sharma', 'diya.sharma@example.com', '2002-11-22', '2021-08-01'),
(3, 'Rohan', 'Patel', 'rohan.patel@example.com', '2004-01-15', '2023-08-01'),
(4, 'Neha', 'Gupta', 'neha.gupta@example.com', '2003-03-30', '2022-08-01'),
(5, 'Aditya', 'Verma', 'aditya.verma@example.com', '2002-09-05', '2021-08-01');

-- Insert Courses
INSERT INTO Courses (CourseID, CourseName, Credits, Instructor)
VALUES
(101, 'Database Systems', 3, 'Dr. Rakesh Nair'),
(102, 'Operating Systems', 4, 'Prof. Priya Menon'),
(103, 'Computer Networks', 3, 'Dr. S. Iyer');

-- Insert Attendance 
INSERT INTO Attendance (AttendanceID, StudentID, CourseID, AttendanceDate, Status)
VALUES
(1, 1, 101, '2025-11-01', 'Present'),
(2, 1, 101, '2025-11-02', 'Absent'),
(3, 1, 101, '2025-11-03', 'Present'),
(4, 2, 101, '2025-11-01', 'Absent'),
(5, 2, 101, '2025-11-02', 'Present'),
(6, 2, 101, '2025-11-03', 'Absent'),
(7, 3, 102, '2025-11-01', 'Present'),
(8, 3, 102, '2025-11-02', 'Present'),
(9, 3, 102, '2025-11-03', 'Present'),
(10, 4, 103, '2025-11-01', 'Absent'),
(11, 4, 103, '2025-11-02', 'Absent'),
(12, 4, 103, '2025-11-03', 'Present'),
(13, 5, 102, '2025-11-01', 'Present'),
(14, 5, 102, '2025-11-02', 'Absent'),
(15, 5, 102, '2025-11-03', 'Absent');
