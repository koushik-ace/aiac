class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

    def display_details(self):
        grade = self.calculate_grade()
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}, Grade: {grade}")

students = []
n = int(input("Enter number of students: "))
for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    name = input("Name: ")
    roll_no = input("Roll No: ")
    marks = float(input("Marks: "))
    s = Student(name, roll_no, marks)
    students.append(s)

print("\nStudent Details:")
for s in students:
    s.display_details()