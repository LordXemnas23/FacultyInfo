#!/usr/bin/python
"""Reads in an HTML file and writes a csv file
"""
import urllib
import csv

def read(url):
    """Reads in a url with urllib

    Args:
        url: a url in a string

    Returns:
        fil.read(): a list of html code read line by line
    """

    fil = urllib.urlopen(url)
    return fil.read()

def write(info):
    """Creates a csv file and enters data into a table

    Args:
        info: a list of data extracted from an html page
    """

    with open("Info.csv", "wb") as output:
        wrt = csv.writer(output)
        wrt.writerow(("Name", "Department", "Email", "Phone"))

        for row in range(0, len(info), 4):
            wrt.writerow(info[row:row + 4])
