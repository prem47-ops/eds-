


# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: Load Dataset
# -----------------------------
# Load Titanic dataset from URL
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

print("Dataset Preview:\n", df.head())

# -----------------------------
# STEP 2: Data Cleaning
# -----------------------------
# Fill missing Age with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing Embarked with most common value
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# -----------------------------
# STEP 3: IDENTIFIED GRAINS (5)
# -----------------------------
# Grain 1: Survival count
survival_count = df['Survived'].value_counts()

# Grain 2: Survival by gender
survival_gender = df.groupby('Sex')['Survived'].sum()

# Grain 3: Passenger class distribution
pclass_count = df['Pclass'].value_counts()

# Grain 4: Age distribution
age_data = df['Age']

# Grain 5: Fare vs Age relationship
fare = df['Fare']
age = df['Age']

# -----------------------------
# STEP 4: VISUALIZATIONS
# -----------------------------

# GRAPH 1: Survival Count (Bar Chart)
plt.figure()
survival_count.plot(kind='bar')
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.xticks(rotation=0)
plt.savefig('survival_count.png')
plt.show()

# GRAPH 2: Survival by Gender (Bar Chart)
plt.figure()
survival_gender.plot(kind='bar')
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Survivors")
plt.savefig('survival_gender.png')
plt.show()

# GRAPH 3: Passenger Class Distribution (Pie Chart)
plt.figure()
pclass_count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Passenger Class Distribution")
plt.ylabel("")
plt.savefig('pclass_distribution.png')
plt.show()

# GRAPH 4: Age Distribution (Histogram)
plt.figure()
plt.hist(age_data, bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig('age_distribution.png')
plt.show()

# GRAPH 5: Fare vs Age (Scatter Plot)
plt.figure()
plt.scatter(age, fare)
plt.title("Fare vs Age")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.savefig('fare_vs_age.png')
plt.show()

print("\n===== TITANIC ANALYSIS COMPLETED =====")
