#!/usr/bin/env python3

# Write a program to calculate the shipping costs.
# When called, it is expected to be passed two pieces of data:
# the country to ship to, and the number of widgets purchased.
# The function will return a resulting shipping costs.

NOT_YET = "We do not ship there yet."

# Function to determine shipping cost, based on country and quantity.
def calculateShipping(country, nWidgets):
    if (country == "US") or (country == "United States"):
        if nWidgets <= 50:
            Cost = 6.25
        elif nWidgets <= 100:
            Cost = 9.50
        elif nWidgets <= 150:
            Cost = 12.75
        else:
            Cost = 15.00

    elif (country == "CA") or (country == "Canada"):
        if nWidgets <= 50:
            Cost = 8.25
        elif nWidgets <= 100:
            Cost = 12.50
        elif nWidgets <= 150:
            Cost = 18.75
        else:
            Cost = 25.00

    else:
        shippingCost = NOT_YET

    return Cost

#def printCusReq(CountryLoc, QtyReq):
#    if calculateShipping(CountryLoc, QtyReq):
#        print("OK! You need", QtyReq, "widgets for shipment to", CountryLoc)
#    else:
#        print("Please try again.")

# Ask user to enter the quantity of widgets and country of shipment.
CountryLoc = input("Enter the country of shipment:  ")
QtyReq = int(input("Enter the quantity of widgets required: "))
#printCusReq(CountryLoc, QtyReq)

# Call the function to see how much it will cost to ship.
AmtforShipping = calculateShipping(CountryLoc, QtyReq)
if AmtforShipping == NOT_YET:
    print("Sorry, we do not ship to", CountryLoc)
else:
    print("It will cost $", AmtforShipping, "to ship your package.")




