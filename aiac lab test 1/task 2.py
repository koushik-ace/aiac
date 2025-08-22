class Student:
    def __init__(self):
        self.name = input("Enter student's name: ")
        self.roll_no = input("Enter student's roll number: ")
        try:
            self.marks = float(input("Enter student's marks: "))
        except ValueError:
            print("Invalid input for marks. Setting marks to 0.")
            self.marks = 0.0

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

# Example usage
student = Student()
student.display_details()
