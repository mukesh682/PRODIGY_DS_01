import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


chunk_size = 10**6  # 1 million rows per chunk
data_iter = pd.read_csv('data_cardiovascular_risk.csv', chunksize=chunk_size, usecols=['age','BMI'])

category_counts = {}

# Process each chunk
for chunk in data_iter:
    chunk_counts = chunk['age'].value_counts().to_dict()
    for age, count in chunk_counts.items():
        if age in category_counts:
            category_counts[age] += count
        else:
            category_counts[age] = count

category_df = pd.DataFrame(list(category_counts.items()), columns=['age', 'BMI'])



category_df = category_df.sort_values(by='BMI', ascending=False)

# Plotting the bar chart
plt.figure(figsize=(12, 8))
sns.barplot(x='age', y='BMI', data=category_df, palette='viridis')
plt.title('Distribution of Categorical Variable')
plt.xlabel('age')
plt.ylabel('BMI')
plt.xticks(rotation=90)
plt.show()
