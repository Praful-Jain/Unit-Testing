# For the year 2015 plot the top economical bowlers.
import csv
import matplotlib.pyplot as plt
from main import deliveries_reader


def top_economical_bowlers():
    
    # Dictionary to store number of bowls bowled by a bowler
    bowls={}
    # Dictionary to store number of runs took by opponent
    runs={}
    
    for row in deliveries_reader :
        if int(row['match_id']) >= 518 and int(row['match_id']) <=576 :
            if(row['wide_runs'] == '0' and row['noball_runs'] == '0') :
                bowls[row['bowler']] = bowls.get(row['bowler'] , 0) + 1
            runs[row['bowler']]  = runs.get(row['bowler'] , 0) + int(row['total_runs'])     
                  
    overs={}
    for player in bowls :
        overs[player] = bowls[player]/6 
        
    # Dictionary to store economy of each bowler
    economy = {}
    for player in runs :
        economy[player] = round(runs[player]/overs[player] , 2)
    
    # Sorting in ascending order
    economy = dict(sorted( economy.items() ,key = lambda x : x[1]))
    
    # Identifying top 10 bowlers based on their economy
    top10_bowler={}
    count=0
    for bowler in economy :
        top10_bowler[bowler] = economy[bowler]
        count += 1
        if(count==10) :
            break

    return top10_bowler
    