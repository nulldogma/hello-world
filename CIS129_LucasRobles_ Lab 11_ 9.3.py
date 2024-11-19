#Module 11 Lab-11
#CIS 129 Programming and Problem Solving I
#Lucas Robles
#November 18th, 2024
#//////////////////////////////////////////////////////////
"""
Excercise 9.3
Writing Student Records to a CSV File
-------------------------- 
This program will allow the user to enter each student’s first name and last name as strings 
and the student’s three exam grades as integers. This program will use the csv module to 
write each record into the grades.csv file. Each record is formatted in a single line of text 
in the following CSV format:

    firstname,lastname,exam1grade,exam2grade,exam3grade
"""
#//////////////////////////////////////////////////////////

import csv

def get_valid_input(prompt, input_type,  SENTINEL):
    """a function to validate user input based on the specified type (string or integer)"""
    while True: 
        try: 
            if input_type == int:
                value = int(input(prompt)) 
                if value < 0 and value != int(SENTINEL):    #handling input if a negative number is entered
                    print("Invalid Entry, please type in a non-negative number.") 
                else: 
                    return value     
            else: 
                value = input(prompt) 
                return value 
        except ValueError: 
            print(f"Invalid Entry, please enter a valid {input_type.__name__}.")

def write_CSV(file, student_data):
    """a function to write a CSV grade file using student data."""
    writer = csv.writer(file) 
    writer.writerow(student_data)

def get_data(SENTINEL):
    """a function to ask for user to input data"""
    first_name = get_valid_input("Enter student's first name: ", str, SENTINEL) 
    last_name = get_valid_input("Enter student's last name: ", str, SENTINEL) 
    exam1_grade = get_valid_input('Exam 1 grade: ', int, SENTINEL) 
    exam2_grade = get_valid_input('Exam 2 grade: ', int, SENTINEL) 
    exam3_grade = get_valid_input('Exam 3 grade: ', int, SENTINEL) 
    student_data = [first_name, last_name, exam1_grade, exam2_grade, exam3_grade]   #a list to hold student data inputs
    return student_data

def main():
    # Declare Constants
    SENTINEL = 'no'

    # Begin program loop, SENTINEL to exit program loop
    file_grade = 'grades.csv'
    with open(file_grade, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['firstname', 'lastname', 'exam1grade', 'exam2grade', 'exam3grade'])  # Write header

        while True:
            student_data = get_data(SENTINEL)
            write_CSV(file, student_data)
            repeat_input = input("Do you want to input another student's information? (Type 'no' to EXIT): ").strip().lower()
            if repeat_input.lower() == SENTINEL:    #lower case any input for this question
                print("Goodbye!")
                break

main()

