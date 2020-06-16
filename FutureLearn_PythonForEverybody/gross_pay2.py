#!/usr/bin/env python3

try:
    h = float(input("Enter hours: "))   # h for hours worked.

    sh = float(40)  # sh for standard flat hours worked.

    r = float(input("Enter current rates per hours: "))     # r for rates.

    if h > sh:
        xtra_hrs = h - sh   # xtra_hrs for additional hours worked.
        xtra_rates = float(r + (r / 2))     # xtra_rates for additional rates.

except ValueError:
    print("Non-numeric input detected, please try again.")
    quit()  # use quit() to stop the program.

Total_Pay = str(sh * r + xtra_hrs * xtra_rates)
print(Total_Pay)

