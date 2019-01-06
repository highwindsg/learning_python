#!/usr/bin/env python3

# Calculate the cost of purchasing some number of small and large widgets.
# Small widgets cost five dollars each, large widgets cost eight dollars each.
# Tax rate is nine percent.

TAX_RATE = .09      # 9% tax rate
COST_PER_SMALL_WIDGETS = 5.00
COST_PER_LARGE_WIDGETS = 8.00

def calculateCost(nSmallWidgets, nLargeWidgets):
    subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGETS) + (nLargeWidgets * COST_PER_LARGE_WIDGETS)
    taxAmount = subTotal * TAX_RATE
    totalCost = subTotal + taxAmount
    return totalCost

def calculateTax(nSmallWidgets, nLargeWidgets):
    subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGETS) + (nLargeWidgets * COST_PER_LARGE_WIDGETS)
    taxAmount = subTotal * TAX_RATE
    return taxAmount

total1 = calculateCost(4, 8)    # 4 small and 8 large widgets
print("Total cost with tax for the first order is", total1)
print("Tax amount only for first order is", calculateTax(4, 8))
print("")
total2 = calculateCost(12, 5)   # 12 small and 5 large widgets
print("Total cost with tax for the second order is", total2)
print("Tax amount only for second order is", calculateTax(12, 5))
