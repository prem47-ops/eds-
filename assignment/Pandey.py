import pandas as pd

# Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# Display first rows
print(df.head())

# Check structure
print(df.info())
# Drop missing values
df = df.dropna()

# Convert columns
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Create new columns
df['Month'] = df['ORDERDATE'].dt.month
df['Sales'] = df['QUANTITYORDERED'] * df['PRICEEACH']
monthly_sales = df.groupby('Month')['Sales'].sum()
best_month = monthly_sales.idxmax()
print("Best Month:", best_month)
print("Sales:", monthly_sales.max())
product_sales = df.groupby('PRODUCTLINE')['QUANTITYORDERED'].sum()
print(product_sales.sort_values(ascending=False))
df['City'] = df['CITY']

city_sales = df.groupby('City')['Sales'].sum()
print(city_sales.sort_values(ascending=False))
from itertools import combinations
from collections import Counter

df_dup = df[df['ORDERNUMBER'].duplicated(keep=False)]

grouped = df_dup.groupby('ORDERNUMBER')['PRODUCTLINE'].apply(list)

count = Counter()

for row in grouped:
    count.update(Counter(combinations(row, 2)))

print(count.most_common(10))
df['Hour'] = df['ORDERDATE'].dt.hour
hourly_sales = df.groupby('Hour')['Sales'].sum()
print(hourly_sales)
avg_order = df['Sales'].mean()
print("Average Order Value:", avg_order)
revenue_product = df.groupby('PRODUCTLINE')['Sales'].sum()
print(revenue_product.sort_values(ascending=False))
monthly_orders = df.groupby('Month')['ORDERNUMBER'].count()
print(monthly_orders)
top_quantity = df.groupby('PRODUCTLINE')['QUANTITYORDERED'].sum().idxmax()
print("Top Quantity Product:", top_quantity)
city_orders = df.groupby('City')['ORDERNUMBER'].count()
print(city_orders.sort_values(ascending=False))
df['Day'] = df['ORDERDATE'].dt.day
print(df.groupby('Day')['Sales'].sum())
df['Weekday'] = df['ORDERDATE'].dt.weekday
print(df.groupby('Weekday')['Sales'].sum())
print(df.loc[df['PRICEEACH'].idxmax()])
print(df.loc[df['PRICEEACH'].idxmin()])
print(df['Sales'].describe())
print(df['PRODUCTLINE'].value_counts())
print(df.groupby(['City','Month'])['Sales'].sum())
print(hourly_sales.idxmax())
print("Total Revenue:", df['Sales'].sum())
print(df[['PRICEEACH','QUANTITYORDERED']].corr())
