import os
import pandas as pd

csv_file = "sales_data.csv"
if not os.path.exists(csv_file):
    raise FileNotFoundError(f"Required file not found: {csv_file}\nPlease place sales_data.csv in this folder.")

# Load dataset
df = pd.read_csv(csv_file)

# Display first rows
print(df.head())

# Check structure
print(df.info())
# Drop missing values
df = df.dropna()

# Convert columns
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create new columns
df['Month'] = df['Order Date'].dt.month
df['Sales'] = df['Quantity Ordered'] * df['Price Each']
monthly_sales = df.groupby('Month')['Sales'].sum()
best_month = monthly_sales.idxmax()
print("Best Month:", best_month)
print("Sales:", monthly_sales.max())
product_sales = df.groupby('Product')['Quantity Ordered'].sum()
print(product_sales.sort_values(ascending=False))
df['City'] = df['Purchase Address'].apply(lambda x: x.split(',')[1])

city_sales = df.groupby('City')['Sales'].sum()
print(city_sales.sort_values(ascending=False))
from itertools import combinations
from collections import Counter

df_dup = df[df['Order ID'].duplicated(keep=False)]

grouped = df_dup.groupby('Order ID')['Product'].apply(list)

count = Counter()

for row in grouped:
    count.update(Counter(combinations(row, 2)))

print(count.most_common(10))
df['Hour'] = df['Order Date'].dt.hour
hourly_sales = df.groupby('Hour')['Sales'].sum()
print(hourly_sales)
avg_order = df['Sales'].mean()
print("Average Order Value:", avg_order)
revenue_product = df.groupby('Product')['Sales'].sum()
print(revenue_product.sort_values(ascending=False))
monthly_orders = df.groupby('Month')['Order ID'].count()
print(monthly_orders)
top_quantity = df.groupby('Product')['Quantity Ordered'].sum().idxmax()
print("Top Quantity Product:", top_quantity)
city_orders = df.groupby('City')['Order ID'].count()
print(city_orders.sort_values(ascending=False))
df['Day'] = df['Order Date'].dt.day
print(df.groupby('Day')['Sales'].sum())
df['Weekday'] = df['Order Date'].dt.weekday
print(df.groupby('Weekday')['Sales'].sum())
print(df.loc[df['Price Each'].idxmax()])
print(df.loc[df['Price Each'].idxmin()])
print(df['Sales'].describe())
print(df['Product'].value_counts())
print(df.groupby(['City','Month'])['Sales'].sum())
print(hourly_sales.idxmax())
print("Total Revenue:", df['Sales'].sum())
print(df[['Price Each','Quantity Ordered']].corr())
