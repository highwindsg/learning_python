#!/usr/bin/env python3

# For items in mydict that has more than 3 characters in the key,
# add up their total values.

total = 0
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}

# It adds the values of the keys that have length greater than 3.
# Therefore they are the sum of the numbers of elephant and bear.
for akey in mydict:
    if len(akey) > 3:
        total = total + mydict[akey]

print(total)
print("")



"""
The dictionary total_golds contains the total number of gold medals 
that countries have won over the course of history. Use dictionary 
mechanics to find the number of golds Chile has won, and assign that 
number to the variable name chile_golds. Do not hard code this!
"""

total_golds = {
    "Italy": 114, 
    "Germany": 782, 
    "Pakistan": 10, 
    "Sweden": 627, 
    "USA": 2681, 
    "Zimbabwe": 8, 
    "Greece": 111, 
    "Mongolia": 24, 
    "Brazil": 108, 
    "Croatia": 34, 
    "Algeria": 15, 
    "Switzerland": 323, 
    "Yugoslavia": 87, 
    "China": 526, 
    "Egypt": 26, 
    "Norway": 477, 
    "Spain": 133, 
    "Australia": 480, 
    "Slovakia": 29, 
    "Canada": 22, 
    "New Zealand": 100, 
    "Denmark": 180, 
    "Chile": 13, 
    "Argentina": 70, 
    "Thailand": 24, 
    "Cuba": 209, 
    "Uganda": 7,  
    "England": 806, 
    "Denmark": 180, 
    "Ukraine": 122, 
    "Bahamas": 12
    }

chile_golds = total_golds.get("Chile")
print(chile_golds)
print("")



"""
Using dictionary mechanics, assign the medal count value for 
"Belarus" to the variable belarus. Do not hardcode this.
"""

medal_count = {'United States': 70, 
               'Great Britain':38, 
               'China':45, 
               'Russia':30, 
               'Germany':17, 
               'Italy':22, 
               'France': 22, 
               'Japan':26, 
               'Australia':22, 
               'South Korea':14, 
               'Hungary':12, 
               'Netherlands':10, 
               'Spain':5, 
               'New Zealand':8, 
               'Canada':13, 
               'Kazakhstan':8, 
               'Colombia':4, 
               'Switzerland':5, 
               'Belgium':4, 
               'Thailand':4, 
               'Croatia':3, 
               'Iran':3, 
               'Jamaica':3, 
               'South Africa':7, 
               'Sweden':6, 
               'Denmark':7, 
               'North Korea':6, 
               'Kenya':4, 
               'Brazil':7, 
               'Belarus':4, 
               'Cuba':5, 
               'Poland':4, 
               'Romania':4, 
               'Slovenia':3, 
               'Argentina':2, 
               'Bahrain':2, 
               'Slovakia':2, 
               'Vietnam':2, 
               'Czech Republic':6, 
               'Uzbekistan':5
              }

belarus = medal_count.get("Belarus")
print(belarus)
print("")



"""
We have a dictionary of the specific events that Italy has won medals 
in and the number of medals they have won for each event. Assign to 
the variable 'events' a list of the keys from the dictionary 
'medal_events'. Do not hard code this.
"""

medal_events = {
    'Shooting': 7, 
    'Fencing': 4, 
    'Judo': 2, 
    'Swimming': 3, 
    'Diving': 2
    }

events = medal_events.keys()
print(events)
print("")



"""
Provided is a dictionary called US_medals which has the first 70 
metals that the United States has won in 2016, and in which category 
they have won it in. Using dictionary mechanics, assign the value of 
the key "Fencing" to a variable fencing_value. Remember, do not hard 
code this.
"""

US_medals = {
    "Swimming": 33, 
    "Gymnastics": 6, 
    "Track & Field": 6, 
    "Tennis": 3, 
    "Judo": 2, 
    "Rowing": 2, 
    "Shooting": 3, 
    "Cycling - Road": 1, 
    "Fencing": 4, 
    "Diving": 2, 
    "Archery": 2, 
    "Cycling - Track": 1, 
    "Equestrian": 2, 
    "Golf": 1, 
    "Weightlifting": 1
    }


fencing_value = US_medals.get("Fencing")
print(fencing_value)
print("")
