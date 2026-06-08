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