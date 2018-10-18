#!/usr/bin/python
"""Takes HTML file and extracts data using Beautiful Soup
"""
from bs4 import BeautifulSoup

def extract(fil):
    """Takes file and extracts data with beautiful soup

    Args:
        fil: an opened HTML file

    Returns:
        extracted: a list table data as strings
    """

    extracted = []
    soup = BeautifulSoup(fil, "lxml")

    for data in soup.find_all('td'):
        newdata = data.text.encode('utf-8').strip()
        extracted.append(newdata)

    return extracted
