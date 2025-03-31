# This opens the merged dataset and generates a bar chart with country along x-axis, particle count on y-axis,
# and overlays a line chart of GDP per capita and splits by year

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

# Load merged data
data = pd.read_csv("df_cleaned.csv")

# Display the first few rows of the data
print(data.head())

# Use seaborn
sb.set_theme()

# Filter the data by conditions in another column
data = data[(data['Dim1'] == 'Total') & (data['Subject']=='GDP per capita')]

# Sort data by particle levels in descending order
data = data.sort_values(by='FactValueNumeric', ascending=False).reset_index(drop=True)

# Create a FacetGrid for multiple subplots (one per year)
g = sb.FacetGrid(data, col="Year", col_wrap=3, sharey=False, height=3)

# Loop through each subplot
for ax, (year, subset) in zip(g.axes.flat, data.groupby("Year")):
    # Bar plot for PPM (Primary Y-axis)
    sb.barplot(x="Country", y="FactValueNumeric", data=subset, ax=ax, color="skyblue", order=subset['Country'])

    # Create secondary Y-axis
    ax2 = ax.twinx()

    # Line plot for GDP (Secondary Y-axis)
    sb.lineplot(x="Country", y="OBS_VALUE", data=subset, ax=ax2, color="red", marker="o", linewidth=2)

    # Labels for each axis
    ax.set_ylabel("PM2.5 Concentration", color="blue")
    ax2.set_ylabel("GDP per capita (USD)", color="red")

    # Rotate x-axis labels for readability
    ax.set_xticks(range(len(subset["Country"])))  # Set tick positions
    ax.set_xticklabels(subset["Country"], rotation=90, fontsize=7)  # Set labels with rotation

# Set title for the entire figure
plt.suptitle("PPM vs GDP by Country (Grouped by Year)", fontsize=14, y=1.05)

# Show the plots
plt.show()