import pandas as pd

a = pd.Series([10, 20, 30, 40, 50])
print(a)

a1 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(a1)

data = {'Name': ['Farhaan','Khan'], 'Age': [18, 20]}
df = pd.DataFrame(data)
print(df)

data = {"Name":["Farhaan", "Khan", "Pathaan"], 
        "Age": [18, 20, 25],
        "City": ["Delhi", "Mumbai", "Goa"]}
df = pd.DataFrame(data)
print(df)

data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
df = pd.DataFrame(data)
print(df)

data = {"Name":["Farhaan", "Khan", "Pathaan"], 
        "Age": [18, 20, 25],
        "Score": [85, 90, 95]}
df = pd.DataFrame(data)
print(df[['Name']])
print(df[['Name', 'Score']])
print(df.iloc[0])  # first row
print(df.iloc[1])  # second row
print(df[0:2])  # first two rows
print(df[1:2])
print(df[(df['Age'] > 18) & (df['Score'] > 90)])  # filter rows based on conditions
print(df.isnull())  # check for missing values
print(df.dropna())  # remove rows with missing values
print(df.fillna(0))  # fill missing values with 0  
print(df.rename(columns={'Score': 'Marks'}))  # rename columns
print(df.rename(columns={'Name': 'Student_Name'}))  # rename Name column to Student_Name
print(df.replace({'Age': {18: 19}}))  # replace age 18 with 19
print(df['Age'].min())  # minimum age
print(df['Age'].max())  # maximum age
print(df['Age'].mean())  # average age
print(df['Age'].median())  # median age
print(df['Age'].sum())  # sum age
