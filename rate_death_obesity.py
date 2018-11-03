import numpy as np
from scipy.stats import pearsonr
from matplotlib import pyplot as plt
from matplotlib import ticker
from scipy import stats

data_obesity = np.genfromtxt('data/Nutrition__Physical_Activity__and_Obesity_no_men.csv', delimiter=',', usecols=(1,3,10),dtype="i8,U20,f8", skip_header=1)
data_deaths = np.genfromtxt('data/USCS_TrendMap.csv', delimiter=',', usecols=(0,1,3),dtype="i8,U20,f8", skip_header=1)

years_obesity, locations_obesity, values = zip(*data_obesity)
years_deaths, locations_deaths, deaths = zip(*data_deaths)

# Getting obesity data
obesity_states = {}
for i, state in enumerate(locations_obesity):
    if ("Columbia" in state or "National" in state or "Guam" in state
            or "Puerto Rico" in state or "Virgin Islands" in state):
        continue
    if 2011 > years_obesity[i] >= 2016:
        continue
    if state not in obesity_states:
        obesity_states[state] = []
    if not np.isnan(values[i]):
        obesity_states[state].append(values[i])

for key, value in obesity_states.items():
    obesity_states[key] = np.mean(value)


# Getting deaths data
deaths_states = {}
for i, state in enumerate(locations_deaths):
    if "Columbia" in state or "National" in state or "Guam" in state:
        continue
    if years_deaths[i] < 2011 or years_deaths[i] >= 2016:
        continue
    if state not in deaths_states:
        deaths_states[state] = []
    if not np.isnan(deaths[i]):
        deaths_states[state].append(deaths[i])

for key, value in deaths_states.items():
    deaths_states[key] = np.mean(value)

# We go through the dictionary and we add to a lists the values in order
# alphabetically because we are sorting the keys (states)
sorted_states = sorted(deaths_states)
list_states = []
list_deaths = []
list_obesity = []
for state in sorted_states:
    list_states.append(state)
    list_deaths.append(deaths_states[state])
    list_obesity.append(obesity_states[state])


# Since the states are strings, we generate a range to use it instead
range_states = range(0, len(list_states)) # Is the same for both

fig = plt.figure()
ax = fig.add_subplot(111)

# Second y axis
ax2 = ax.twinx()
print(list_states)

ax.set_xticks(range_states)
ax.set_xticklabels(list_states, rotation=80, fontsize=9)
ax.plot(range_states, list_deaths, "o-",ms=4,  color="#c64760")
ax2.plot(range_states, list_obesity, ".-",ms=4,  color="#648e91")
print(pearsonr(list_deaths,list_obesity))

ax.set_title('Rates of Breast Cancer Deaths and Obesity')
ax.set_xlabel("States")
ax.set_ylabel("Rates by State in women")
ax2.set_ylabel("Obesity in women(%)")
ax.grid(True, color="#d9d1c7")
plt.tight_layout()
plt.show()