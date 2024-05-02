import pandas as pd

# Load the Excel file
df = pd.read_csv('/Users/lucastamatescumicrosoft/Downloads/forbidden_question_set.csv')

# Randomly sample 5 rows from the DataFrame
sample = df.sample(n=100)

# Write the sample DataFrame to a CSV file
sample.to_csv('sampled_jailbreaking_questions.csv', index=False)

print(sample)