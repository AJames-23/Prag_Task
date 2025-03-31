# Please install the following for this project:
# pandas
# seaborn
# matplotlib
# numpy
# scipy

# This script loads the two data sets, merges them together, filters to 'GDP per capita'
# and saves the new merged dataset as 'df_cleaned.csv'

import pandas as pd

# Load data
df1 = pd.read_csv("data.csv")
df2 = pd.read_csv("OECD,DF_FACTBOOK2015_PUB,+all.csv", low_memory=False)

# Standardise country names to title case
df1["Location"] = df1["Location"].str.title()
df2["Country"] = df2["Country"].str.title()

# Filter to the things we are interested in to reduce size and speed up analysis
subsOfInterest = ['GDP per capita']

df2 = df2[df2['Subject'].isin(subsOfInterest)]

# Apply name corrections
name_mapping = {
    "United Kingdom Of Great Britain And Northern Ireland": "United Kingdom",
}
df1["Location"] = df1["Location"].replace(name_mapping)

# Rename columns for merging the 2 sets of data
df1.rename(columns={'Location': 'Country', 'Period': 'Year'}, inplace=True)
df2.rename(columns={'Year':'Year1', 'TIME_PERIOD': 'Year'}, inplace=True)

# Merge the 2 sets of data on 'Country' and 'Year'
merged_df = pd.merge(df1, df2, on=['Country', 'Year'], how='inner')

# Remove columns with any blank rows to tidy things up a bit
df_cleaned = merged_df.dropna(axis=1, how='any')  # Removes columns with NaN values
df_cleaned = df_cleaned.loc[:, (df_cleaned != '').any(axis=0)]  # Removes columns with no data

# Save the merged dataset
df_cleaned.to_csv(r"df_cleaned.csv", index=False)

print("Merged dataset saved as 'df_cleaned.csv'")

