#Module 12 Lab-12
#CIS 129 Programming and Problem Solving I
#Lucas Robles
#November 25th, 2024
#//////////////////////////////////////////////////////////
"""
Pet Class Program
-------------------------- 
This program will ask user to enter the name of a pet, the
type of animal it is, and the age of the pet. The class Pet
will be used to create and retrieve the data to create an
object. The object will be used to access pet data and
display the output on the screen.
"""
#//////////////////////////////////////////////////////////

def main():
    """This will be the Main Function for the Pet Class Program."""
    # declaring input variables
    inputName = getValidInput("Enter a pet name:\n", str)     #storing valid inputs to the variables
    inputType = getValidInput("Enter a pet type:\n" , str)
    inputAge = getValidInput("Enter a pet age:\n", int)

    #creating a Pet class object
    Animal = Pet(inputName, inputType, inputAge)

    #stroring the values for the current pet
    print("The pet name is", Animal.getName())
    print("The pet type is", Animal.getType())
    print("The pet age is", Animal.getAge())

def getValidInput(prompt, inputType):
    """This function will validate the user input based on the specified type (str or int in this case)"""
    while True:
        try:
            if inputType == int:
                value = int(input(prompt))
                if value <= 0:
                    print("Invalid Entry, please type in a positive number.")
                else:
                    return value
            elif inputType == str:
                value = input(prompt).strip()
                if not value.isalpha():
                    print("Invalid Entry, please try again.")
                else:
                    return value.capitalize()      #this will capitalize the first letter of the string and return the sanitized string input
        except ValueError:
            print("Invalid Entry, please try again.")

class Pet:
    """A class for holding the name of a pet, the type of animal, and the age."""

    def __init__(self, name, type, age):
        """Contructor to initialize the pet attributes."""
        self.name = name
        self.type = type
        self.age = age

    #The following methods will be in class Pet
	# __________________________________________________________	empty line added for readability
	# Mutators
    def setName(self, name):
        """This method will store a value in the name field."""
        self.name = name

    def setType(self, type):
        """This method will store a value in the type field."""
        self.type = type

    def setAge(self, age):
        """This method will store a value in the age field."""
        self.age = age

    # __________________________________________________________	empty line added for readability
	# Accessors
    def getName(self):
        """This method will return the value of the name field."""
        return self.name
    
    def getType(self):
        """This method will return the value of the type field."""
        return self.type

    def getAge(self):
        """This method will return the value of the age field."""
        return self.age

main()