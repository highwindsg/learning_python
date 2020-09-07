#!/usr/bin/env python3

# For items in mydict that has more than 3 characters in the key,
# add up their total values.

total = 0
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}

for akey in mydict:
    if len(akey) > 3:
        total = total + mydict[akey]

print(total)
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
