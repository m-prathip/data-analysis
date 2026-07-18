import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_performance.csv")
df.info()
df.describe()
df.head()
df.isnull().sum()
print(df['Sales'].sum())
category = df.groupby("Category")["Sales"].sum()
print(category)
top = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
print(top)
df['Order Date'] = pd.to_datetime(df['Order Date'])

monthly = df.groupby(df['Order Date'].dt.month)['Sales'].sum()
monthly.plot(kind='line')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
state = df.groupby("State")["Profit"].sum()

state.sort_values().tail(10).plot(kind='bar')
plt.show()