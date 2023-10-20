#Plot a stacked bar chart of matches won of all teams over all the years of IPL.
import csv
import sys
import matplotlib.pyplot as plt
from main import matches_reader

def matches_won_overyears():
    
    matches_won={}        # will be organized as : team --> year --> no. of matches won that year
    min = sys.maxsize
    max = -(sys.maxsize)-1
    
    for row in matches_reader:    #traverse matches_reader
        
        winner = row['winner']
        if winner not in matches_won:
            matches_won[winner]={}
            
        year = row['season']
        if int(year) < min: min=int(year)
        if int(year) > max: max=int(year)
        if year not in matches_won[winner]:
            matches_won[winner][year]=0
        matches_won[winner][year]+=1
  
  
    final_result={}   # will be organized as : team --> no. of matches won over IPL years

    for team in matches_won:
        for i in range(min,max+1):      #traverse over the years
            year = str(i)
            
            if team not in final_result:   #if team not present in final then add it to final and initialize it as list
                final_result[team]=[]
            
            if year not in matches_won[team]: #if a team not won any match in a particulary year then for that year append the team list(in final) with 0
                final_result[team].append(0)
            else:                       # else append with number of matches won by that team
                final_result[team].append(matches_won[team][year])
    
    return final_result
