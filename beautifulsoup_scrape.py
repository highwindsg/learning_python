#!/usr/bin/env python3

"""
Install the BeautifulSoup module so as to parse website's HTML
format using a programming language to give it structure.
eg. $ sudo pip install beautifulsoup4==4.4.1.
"""

import urllib.request   # Import request from urllib.
from bs4 import BeautifulSoup   # Import BeautifulSoup from bs4.

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
        """ Note that the find_all() method is not the same as in findall() in regex.
        The scrape() functions calls the 'find_all' method on the BeautifulSoup obj
        'sp'. Then pass in a "a" param (which tells the function to look for <a></a>
        tags) and the method will return all the URLs the website links to in the HTML
        you choose to download from.
        """
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)


