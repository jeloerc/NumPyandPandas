import pandas as pd  # pd is the standard convention

# Create a Series
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(f"Series:\n{s}")
print(f"Value at index 'b': {s['b']}")

# Create a DataFrame from a dictionary
data = {
    'Name': ['Ana', 'Luis', 'Eva', 'Juan'],
    'Age': [28, 34, 29, 40],
    'City': ['Madrid', 'Barcelona', 'Madrid', 'Valencia']
}
df = pd.DataFrame(data)
print(f"\nDataFrame:\n{df}")

# Basic inspection
print(f"\nFirst 2 rows (head):\n{df.head(2)}")
print(f"\nLast row (tail):\n{df.tail(1)}")
print("\nGeneral info (info):")
df.info()
print(f"\nDescriptive statistics (describe):\n{df.describe()}")
print(f"\nShape (rows, columns): {df.shape}")
print(f"Column names: {df.columns.tolist()}")  # .tolist() converts it to a Python list

# Select columns
name_col = df['Name']  # Returns a Series
print(f"\n'Name' column (as Series):\n{name_col}")
subset_df = df[['Name', 'City']]  # Double brackets return a DataFrame
print(f"\nSubset of 'Name' and 'City' columns (as DataFrame):\n{subset_df}")

# Select rows (iloc uses numerical indices, loc uses labels/indices)
print(f"\nRow at index 1 (iloc):\n{df.iloc[1]}")
# If the index were different (e.g., letters like in the Series), we would use df.loc['b']
