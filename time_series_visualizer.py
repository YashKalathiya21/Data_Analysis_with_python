import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    '/Users/yashkalathiya/Downloads/Yash/Data Analyst Portfolio Projects/fcc-forum-pageviews.csv',
    index_col = 'date',parse_dates=True)

df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Draw Line Plot

plt.plot(df.index,df['value'])
plt.xlabel('Date')
plt.ylabel('Page Views')
plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

# Draw Bar Plot

df2 = df.copy()
df2['year'] = df2.index.year
df2['month'] = df2.index.month
df2_avg = df2.groupby(['year','month']).mean().unstack(level=-1)
df2_avg.plot(kind='bar', figsize=(10, 7)).figure
plt.xlabel("Years")
plt.ylabel("Average Page Views")
plt.legend(
    labels=['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'],
    title="Months")

# Draw Box Plot

df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['year'] = df_box['date'].dt.year
df_box['month'] = df_box['date'].dt.strftime('%b')
df_box['month_num'] = df_box['date'].dt.month
df_box = df_box.sort_values('month_num')

fig, axes = plt.subplots(1,2,figsize=(16,6))

# Year-wise Box Plot
sns.boxplot(data=df_box,x='year', y='value', ax=axes[0])
axes[0].set_title("Year-wise Box Plot (Trend)")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Page Views")

# Month-wise Box Plot
sns.boxplot(data=df_box, x='month', y='value', ax=axes[1])
axes[1].set_title("Month-wise Box Plot (Seasonality)")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Page Views")