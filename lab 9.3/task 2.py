"""Student Management System for SRU.

This module provides a class to manage student information including
personal details, hostel status, and fee payment tracking. It includes
an interactive interface for creating and managing student records.
"""


class sru_student:
    """A class representing a student at SRU.
    
    This class manages student information including name, roll number,
    hostel accommodation status, and fee payment status.
    
    Attributes
    ----------
    name : str
        The name of the student.
    roll_no : str or int
        The roll number of the student.
    hostel_status : str
        The hostel accommodation status of the student.
    fee_paid : bool
        Indicates whether the student's fee has been paid.
    """
    
    def __init__(self, name, roll_no, hostel_status):
        """Initialize a new SRU student.
        
        Parameters
        ----------
        name : str
            The name of the student.
        roll_no : str or int
            The roll number of the student.
        hostel_status : str
            The hostel accommodation status of the student.
        """
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        # Initialize fee status as unpaid by default
        self.fee_paid = False
    
    def fee_update(self, status):
        """Update the fee payment status of the student.
        
        Parameters
        ----------
        status : bool
            True if fee has been paid, False otherwise.
        """
        self.fee_paid = status
    
    def display_details(self):
        """Display all student details.
        
        Prints the student's name, roll number, hostel status,
        and fee payment status to the console.
        """
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Hostel Status:", self.hostel_status)
        print("Fee Paid:", "Yes" if self.fee_paid else "No")

# Main execution - First student
print("=== First Student ===")
# Get student information from user
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
hostel_status = input("Hostel status (Yes/No): ")

# Create student object
student = sru_student(name, roll_no, hostel_status)

# Get fee payment status and update
fee_status = input("Has the fee been paid? (Yes/No): ")
student.fee_update(fee_status.lower() == "yes")

# Display student details
student.display_details()

# Main execution - Second student
print("\n=== Second Student ===")
# Get student information from user
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
hostel_status = input("Hostel status (Yes/No): ")

# Create student object
student = sru_student(name, roll_no, hostel_status)

# Get fee payment status and update
fee_status = input("Has the fee been paid? (Yes/No): ")
student.fee_update(fee_status.lower() == "yes")

# Display student details
student.display_details()