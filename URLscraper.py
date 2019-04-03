#!/usr/bin/env python3

"""
Install the BeautifulSoup module so as to parse website's HTML
format using a programming language to give it structure.
eg. $ sudo pip install beautifulsoup4==4.4.1.
"""

#import urllib.request   # Import request from urllib.
from bs4 import BeautifulSoup   # Import BeautifulSoup from bs4.
import urllib.request   # Import request from urllib.

class Scraper:  # Create a class named Scraper.
    def __init__(self, site):   # Define a init start function with param self and site.
        self.site = site        # From self get the attribute of site and assign to site.

    # The Scraper class has a method called 'scrape' you will call whenever you want to
    # scrape data from the site you passed in.
    def scrape(self):   # Define a scrape function with param self.
        """ The urlopen() function makes a request to a website and returns a
        Response obj 'r' that has its HTML stored in it, along with other data.
        """
        r = urllib.request.urlopen(self.site)   # The urlopen() method opens the website
                                                # from param site in self, and assigns
                                                # to var 'r'.
        """ The function response.read() 'r.read()' then returns the HTML from
        the Response obj 'r' and assigns to var 'html'.
        """
        html = r.read()
        """ Create a BeautifulSoup obj and pass in the 'html' var and the string
        'html.parser' (because you are parsing HTML) as params.
        """
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        """ Note that the find_all() method is not the same as the findall() in regex.
        The scrape() function calls the 'find_all' method on the BeautifulSoup obj
        'sp'. Then pass in a "a" param (which tells the function to look for <a></a>
        tags) and the method will return all the URLs the website links to in the HTML
        you choose to download from.
        """
        # Each time around the 'for loop', the var tag is assigned the value of a new obj.
        for tag in sp.find_all("a"):
            # We only want the 'href' instance var which contains each URL and we use
            # the .get method and pass in 'href' as a param, and assign to var 'url'.
            url = tag.get("href")
            # If the 'url' var contains nothing, then 'continue' next round.
            if url is None:
                continue
            # And if the string 'html' is found in var 'url', we print it.
            if "html" in url:
                print("\n" + url)


# Assign the Google News URL to the var 'news'.
news = "https://news.google.com/"
# Call the Scraper class the assign the 'news' var as a param to it,
# and then get the scrape() function on it.
Scraper(news).scrape()

