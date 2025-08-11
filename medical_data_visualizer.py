import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/yashkalathiya/Downloads/Yash/Data Analyst Portfolio Projects/medical_examination.csv')
df['overweight'] = ((df['weight'] / (df['height']/100)**2) > 25).astype(int)
df[['gluc','cholesterol']] = (df[['gluc','cholesterol']] > 1).astype(int)

def draw_cat_plot():
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name = 'total')
    fig = sns.catplot(data = df_cat, kind='bar', x = 'variable', y='total', hue = 'value', col='cardio').fig
    return fig

fig = draw_cat_plot()
plt.show()

def draw_heat_map():
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(12, 12))


    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, vmax=0.3, square=True, linewidths=0.5, cbar_kws={"shrink": 0.5})

    return fig

fig = draw_heat_map()
plt.show()