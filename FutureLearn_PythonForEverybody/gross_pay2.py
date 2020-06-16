#!/usr/bin/env python3

h = float(input("Enter hours: "))

sh = float(40)

r = float(input("Enter current rates per hours: "))

if h > sh:
    xtra_hrs = h - sh 
    xtra_rates = float(r + (r / 2))


Total_Pay = str(sh * r + xtra_hrs * xtra_rates)
print(Total_Pay)

