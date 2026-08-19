import numpy as np
import pandas as pd

# 1. Initialize the Mock Messy Dataset Matrix
raw_data = {
    'Store': ['Amsterdam', 'Berlin', 'Chicago', 'Amsterdam', 'Chicago', 'Berlin'],
    'Net Revenue': ['$125,000', '$98,500', 'Missing', '$142,000', '$88,200', '$98,500'],
    'Discounts': ['10%', '5%', '12%', '8%', 'Missing', '5%']
}

df = pd.DataFrame(raw_data)
print("--- ORIGINAL MESSY DATAFRAME ---")
print(df)
print("\n" + "="*40 + "\n")

# 2. Drop Exact Duplicate Rows (Clears the extra Berlin row)
df = df.drop_duplicates()

# 3. Replace "Missing" Text with Official System Null Identifiers (NaN)
df = df.replace('Missing', np.nan)

# 4. Clean Currency Symbols and Convert to Math Floating Numbers
df['Net Revenue'] = df['Net Revenue'].str.replace('$', '', regex=False)
df['Net Revenue'] = df['Net Revenue'].str.replace(',', '', regex=False)
df['Net Revenue'] = df['Net Revenue'].astype(float)

# 5. Clean Percentage Symbols and Convert to Decimal Logic
df['Discounts'] = df['Discounts'].str.replace('%', '', regex=False).astype(float) / 100

print("--- CLEANED DATAFRAME READY FOR ANALYSIS ---")
print(df)

print("\n" + "="*40 + "\n")
print("--- SUMMARY STATISTICAL METRICS ---")
# .describe() instantly calculates count, mean, min, max, and standard deviation for your table!
print(df.describe())

print("\nMedian of Net Revenue:", df['Net Revenue'].median())
print("Mode of Store Location:", df['Store'].mode()[0])

df.to_csv('C:/Users/Parneet Kaur/PycharmProjects/exercise_1/final_clean_output.csv', index=False)
print("\n🎉 File successfully saved to your project directory!")