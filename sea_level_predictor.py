import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('/Users/yashkalathiya/Downloads/Yash/Data Analyst Portfolio Projects/epa-sea-level.csv')

# Create scatter plot
plt.figure(figsize=(10,6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=15)

plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
plt.xlabel('Year')
plt.ylabel('CSIRO Adjusted Sea Level')

slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
years = pd.Series(range(1880,2051))
plt.plot(years, intercept + slope*years, 'r')
# Create second line of best fit
df2 = df.loc[df['Year'] >= 2000]
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
years2 = pd.Series(range(2000,2051))
plt.plot(years2, intercept2 + slope2*years2, 'b', linestyle = '--')
# Add labels and title
ax.set(xlabel="Year", ylabel="Sea Level (inches)", title="Rise in Sea Level")
# Save plot and return data for testing
plt.legend()
plt.savefig('sea_level_plot.png')