There are a number of scripts in this project:

1_Merge_Data.py:
  This script loads the two data sets, merges them together, filters to 'GDP per capita' and saves the new merged dataset for further processing
  
2_GDP_perCapita.py:
  This opens the merged dataset and generates a bar chart with country along x-axis, particle count on y-axis, and overlays a line chart of GDP per capita
  
2.5_GDP_perCapita.py:
  As above, but splits by year
  
3_GDP_vPM2_5.py:
  Plots a scatter graph of GDP per capita on x-axis vs particle count on y-axis fits linear regression and displays R_squared 'goodness of fit'.
  
4_Unique_Subs.py:
  Generates a list of unique factors and then iterates through the factors, generating linear regression then prints the top 10 factors with the highest R_squared values
  
5_Population_Levels.py:
  Generates a graph of population vs particle count. Conclusion is that there isn't necessarily a real correlation here
