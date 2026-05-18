import pandas as pd
data = {
    "Name": ["Amit", "Riya", "John", "Sara","Deepa","seema"],
    "Age": [23, 25, 22, 24,30,28],
    "Salary": [30000, 40000, 35000, 45000,80000,70000]
    
}

df = pd.DataFrame(data)
print(df)
#df = pd.read_csv("data.csv")
#df.to_csv("output.csv", index=False)
print(df.head())       # First 5 rows
print(df.tail())       # Last 5 rows
print(df.info())       # Summary
print(df.describe())   # Statistical summary
print(df["Name"] )             # Single column
print(df[["Name", "Age"]])     # Multiple columns
print(df.iloc[0])              # First row
print(df.loc[0, "Name"])     # Specific value
print(df[df["Age"] > 23])
print(df[df["Salary"] > 35000])
df["Bonus"] = df["Salary"] * 0.10
print(df)
df["Age"] = df["Age"] + 1
print(df)
print(df.drop("Bonus", axis=1, inplace=True))
print(df.sort_values(by="Salary", ascending=False))
print(df.groupby("Age")["Salary"].mean())
print(df.isnull())
print(df.fillna(0))
print(df.dropna())
print(df["Salary"].mean())
print(df["Salary"].max())
print(df["Salary"].min())
print(df["Salary"].sum())
df["Salary"] = df["Salary"].apply(lambda x: x + 5000)
print(df)
df1 = pd.DataFrame({"ID": [1,2], "Name": ["A", "B"]})
df2 = pd.DataFrame({"ID": [1,2], "Salary": [30000, 40000]})

merged = pd.merge(df1, df2, on="ID")
print(merged)
print(pd.concat([df1, df2]))
df.rename(columns={"Name": "Employee_Name"}, inplace=True)
print(df)
print(df["Age"].unique())
print(df["Age"].nunique())
print(df["Age"].value_counts())
df.set_index("Employee_Name", inplace=True)
df.reset_index(inplace=True)
df["Age"] = df["Age"].astype(float)
print(df)
