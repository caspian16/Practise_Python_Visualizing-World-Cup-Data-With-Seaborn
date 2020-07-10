import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv('WorldCupMatches.csv')
df['Total Goals']=df['Home Team Goals'] + df['Away Team Goals'] 
df_goals=pd.read_csv('goals.csv')
sns.set_style('whitegrid')
sns.set_context("notebook",font_scale=1.25)
f,ax =plt.subplots(figsize=(12,7))
ax=sns.barplot(data=df, x='Year',y='Total Goals')
ax.set_title('Number of goals from 1930-2014')
plt.show()
f, ax2=plt.subplots(figsize=(12,7))
ax2=sns.boxplot(data=df_goals,x='year',y='goals',,palette='Spectral')
ax2.set_title('Number of goals')

plt.show()