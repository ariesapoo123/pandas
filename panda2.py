import pandas as pd

df = pd.read_csv('weather.csv')

print("First 5 rows of Data Frame are: ")
print(df.head())

print("First 10 rows of Data Frame are: ")
print(df.head(10))

print("Basic statistics on the particular dataset are: ")
print(df.describe())

print("Last 5 rows of Data Frame are: ")
print(df.tail())

l=df.columns

second_column=l[1]

print("Second Column is:", second_column)

df1 = pd.read_csv('weather.csv', usecols=[second_column])

print("Basic Statistics on the extracted second coloum are: ")
print(df1.describe())