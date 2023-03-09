import matplotlib.pyplot as plt
import numpy as np

# Data
states = ['Andhra Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Odisha', 'Punjab', 'Rajasthan', 'Tamil Nadu', 'Telangana', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
rice = [3302, 3106, 2155, 1597, 2141, 3044, 1705, 2078, 2131, 2793, 2733, 1340, 1841, 2289, 2716, 1896, 2676, 3456, 1396, 1839, 2346]
wheat = [np.nan, 1147, 2206, 1227, 3014, 5030, 1671, 1689, 1908, 858, np.nan, 2360, 1558, 3139, 4325, 3457, 3075, 2485, 2865, 1405, 3042]
coarse_cereals = [4192, 675, 2336, 781, 1402, 2001, 2318, 1490, 1443, 1957, 831, 1397, 1178, 3331, 2717, 1148, 1619, 1703, 3175, 1249, 2452]
pulses = [711, 573, 975, 613, 815, 706, 954, 508, 885, 492, 747, 803, 693, 1985, 955, 2828, 683, 2009, 1812, 594, 802]
foodgrains = [2600, 1704, 2098, 1384, 1874, 3879, 1911, 1690, 1798, 1629, 2695, 1510, 1155, 3188, 4132, 3666, 3316, 3198, 4266, 1909, 3496]

# Figure and Axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting data
ax.plot(states, rice, label='Rice')
ax.plot(states, wheat, label='Wheat')
ax.plot(states, coarse_cereals, label='Coarse Cereals')
ax.plot(states, pulses, label='Pulses')
ax.plot(states, foodgrains, label='Foodgrains')

# Axes labels
ax.set_xlabel('States')
ax.set_ylabel('Production (in 000 tonnes)')
ax.set_title('Cereal Production in India (2011-16)')

# Tick labels rotation
plt.xticks(rotation=90)

# Legend
ax.legend()

# Show plot
plt.show()
