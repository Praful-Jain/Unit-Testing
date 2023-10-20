# For the year 2016 plot the extra runs conceded per team.
import csv
import matplotlib.pyplot as plt
from main import matches_reader

def extra_runs_2016():
    extra_runs = {}

    for row in matches_reader :
        if(row['season'] == '2016') :
            extra_runs[row['winner']] =  extra_runs.get(row['winner'] , 0) + int(row['win_by_runs'])
     
    return extra_runs