# Generates a graph of population vs particle count.
# Conclusion is that there isn't necessarily a real correlation here

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Load data
data = pd.read_csv("df_cleaned_unfiltered.csv")

# Filter relevant data
data = data[(data['Dim1'] == 'Total') & (data['Subject'] == 'Population levels')]

# Sort by GDP for better visualization
data = data.sort_values(by=['Year', 'OBS_VALUE'])

# Regression Calculation
x = data['OBS_VALUE']  # GDP per capita
y = data['FactValueNumeric']  # PM2.5 Concentration

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
regression_eq = f"y = {slope:.2f}x + {intercept:.2f}"  # Equation of line
r_squared = f"R² = {r_value**2:.3f}"  # R² value

# Set seaborn theme
sb.set_theme(style="whitegrid")

# Scatter plot with regression line
plt.figure(figsize=(12, 6))
sb.regplot(x=x, y=y, scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})

# Add regression equation and R² to the plot
plt.text(x.min(), y.max(), f"{regression_eq}\n{r_squared}", fontsize=12, color="red", bbox=dict(facecolor='white', alpha=0.5))

# Labels
plt.title(f"Regression: PM2.5 Concentration vs Population levels", fontsize=14)
plt.xlabel("Population levels")
plt.ylabel("PM2.5 Concentration")

# Show the plot
plt.show()