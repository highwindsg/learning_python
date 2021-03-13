#!/usr/bin/env python3

import urllib.request, urllib.parse, urllib.error
import json


# Google API key may be needed for authentication.
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI"    

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break
    
    url = serviceurl + urllib.parse.urlencode({"address": address})
    
    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")
    
    try:
        js = json.loads(data)
        
    except:
        js = None
        
    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)
    location = js["results"][0]["formatted_address"]
    print(location)
    print("")
    
    
    """
    Self homework. Search google or youtube on how to use the API key in line 8.
    My Google API key is: key=AIzaSyC6qM8BkM3geu1Dunt_P1JMpsHTgUfc_Z0
    """
    