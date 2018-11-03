import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker
from scipy import stats
from scipy.stats import pearsonr


my_data = np.genfromtxt('data/USCS_TrendMap.csv', delimiter=',', usecols=(0,1,3),dtype="i8,U20,f8", skip_header=1)
incomes = np.genfromtxt('data/US_states_median_household_income.csv', delimiter=',', usecols=(1,2,3,4,5,6),dtype="U20,i8,i8,i8,i8,i8", skip_header=5)

years, locations, deaths = zip(*my_data)
incomes_states, incomes_2015, incomes_2014, incomes_2013, incomes_2012, incomes_2011 = zip(*incomes)
incomes_states = [i.strip() for i in incomes_states] # Cleaning the names
# Going through the years of income to get a mean
income_states = {}
for i, income_state in enumerate(incomes_states):
    income_state = income_state.strip()
    if income_state not in income_states:
        income_states[income_state] = 0
    income_mean = np.mean([incomes_2015[i], incomes_2014[i],incomes_2013[i], incomes_2012[i], incomes_2011[i]])
    income_states[income_state] = income_mean

print(income_states)
# We will create a dictionary containing each state
states = {}

for i, state in enumerate(locations):
    if "Columbia" in state:
        continue
    # If the state is not inside the dictionary,
    # we create a new entry, asigning its value to the deathcount.
    if state not in states:
        states[state] = []

    # The index i will have the information about which row it is.
    # Since states could be many times, we will have a list of
    # the deathcounts per state.
    states[state].append(deaths[i])

# Now we take the mean of the values, and override them
for key, value in states.items():
    states[key] = (np.mean(value), income_states[key])

# We can get a list of the states, and another list for the values,
# from our dictionary
list_states, list_values_and_incomes = zip(*states.items())
list_values, list_incomes = zip(*list_values_and_incomes)
print(list_incomes)

# Since the states are strings, we generate a range to use it instead
range_states = range(0, len(list_states))


fig = plt.figure()
ax = fig.add_subplot(111)

# Second y axis
ax2 = ax.twinx()
host = fig.add_subplot(111)

ax.set_xticks(range_states)
ax.set_xticklabels(list_states, rotation=80, fontsize=9)
ax.plot(range_states, list_values, "o-",ms=4,  color="#c64760")
ax2.plot(range_states, list_incomes, ".-",ms=4,  color="#15929F")
print(pearsonr(list_values,list_incomes))

ax.set_title('Nationwide Changes in Rates of Cancer Deaths')
ax.set_xlabel("States")
host.set_ylabel("Rates by state in women")
ax2.set_ylabel("Median hold income (USD $)")
ax.grid(True, color="#d9d1c7")
plt.tight_layout()
plt.show()