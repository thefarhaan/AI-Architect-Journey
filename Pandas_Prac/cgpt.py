import pandas as pd

students = {
    "Name": ["Alice", "Bob", "Carol", "David", "Eva"],
    "Age": [20, 22, 21, 23, 20],
    "Marks": [85, 78, 92, 65, 88],
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai"]
}

df = pd.DataFrame(students)

# print(df)
print(df.iloc[0:3]) 
print(df.shape)
print(df[['Name', 'Marks']])
print(df[df['Marks']  > 80])
df["Status"] = ["Passed" if mark >= 40 else "Failed" for mark in df["Marks"]]
print(df)
print(df["Marks"].mean())
print(df["Marks"].max())
print(df.sort_values("Marks", ascending=False))
print(df.groupby("City")["Marks"].mean())
print(df.to_csv("students.csv", index=False))  # Save DataFrame to CSV file