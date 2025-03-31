# Generates a list of unique factors and then iterates through the factors, generating linear regression
# then prints the top 10 factors with the highest R_squared values

import pandas as pd
import scipy.stats as stats

def merge_unfiltered():

    # Load data
    df1 = pd.read_csv("data.csv")
    df2 = pd.read_csv("OECD,DF_FACTBOOK2015_PUB,+all.csv", low_memory=False)

    # Standardise country names to title case
    df1["Location"] = df1["Location"].str.title()
    df2["Country"] = df2["Country"].str.title()

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
    df_cleaned.to_csv(r"df_cleaned_unfiltered.csv", index=False)

    print("Merged dataset saved as 'df_cleaned_unfiltered.csv'")

def list_unique_subs():
    data = pd.read_csv('df_cleaned_unfiltered.csv')

    # Get unique values from the Subject column
    unique_values = data['Subject'].unique()

    # Create an empty list to store results
    results = []

    # Iterate through subjects and calculate linear regression for each
    for i, name in enumerate(unique_values):
        # Filter relevant data by subject
        df = data[(data['Dim1'] == 'Total') & (data['Subject'] == name)]

        # Regression Calculation
        x = df['OBS_VALUE']  # Data
        y = df['FactValueNumeric']  # PM2.5 Concentration

        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        regression_eq = f"y = {slope:.2f}x + {intercept:.2f}"  # Equation of line
        r_squared = f"{r_value ** 2:.3f}"  # R² value

        # Append results to list
        results.append([name, regression_eq, r_squared])

    # Convert results list into a DataFrame
    results_df = pd.DataFrame(results, columns=['Subject', 'Regression Equation', 'R_squared'])

    # Sort the DataFrame by R_squared in descending order and get the top 10 rows
    top_10_results = results_df.sort_values(by="R_squared", ascending=False).head(10)

    # Display the top 10 results
    print(top_10_results)
    # Save to CSV
    results_df.to_csv('regression_results.csv', index=False)

    print("Results saved to regression_results.csv")

merge_unfiltered()
list_unique_subs()