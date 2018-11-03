import numpy as np
from scipy.stats import pearsonr
from matplotlib import pyplot as plt
from matplotlib import ticker
from scipy import stats


my_data2 = np.genfromtxt('data/USCS_DemographicRace.csv', delimiter=',', usecols=(2,3),dtype="U20,f8")

print(my_data2)

race, death_count = zip(*my_data2)
print(death_count)

x= range(0,len(race))

fig = plt.figure()
ax = fig.add_subplot(111)

print (race)
ax.set_xticks(x)
ax.set_xticklabels(race)

#bar(1, Data, 'colorcode'), bar(2, Data, 'colorcode') , bar (3, Data, 'colorcode')

ax.bar(x,death_count, color=['#c3e4cf', '#fab1a6', '#93bab3', '#f8d979', '#92d3ca'])

ax.set_title('Rate of cancer deaths by ethnicities in USA')
ax.set_xlabel("Ethnicities")
ax.set_ylabel(r"Rate of cancer deaths in women (%)")

plt.show()