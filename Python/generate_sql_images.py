import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../Dataset/Superstore.csv")

def render_mpl_table(data, filename, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')
    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in mpl_table._cells.items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0] % len(row_colors) ])
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

import numpy as np

# 1. Region Sales & Profit
region_df = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
region_df.rename(columns={'Sales': 'Total_Sales', 'Profit': 'Total_Profit'}, inplace=True)
region_df = region_df.round(2)
render_mpl_table(region_df, '../Images/sql_region.png')

# 2. Segment Average Discount
segment_df = df.groupby('Segment')['Discount'].mean().reset_index()
segment_df.rename(columns={'Discount': 'Average_Discount'}, inplace=True)
segment_df = segment_df.round(3)
render_mpl_table(segment_df, '../Images/sql_segment.png')

# 3. Top Customers by Orders
# Count number of orders per customer (could be rows or unique order ids, let's assume unique Order IDs)
if 'Order ID' in df.columns or 'Order_ID' in df.columns:
    order_col = 'Order ID' if 'Order ID' in df.columns else 'Order_ID'
    customer_col = 'Customer Name' if 'Customer Name' in df.columns else 'Customer_Name'
    customer_df = df.groupby(customer_col)[order_col].nunique().reset_index()
    customer_df.rename(columns={order_col: 'Total_Orders'}, inplace=True)
    customer_df = customer_df.sort_values(by='Total_Orders', ascending=False).head(10)
    render_mpl_table(customer_df, '../Images/sql_customers.png')

print("SQL Table images generated successfully.")
