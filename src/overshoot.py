import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pycaret.regression import *

data = pd.read_csv("../data/overshoot.csv")

year = data['Year']
fullDate = data['DaysPassed']

fig = plt.figure(figsize =(10, 7))
 
# Horizontal Bar Plot
plt.bar(year, fullDate)
plt.xlabel("Year")
plt.ylabel("Days passed until Overshoot Day")
# Show Plot
plt.show()
