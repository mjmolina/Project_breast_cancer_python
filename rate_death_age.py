import numpy as np
from scipy.stats import pearsonr
from matplotlib import pyplot as plt
from matplotlib import ticker
from scipy import stats


my_data1 = np.genfromtxt('data/USCS_DemographicAge.csv', delimiter=',', usecols=(2,3),dtype="U20,f8")
print(my_data1)

age_specific_rate, death_count = zip(*my_data1)
print(death_count)

x= range(0,len(age_specific_rate))

fig = plt.figure()
ax = fig.add_subplot(111)

print (age_specific_rate)
ax.set_xticks(x)
ax.set_xticklabels(age_specific_rate)

ax.plot(x,death_count, "o-",color="#d46051",ms=4)

ax.set_title('Rate of Breast Cancer Deaths by age group in USA', fontsize=11)
ax.set_xlabel("Age group (range of ages)", fontsize=11)
ax.set_ylabel("Rate Breast Cancer Deaths\n(Rate per 100,000)", fontsize=11)
plt.show()