# ==COFFEE AND MUFFIN SHOP RECIEPT=======
# this program will create a receipt for a coffee shop
# Author: Lucas Robles
# Created: 9/17/2024
#*********************************************************************

##variables================
coffeePrice = 5.00  #price of coffee
muffinPrice = 4.00  #price of muffins

#contants=================
SALES_TAX = 0.06    #sales tax of 6 % written in decimal form.

#PRINT INTRO and PROMPT=======================
#this will begin the program and print an introduction.
print("\n***************************************")
print("My Coffee and Muffin Shop")

#user input for amount of coffee bought
coffeeBought = input("Number of coffees bought?\n")
#user input for amount of muffins bought
muffinsBought = input("Number of muffins bought?\n")

#CALCULATIONS=================================
#multiplies items bought by the price
#converted inputs into floats for decimal point
coffeeTotal = float(coffeeBought) * coffeePrice
muffinTotal = float(muffinsBought) * muffinPrice

preTaxTotal = coffeeTotal + muffinTotal   #pre-tax total
salesTaxTotal = preTaxTotal * SALES_TAX   #finding tax
taxTotal = preTaxTotal + salesTaxTotal    #total after tax

#printing the reciept and showing the total====
print("***************************************\n\n")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(coffeeBought, "Coffee at $5 each: $", f"{coffeeTotal:.2f}")  #using f string to format, limiting to two spaces after the decimal
print(muffinsBought, "Muffins at $4 each: $", f"{muffinTotal:.2f}")
print("6% tax: $ " + f"{salesTaxTotal:.2f}" [1:])  #tax is formatted to two decimal places and slices string from second character 
print("---------")
print("Total: $", taxTotal)
print("***************************************")
