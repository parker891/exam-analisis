import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('StudentsPerformance.csv')
print(df.head())
df['average score'] = (df['math score']+df['reading score']+df['writing score']) / 3

# df.head()
# print(df.head())

# plt.figure(figsize=(7,4))
# sns.set_palette('husl')
# plt.title('Avg. Score Distribution', fontsize=15, fontweight='bold')
# sns.histplot(data=df, x='average score',bins=30,kde=True,color='g')

# plt.show()

# plt.figure(figsize=(7,4))
# sns.set_palette('husl',2)
# plt.title('Gender relation with average score', fontsize=15, fontweight='bold',)

# sns.histplot(data=df,x='average score',kde=True,hue='gender', bins = 20, alpha=0.4)
# plt.show()

# plt.figure(figsize=(12,5))

# plt.subplot(1,3,1)
# sns.boxplot(x = 'gender', y = 'math score', data = df,palette = ['coral', 'lawngreen'])

# plt.subplot(1,3,2)
# sns.boxplot(x = 'gender', y = 'reading score', data = df,palette = ['coral', 'lawngreen'])

# plt.subplot(1,3,3)
# sns.boxplot(x = 'gender', y = 'writing score', data = df,palette = ['coral', 'lawngreen'])

# plt.tight_layout()
# plt.show()
# sns.scatterplot(data=df, x='math score', y='reading score')
# plt.title("Reading Score with Math Score")
# plt.xlabel("Math Score")
# plt.ylabel('Reading Score')

# plt.show()

# labels=df['gender'].value_counts().index
# values=df['gender'].value_counts().values

# plt.figure(figsize=(6,6))
# plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title('Gender')
# plt.show()

sns.barplot(x='race/ethnicity',y='math score',data=df);
df.groupby("race/ethnicity")["math score"].mean()
plt.show()
