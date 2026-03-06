import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28 ],
    "City": ["New York", "San Francisco", "Los Agneles", "Chicago"]
}

df = pd.DataFrame(data)
print(df)

# accessing columns
print(df["Name"])

# accessing rows
print(df.iloc[2])
print(df.loc[3])

# slicing rows
print(df[['Name', 'Age']]) #specific columns
print(df[1:3]) #specific rows

unique_dates = df['Age'].unique()
print(unique_dates)

high_above_25 = df["Age"] > 25
print(df[high_above_25])