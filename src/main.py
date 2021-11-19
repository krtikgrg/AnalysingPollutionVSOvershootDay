import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("../data/EST.csv")
year = data['Year']
tot = data['Total']
gas = data['Gas']
liquid = data['Liquids']
solid = data['Solids']

pollution = []
bracket = []
GAS = []
LIQUID = []
SOLID = []
for i in range(0,len(year),20):
    ctr = 0
    summ = 0
    sumg = 0
    suml = 0
    sums = 0
    curbra = str(year[i])+" - "
    for j in range(i,min(i+10,len(year))):
        summ += tot[j]
        ctr += 1
        sumg += gas[j]
        suml += liquid[j]
        sums += solid[j]
    curbra = curbra + str(year[j-1])
    pollution.append(summ/ctr)
    GAS.append(sumg/ctr)
    LIQUID.append(suml/ctr)
    SOLID.append(sums/ctr)
    bracket.append(curbra)

print(pollution)
fig = plt.figure(figsize =(10, 7))
 
# Horizontal Bar Plot
plt.bar(bracket, pollution)
plt.xlabel("Year Brackets")
plt.ylabel("Pollution Level")
# Show Plot
plt.show()



# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
#GAS
#LIQUID
#SOLID

# Set position of bar on X axis
br1 = np.arange(len(GAS))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
 
# Make the plot
plt.bar(br1, GAS, color ='r', width = barWidth,
        edgecolor ='grey', label ='Gaseous pollution')
plt.bar(br2, LIQUID, color ='g', width = barWidth,
        edgecolor ='grey', label ='Liquid pollution')
plt.bar(br3, SOLID, color ='b', width = barWidth,
        edgecolor ='grey', label ='Solid pollution')
 
# Adding Xticks
plt.xlabel('Types of pollution', fontweight ='bold', fontsize = 15)
plt.ylabel('Pollution', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(GAS))],
        bracket)
 
plt.legend()
plt.show()