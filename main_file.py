#!/usr/bin/python
"""Reads and extracts data from html page and enters it into a csv file
"""
from extract.read_write import read
from extract.read_write import write
from extract._extract import extract

def main():
    """Executes functions to extract table data from a url and write it into another table with in a .csv file
    """
    url = "http://www.ecsu.edu/faculty-staff/profiles/index.html"

    opened = read(url)
    xtracted = extract(opened)
    write(xtracted)

if __name__ == '__main__':
    main()
