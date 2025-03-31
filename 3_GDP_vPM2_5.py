# Plots a scatter graph of GDP per capita on x-axis vs particle count on y-axis
# fits linear regression and displays R_squared 'goodness of fit'.

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Load merged data
data = pd.read_csv(r"df_cleaned.csv")

# Display the first few rows of the data
print(data.head())

# Use seaborn
sb.set_theme()

# Filter the data by conditions in another column
data = data[(data['Dim1'] == 'Total') & (data['Subject']=='GDP per capita')]

# Sort data by GDP per capita for better visualisation
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
#plt.data()
sb.regplot(x='OBS_VALUE', y='FactValueNumeric', data=data, scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})

# Add regression equation and R² to the plot
plt.text(x.min(), y.max(), f"{regression_eq}\n{r_squared}", fontsize=12, color="red", bbox=dict(facecolor='white', alpha=0.5))

# Titles and labels
plt.title("Trend of PM2.5 Concentration vs GDP per Capita", fontsize=14)
plt.xlabel("GDP per Capita (USD)")
plt.ylabel("PM2.5 Concentration")

# Show the plot
plt.show()

