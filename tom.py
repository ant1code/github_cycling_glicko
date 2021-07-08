import itertools as it
import pandas as pd

out = pd.DataFrame({'riders':["R1","R2","R3","R4","R5","R6"],
                   'places':[1,5,4,2,3,6],
                   'elos':[1000, 1000, 1000, 1000, 1000, 1000]})

def computeELO(rider1, rider2):

    elo1 = 10 # how much the guz who won gained
    elo2 = 10 # loser lost pts, but positive

    return (elo1, elo2)

out = out.sort_values('places')

length = len(list(out['places']))
riders = list(out['riders'])
elos = list(out['elos'])

for i in range(length):
    if i == length:
        continue
    else:
        for j in range(i + 1, length, 1):
            newELO = computeELO(riders[i], riders[j])
            elos[i] += newELO[0]
            elos[j] -= newELO[1]

newDF = pd.DataFrame({'riders':riders,
                      'elos':elos})

newDF.to_csv('NEW_ELO.csv')
