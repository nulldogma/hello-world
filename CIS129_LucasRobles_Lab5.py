#Module 5 Lab-5
#CIS 129 Programming and Problem Solving I
#Lucas Robles
#October 1st, 2024
#//////////////////////////////////////////////////////////
#/  THE BOTTLE RETURN PROGRAM                             /
#/--------------------------                              /
#/This program will calculate the amount paid out         /
#/for bottle returns at the cost of $0.10. The amount     /
#/paid and the total of bottles returned will be displayed/
#//////////////////////////////////////////////////////////

#MAIN function======================================================================
def main():
    #declaring the local variables below using snake_case
    total_bottles = 0   #the accumulated amount of bottles
    total_payout = 0    #store calculated value of bottles times 0.10, the cost of the bottles
    keep_going = 'y'    #variable used to run the program again

    #&&&&&&&&&&&&&&&&&&&&&&&&&&
    #begin the while loop to run program again
    while keep_going == 'y':
        #call functions and assign values to main function variables.
        total_bottles = get_bottles()               #calculate the accumulation of bottles
        total_payout = calc_payout(total_bottles)   #calculate the money paid out @ $0.10 per bottle
        print_info(total_bottles, total_payout)     #display the results of calculations

        #user input will decide if the loop will run again
        print("\nDo you want to enter another week's worth of data?")
        keep_going = input("(Enter y or n): ")
        print('\n')     #a blank line will be added after the user selects y or n
    #&&&&&&&&&&&&&&&&&&&&&&&&&&

#====================================
#   FUNCTIONS
#====================================
#________________________________________________
#get calculations for number of bottles accumulated
def get_bottles():
    NUM_OF_DAYS = 7     #constant used to store the number of days in the week
    #declare variables
    total_bottles = 0    #variable will store the input of bottles returned, 
    today_bottles = 0    #variable will store the accumulated amount of bottles returned
    counter = 0          #variable will control when the while loop below ends

    #&&&&&&&&&&&&&&&&&&&&&&&&&&
    #the while loop will continue to ask the user's input for bottles returned each day,
    #it will display the counter, showing the amount of days
    while counter < NUM_OF_DAYS:
        #counter will be increased by 1 for every loop until it has reached 7
        counter += 1
        ##storing bottles returned on each day
        today_bottles = int(input(f'Enter number of bottles returned for day #{counter}: '))
        total_bottles += today_bottles  #adding the input to the total returned
    return total_bottles
    #&&&&&&&&&&&&&&&&&&&&&&&&&&

#__________________________________________________
#function calculates the amount of money paid out 
#depending on the total bottles returned
def calc_payout(total_bottles):  
    PAYOUT_PER_BOTTLE = 0.10                         #the cost of a bottle at $0.10
    total_payout = 0                                 #this will reset to zero(0) for multiple runs
    total_payout = PAYOUT_PER_BOTTLE * total_bottles #multiply the cost of a bottle by the amount of bottles
    return total_payout

#__________________________________________________
#function will display the results from the above calculations
def print_info(total_bottles, total_payout):
    print(f"\nThe total number of bottles collected is: {total_bottles}")   #f string used to insert the value of the variable during runtime
    print(f"The total paid out is: $ {total_payout:.1f}")                   #the total payout is formatted to display only the tenths place after the decimal

#call MAIN function
main()
#==================================================================================