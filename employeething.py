import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

dates = pd.date_range(start="2026-01-01", periods=100)
quantities=np.random.randint(1,10,size=100)
base_price=np.random.uniform(15.0,120.0,size=100)
categories = np.random.choice(['Electronics','Appeals', 'Hime','Books'],size=100)

df = pd.DataFrame({
    'Date':dates,
    'Quantity':quantities,
    'UnitPrice':base_price,
    'Category':categories
}

)

df.loc[np.ramon.choice(100,5,replace=False),'UnitPrice']=np.nan
print(df.head())

median_price=df['UnitPrice'].median()
df['UnitPrice']=df['UnitPrice']

df['TotalRevenue']=df['Quantity']*df['UnitPrice']
df['OrderSize']=pd.cut(df['Quantity'],bins=[0,3,6,10],labels=['small','medium','large'])
print(df.head())

category_metrics=df.groupby('Category').agg(
    Total_Revenue=('TotalRevenue','sum'),
    Average_Price=('UnitPrice','mean'),
    Total_Quantity=('Quantity','sum')
).sort_values(by='Total_Revenue',ascending=False)

print(category_metrics)

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Bar Chart showing Revenue per Category
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
ax[0].bar(category_metrics.index, category_metrics['Total_Revenue'], color=colors, edgecolor='black')
ax[0].set_title('Total Revenue Generated per Category', fontsize=12, fontweight='bold')
ax[0].set_xlabel('Product Category')
ax[0].set_ylabel('Revenue ($)')
ax[0].grid(axis='y', linestyle='--', alpha=0.7)

# Subplot 2: Line Plot showing Cumulative Sales over Time
df_time = df.sort_values('Date')
cumulative_revenue = df_time['TotalRevenue'].cumsum()

ax[1].plot(df_time['Date'], cumulative_revenue, color='#9467bd', linewidth=2.5, label='Cumulative Sum')
ax[1].set_title('Cumulative Store Revenue Growth Over Time', fontsize=12, fontweight='bold')
ax[1].set_xlabel('Timeline')
ax[1].set_ylabel('Total Accrued Revenue ($)')
ax[1].tick_params(axis='x', rotation=30)  # Tilt labels so they don't overlap
ax[1].grid(True, linestyle=':', alpha=0.6)
ax[1].legend()

# Prevent overlapping plots and show
plt.tight_layout()
plt.show()