#Module 11 Lab-11
#CIS 129 Programming and Problem Solving I
#Lucas Robles
#November 18th, 2024
#//////////////////////////////////////////////////////////
"""
Excercise 9.1 and 9.2
Write/Read Plain Text File
-------------------------- 
This program will ask user to input a number, making sure
that the input is a positive number, and then writes the valid 
grade values to a grades.txt file. 
This program includes a function that reads a grades.txt file, calculates 
the total, count, and average, and then displays the grade values with 
calculations using values from the file.
"""
#//////////////////////////////////////////////////////////

def get_new_grade(message, SENTINEL, LOW_VALUE):
    """a function to validate user input (receive string message holding user input from main)"""
    
    while True:
        try:
            new_grade = float(input(message))  #read user input
            if new_grade < LOW_VALUE and new_grade != SENTINEL:
                print("Invalid Entry, please type in a positive number.")
            else:
                return new_grade  #valid input, exit loop
        except ValueError:
            print("Invalid Entry, please type in a positive number.")  #this will handle invalid input

def write_grades():
    """a function to ask for user input, store the variable in an empty tuples, and write
     valid grades to a new grades.txt file. """
    
    #declare constants
    SENTINEL = -99
    LOW_VALUE = 0
    
    #declare variables
    message = f"Type in a grade and hit enter. Type in {SENTINEL} to quit.\n"   #user input
    grades = []     #creating an empty list to hold values

    #priming read and function call
    new_grade = get_new_grade(message, SENTINEL, LOW_VALUE)  #priming read

    #start the main program loop, SENTINEL is used to exit program
    while new_grade != SENTINEL:
        grades.append(new_grade)
        new_grade = get_new_grade(message, SENTINEL, LOW_VALUE)

    #writes grades to a new grades.txt file
    with open('grades.txt', mode='w') as file:
        for grade in grades:
            file.write(f"{grade}\n")


def read_grades():
    """a function to read a grades.txt file, displays the grade values from the file,
    then this function calculates the values' total(sum), count, and average and displays
    those results as well."""

    #declare variables
    grades = []     #an empty list is created
    
    #read grades from the file
    with open ('grades.txt', mode='r') as file:
        for line in file:                       #this iterates over each line in the file (individual grades)
            grades.append(float(line.strip()))  #this will modify and strip any leading/tailing whitespace, converts string to float, and appends to grades list

    #display each grade
    print("Grades:")
    for grade in grades:
        print(grade)

    #calculations for total, count, and average
    total = sum(grades)
    count = len(grades)
    average = total / count if count != 0 else 0    #returns 0 if division by Zero(0) is attempted

    #display calculation results
    print()                                                 #empty line
    print(f'{"Total:":<8} {"Count:":<8}{"Average":<8}')     #Title Header
    print(f'{total:<9.2f}{count:<8}{average:<8.2f}')           #formatting average values to show two decimal points

def main():
    #call functions
    write_grades()
    read_grades()

main()
