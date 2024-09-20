# ==ESPRESSO AND BAGEL SHOP RECIEPT=======
# this program will create a receipt for a coffee shop, four items will be available 
# Author: Lucas Robles
# Created: 9/20/2024
#*********************************************************************

##variables================
coffeePrice = 2.00  #price of coffee
muffinPrice = 3.00  #price of muffins
bagelPrice = 5.00  #price of bagels
espressoPrice = 4.00  #price of espresso

#contants=================
SALES_TAX = 0.06    #sales tax of 6 % written in decimal form.

#PRINT INTRO and PROMPT=======================
#this will begin the program and print an introduction.
print("\n***************************************")
print("My Espresso and Bagel Shop")

#user input for amount of coffee bought
coffeeBought = input("Number of coffees bought?\n")
#user input for amount of muffins bought
muffinBought = input("Number of muffins bought?\n")
#user input for amount of bagels bought
bagelBought = input("Number of bagels bought?\n")
#user input for amount of espresso bought
espressoBought = input("Number of espresso bought?\n")

#CALCULATIONS=================================
#multiplies items bought by the price
#converted inputs into floats for decimal point
coffeeTotal = float(coffeeBought) * coffeePrice
muffinTotal = float(muffinBought) * muffinPrice
bagelTotal = float(bagelBought) * bagelPrice
espressoTotal = float(espressoBought) * espressoPrice

preTaxTotal = coffeeTotal + muffinTotal + bagelTotal + espressoTotal   #pre-tax total
salesTaxTotal = preTaxTotal * SALES_TAX   #finding tax
taxTotal = preTaxTotal + salesTaxTotal    #total after tax

#printing the reciept and showing the total====
print("***************************************\n\n")
print("***************************************")
print("My Espresso and Bagel Shop Receipt")
print(coffeeBought, "Coffee at $2 each: $", f"{coffeeTotal:.2f}")  #using f string to format, limiting to two spaces after the decimal
print(muffinBought, "Muffins at $3 each: $", f"{muffinTotal:.2f}")
print(bagelBought, "Bagels at $5 each: $", f"{bagelTotal:.2f}")
print(espressoBought, "Espresso at $4 each: $", f"{espressoTotal:.2f}")
print("6% tax: $ " + f"{salesTaxTotal:.2f}" [1:])  #tax is formatted to two decimal places and slices string from second character 
print("---------")
print("Total: $", taxTotal)
print("***************************************")

#exit message and thank you :]
print("\nThanks for coming by!! Come again anytime 24/7 :]\n")
