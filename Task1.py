# Plot the number of matches played per year of all the years in IPL.
import csv
import matplotlib.pyplot as plt
from main import matches_reader         # this matches_reader can be accessed by whole program

def matches_played_peryear():
    matches_played = {}
    for row in matches_reader:
        year = row['season']
        if year not in matches_played:
            matches_played[year] = 0
        matches_played[year] += 1

    return matches_played