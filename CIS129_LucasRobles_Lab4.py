#Module 4 Lab-4
#Lucas Robles
#September 25th, 2024
#Created for CIS 129 Programming and Problem Solving I

#///////////////////////////////////////////////////////////////////
#/This program will calculate a retails company's store bonus      /
#/depending on the monthly sales. This will also calculate employee/
#/bonuses by using a percent of sales increase.                    /
#///////////////////////////////////////////////////////////////////
#MAIN function=======================
def main():
    #declare local variables
    monthlySales = 0 #monthly sales amount
    storeAmount = 0 #store bonus amount
    empAmount = 0  #employee bonus amount
    salesIncrease = 0 #percent of sales increase

    #call functions and ...
    #assigning return values to variables
    monthlySales = getSales()   #assigning return values to variables
    salesIncrease = getIncrease()
    storeAmount = calcStoreBonus(monthlySales)
    empAmount = calcEmpBonus(salesIncrease)
    printBonus(storeAmount, empAmount)  #call to print

 #this function gets the monthly sales============
def getSales():
    monthlySales = float(input('Enter the monthly sales:'))
    return monthlySales

#this function gets the percent of increase in sales================
def getIncrease():
    salesIncrease = float(input('Enter percent of sales increase: '))
    salesIncrease = salesIncrease / 100
    return salesIncrease

#this function calculates the store bonus based on monthly sales====
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

#this function determines the employee bonus amount============
def calcEmpBonus(salesIncrease):
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

#this function prints the bonus information============
def printBonus(storeAmount, empAmount):
    print('The store bonus amount is $', storeAmount)
    print('The employee bonus amount is $', empAmount)
    if (storeAmount == 6000) and (empAmount == 75):
        print("Congrats! You have reached the highest bonus amounts possible! ")

#call MAIN funtion
main()
