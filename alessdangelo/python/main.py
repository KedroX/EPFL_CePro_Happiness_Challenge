# This script generates scatter plots to analyze the relationship between GDP and Happiness scores using data from a CSV.
# Helpful documentation : https://pandas.pydata.org/docs/user_guide/10min.html & https://matplotlib.org/stable/users/explain/quick_start.html
import pandas as pd 
import matplotlib.pyplot as plt
import argparse

# Set up argument parser to check if the user wants to save the charts directly instead of opening them
# source : https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(description="Generate and optionally save charts for GDP vs Happiness analysis.")
parser.add_argument('--save', action='store_true', help="Save the charts as images instead of displaying them.")
args = parser.parse_args()

# Try to read the CSV file provided into a DataFrame, will exit if the file is not found
try:
    df = pd.read_csv('../data/data-2019.csv')
except FileNotFoundError:
    print("File not found. Please check the path to the CSV file.")
    exit()
except pd.errors.EmptyDataError:
    print("Empty CSV file. Please check the CSV file path and contents.")
    exit()

# Check if the DataFrame is empty and exit accordingly
if df.empty :
    print("The DataFrame is empty. Please check the CSV file path and contents.")
    exit()

# Check if the required columns are present in the DataFrame, exiting if not
# source: https://stackoverflow.com/questions/24870306/how-to-check-if-a-column-exists-in-pandas/44119747
required_columns = ['Country', 'Region', 'GDP 2019', 'Score 2019']
if all(item in df.columns for item in required_columns) == False:
    print("The DataFrame does not contain the required columns. Please check the CSV file.")
    exit()

# Get the average happiness and gdp score value for each region
region_avg_happiness = df.groupby('Region')["Score 2019"].mean()
region_avg_gdp = df.groupby('Region')["GDP 2019"].mean()

# Get the top 10 and bottom 10 countries ranked by GDP, excluding the index
top_countries = df[['Country','GDP 2019', 'Score 2019']].nlargest(10, ['GDP 2019', 'Score 2019']).to_string(index=False)
bottom_countries = df[['Country','GDP 2019', 'Score 2019']].nsmallest(10, ['GDP 2019', 'Score 2019'],).to_string(index=False)

# Compute the correlation between GDP and Region_Average Happiness
correlation = df['GDP 2019'].corr(df['Score 2019'])

# Print the average happiness value for each region
print('----------------------------------------------------------------------')
print('Average happiness values for each region:')
print(region_avg_happiness)
print('----------------------------------------------------------------------')

# Print the top 10 countries ranked by GDP
print('Top 10 Countries ranked by GDP:')
print(top_countries)
print('----------------------------------------------------------------------')

# Print the bottom 10 countries ranked by GDP
print('Bottom 10 Countries ranked by GDP:')
print(bottom_countries)
print('----------------------------------------------------------------------')

# Print the computed correlation between GDP and Region_Average Happiness
print(f"Correlation between GDP and Happiness Score: {correlation:.2f}")


# Define the 1st figure : Scatter plot for GDP vs Average Happiness by Region
plt.figure(figsize=(15, 6), num='By Region')
plt.scatter(region_avg_gdp.values, region_avg_happiness.values, color='dodgerblue', alpha=0.7)
plt.title('GDP 2019 vs. Region Average Happiness Score', fontsize=16)
plt.xlabel('Average Region GDP (score)', fontsize=14)
plt.ylabel('Average Region Happiness (score)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

# Save the chart as an image instead of rendering it if the --save argument is passed
if args.save:
    plt.savefig('GDP_vs_Region_Average_Happiness.png')  # Save the chart as an image


# Define the 2nd figure : Scatter plot for GDP vs Average Happiness by Country
plt.figure(figsize=(15, 6), num='By Country')
plt.scatter(df['GDP 2019'], df['Score 2019'], color='dodgerblue', alpha=0.7)
plt.title('GDP 2019 vs. Country Average Happiness Score', fontsize=16)
plt.xlabel('Country GDP (score)', fontsize=14)
plt.ylabel('Average Country Happiness (score)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

# Save the chart as an image instead of rendering it if the --save argument is passed 
# Otherwise it will open the charts to a new window
if args.save:
    print("\nDetected 'save' argument, chart images saved in the /python folder")
    plt.savefig('GDP_vs_Country_Average_Happiness.png')  # Save the chart as an image
else:
    print("\nOpening a new window containing the scatter charts ...")
    plt.show()