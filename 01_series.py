import pandas as pd

data = list(range(10))
print(type(data))
# print(data)

s = pd.Series(data)
print(s)

print(s[2])

print(s.iloc[3])

print(s.iloc[1:3])