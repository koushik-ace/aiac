"""
--------------------------------------------------------------
PROJECT: Employee Salary Analyzer (AI-Assisted Data Processing)
--------------------------------------------------------------

This script:

1. Reads employees.csv containing:
        Name,Department,Salary

2. Validates rows using AI-inspired rules:
        - Name and Department not empty
        - Salary must be numeric

3. Finds the employee with the highest salary per department.

4. Includes UNIT TESTS inside the same file (unittest).

Run Program:
    python employee_analyzer.py

Run Tests:
    python employee_analyzer.py test

--------------------------------------------------------------
"""

import csv
import sys
import unittest
from collections import defaultdict


# --------------------------------------------------------------
# AI VALIDATION LOGIC
# --------------------------------------------------------------
def ai_validate_row(row):
    """Validate row using simple AI-inspired rules."""
    if not row["Name"].strip():
        return False
    if not row["Department"].strip():
        return False

    try:
        float(row["Salary"])
    except ValueError:
        return False

    return True


# --------------------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------------------
def find_highest_salary_per_department(filename):
    """
    Reads CSV and returns top earner per department.
    Format:
        { "IT": ("Riya", 70000), ... }
    """

    department_max = defaultdict(lambda: ("", 0))

    with open(filename, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not ai_validate_row(row):
                continue

            name = row["Name"]
            dept = row["Department"]
            salary = float(row["Salary"])

            if salary > department_max[dept][1]:
                department_max[dept] = (name, salary)

    return department_max


# --------------------------------------------------------------
# PRINT RESULTS
# --------------------------------------------------------------
def print_results(results):
    print("\nHighest Salary in Each Department")
    print("---------------------------------")
    for dept, (name, sal) in results.items():
        print(f"{dept}: {name} (₹{sal})")


# --------------------------------------------------------------
# UNIT TESTS 
# --------------------------------------------------------------
class TestEmployeeAnalyzer(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_employees.csv"

    def tearDown(self):
        import os
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_highest_salary_basic(self):
        with open(self.test_file, "w") as f:
            f.write("Name,Department,Salary\n")
            f.write("Karan,IT,50000\n")
            f.write("Riya,IT,70000\n")
            f.write("Amit,HR,45000\n")
            f.write("Sneha,HR,47000\n")
            f.write("Lokesh,Finance,80000\n")

        result = find_highest_salary_per_department(self.test_file)
        print("TEST 1 →", result)

        self.assertEqual(result["IT"], ("Riya", 70000))
        self.assertEqual(result["HR"], ("Sneha", 47000))
        self.assertEqual(result["Finance"], ("Lokesh", 80000))

    def test_invalid_rows(self):
        with open(self.test_file, "w") as f:
            f.write("Name,Department,Salary\n")
            f.write(" ,IT,50000\n")
            f.write("Riya,IT,70000\n")

        result = find_highest_salary_per_department(self.test_file)
        print("TEST 2 →", result)

        self.assertEqual(result["IT"], ("Riya", 70000))

    def test_salary_not_numeric(self):
        with open(self.test_file, "w") as f:
            f.write("Name,Department,Salary\n")
            f.write("Karan,IT,abc\n")
            f.write("Riya,IT,70000\n")

        result = find_highest_salary_per_department(self.test_file)
        print("TEST 3 →", result)

        self.assertEqual(result["IT"], ("Riya", 70000))

    def test_multiple_departments(self):
        with open(self.test_file, "w") as f:
            f.write("Name,Department,Salary\n")
            f.write("A,Dept1,10000\n")
            f.write("B,Dept2,20000\n")
            f.write("C,Dept3,30000\n")

        result = find_highest_salary_per_department(self.test_file)
        print("TEST 4 →", result)

        self.assertEqual(result["Dept1"], ("A", 10000))
        self.assertEqual(result["Dept2"], ("B", 20000))
        self.assertEqual(result["Dept3"], ("C", 30000))

    def test_duplicate_salaries(self):
        with open(self.test_file, "w") as f:
            f.write("Name,Department,Salary\n")
            f.write("A,IT,50000\n")
            f.write("B,IT,50000\n")

        result = find_highest_salary_per_department(self.test_file)
        print("TEST 5 →", result)

        self.assertIn(result["IT"], [("A", 50000.0), ("B", 50000.0)])

    def test_empty_csv(self):
        with open(self.test_file, "w") as f:
            f.write("Name,Department,Salary\n")

        result = find_highest_salary_per_department(self.test_file)
        print("TEST 6 →", result)

        self.assertEqual(result, {})





# --------------------------------------------------------------
# ENTRY POINT
# --------------------------------------------------------------
if __name__ == "__main__":

    # If run like:
    #   python employee_analyzer.py test
    # then run unit tests
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        unittest.main(argv=['first-arg-is-ignored'], exit=False)

    else:
        # Normal execution
        filename = "employees.csv"
        results = find_highest_salary_per_department(filename)
        print_results(results)
