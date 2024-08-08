# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Harpreet Bassi , 8/5/2024 ,Created Initial Script for Assignment 06
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError:
    print(f"Error: {FILE_NAME} not found. A new file will be created when you save data.")
except json.JSONDecodeError:
    print("Error: The file format is incorrect. Please ensure it is in JSON format.")
except Exception as e:
    print("Error: There was a problem with reading the file.")
    print("-- Technical Error Message --")
    print(e.__doc__)
    print(e.__str__())
finally:
    if file and not file.closed:
        file.close()

# Define the Functions
def output_error_messages(message: str, error: Exception = None):
    """Handles error messages"""
    print(f"ERROR: {message}")
    if error:
        print(f"DETAILS: {error}")

def output_menu(menu: str):
    """Displays a menu to the user"""
    print(menu)

def input_menu_choice():
    """Gets the menu choice from the user"""
    return input("What would you like to do: ")

def input_student_data(student_data: list):
    """Gets student data from the user"""
    try:
        first_name = input("Enter the student's first name: ")
        if not first_name:
            raise ValueError("First name cannot be empty.")
        last_name = input("Enter the student's last name: ")
        if not last_name:
            raise ValueError("Last name cannot be empty.")
        course_name = input("Enter the course name: ")
        if not course_name:
            raise ValueError("Course name cannot be empty.")
        student_data.append({"FirstName": first_name, "LastName": last_name, "CourseName": course_name})
    except ValueError as e:
        output_error_messages("Invalid input.", e)
    print(f"You have now registered {first_name} {last_name} for {course_name}.")

def output_student_courses(student_data: list):
    """Displays the current student course registrations"""
    print("The following students are now registered:")
    print("-" * 50)
    for student in student_data:
        print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
    print("-" * 50)

def read_data_from_file(file_name: str, student_data: list):
    """Reads data from a file into a list of dictionary rows"""
    try:
        with open(file_name, 'r') as file:
            student_data.clear()
            student_data.extend(json.load(file))
    except FileNotFoundError as e:
        output_error_messages("File not found error. Please make sure the file exists.", e)
    except json.JSONDecodeError as e:
        output_error_messages("Error decoding JSON from file.", e)
    except Exception as e:
        output_error_messages("An error occurred while reading the file.", e)

def write_data_to_file(file_name: str, student_data: list):
    """Writes data from a list of dictionary rows to a file"""
    try:
        print(f"Writing the following data to {file_name}...")
        with open(file_name, 'w') as file:
            json.dump(student_data, file, indent=4)
    except Exception as e:
        output_error_messages("An error occurred while writing to the file.", e)

# Present and Process the data
print("Opening the program...")  # Debugging statement
while True:
    output_menu(MENU)
    menu_choice = input_menu_choice()
    print(f"User selected: {menu_choice}")  # Debugging statement

    if menu_choice == "1":
        input_student_data(students)
    elif menu_choice == "2":
        output_student_courses(students)
    elif menu_choice == "3":
        write_data_to_file(FILE_NAME, students)
        output_student_courses(students)
    elif menu_choice == "4":
        print("Exiting the program... Goodbye.")
        break
    else:
        output_error_messages("Invalid menu choice, please try again.")

print("Program Ended")
