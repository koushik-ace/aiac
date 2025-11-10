SELECT 
    s.FirstName,
    s.LastName,
    c.CourseName,
    ROUND(SUM(CASE WHEN a.Status = 'Present' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Attendance_Percentage
FROM 
    Attendance a
JOIN 
    Students s ON a.StudentID = s.StudentID
JOIN 
    Courses c ON a.CourseID = c.CourseID
GROUP BY 
    s.StudentID, c.CourseID
HAVING 
    ROUND(SUM(CASE WHEN a.Status = 'Present' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) < 75;
