# This opens the merged dataset and generates a bar chart with country along x-axis, particle count on y-axis,
# and overlays a line chart of GDP per capita

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

# Load merged data
data = pd.read_csv(r"df_cleaned.csv")

# Display the first few rows of the data
print(data.head())

# Use seaborn
sb.set_theme()

# Filter the data by conditions in another column
data = data[(data['Dim1'] == 'Total') & (data['Subject']=='GDP per capita')]

# Sort data by particle levels in descending order
data = data.sort_values(by='FactValueNumeric', ascending=False).reset_index(drop=True)

# Plot particle count
plot = sb.barplot(x='Country', y='FactValueNumeric', hue='Country', data=data, palette='dark:blue')

# Rotate the x-axis labels to make them vertical
plt.xticks(rotation=90)
#plot.set_titles("")
plt.xlabel('Country')
plt.ylabel('PM2.5 Concentration')

# Create a secondary y-axis
ax2 = plot.twinx()
# Line plot for GDP on the secondary y-axis
sb.lineplot(x='Country', y='OBS_VALUE', data=data, ax=ax2, color='red', marker="o", linewidth=2)

# Labels for the secondary y-axis
ax2.set_ylabel("GDP per capita", color="red")

plt.show()