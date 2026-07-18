import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_performance.csv")
df['Order Date'] = pd.to_datetime(df['Order_Date'] if 'Order_Date' in df.columns else df['Order Date'])

# 1. Sales Chart: Monthly Sales
monthly = df.groupby(df['Order Date'].dt.month)['Sales'].sum()
plt.figure(figsize=(10, 6))
monthly.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.savefig('sales_chart.png', bbox_inches='tight')
plt.close()

# 2. Profit Chart: Top 10 States by Profit
state = df.groupby("State")["Profit"].sum().sort_values().tail(10)
plt.figure(figsize=(10, 6))
state.plot(kind='bar', color='skyblue')
plt.title("Top 10 States by Profit")
plt.xlabel("State")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.savefig('profit_chart.png', bbox_inches='tight')
plt.close()

print("Charts generated: sales_chart.png and profit_chart.png")
