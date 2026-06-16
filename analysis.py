import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("train.csv")

# First 5 rows
print("First 5 Rows:")
print(df.head())

# Shape
print("\nDataset Shape:")
print(df.shape)

# Columns
print("\nColumns:")
print(df.columns)

# Information
print("\nDataset Info:")
print(df.info())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values

# Age -> Median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Embarked -> Mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Cabin -> Unknown
df['Cabin'] = df['Cabin'].fillna('Unknown')

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Check duplicate rows

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

# Box Plot for Fare

plt.figure(figsize=(8,5))
sns.boxplot(x=df['Fare'])

plt.title('Box Plot of Fare')
plt.show()

plt.figure(figsize=(6,4))

sns.countplot(x='Survived', data=df)

plt.title('Passenger Survival Count')
plt.xlabel('Survived')
plt.ylabel('Count')

plt.show()

plt.figure(figsize=(8,5))

sns.countplot(
    x='Sex',
    hue='Survived',
    data=df
)

plt.title('Gender vs Survival')
plt.xlabel('Gender')
plt.ylabel('Count')

plt.show()

plt.figure(figsize=(8,5))

sns.countplot(
    x='Pclass',
    hue='Survived',
    data=df
)

plt.title('Passenger Class vs Survival')
plt.xlabel('Passenger Class')
plt.ylabel('Count')

plt.show()

plt.figure(figsize=(8,5))

sns.histplot(
    df['Age'],
    bins=20,
    kde=True
)

plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.show()

plt.figure(figsize=(10,6))

numeric_df = df.select_dtypes(
    include=['int64', 'float64']
)

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title('Correlation Heatmap')

plt.show()

