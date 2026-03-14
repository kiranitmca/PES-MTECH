import pandas as pd

df = pd.read_csv('D:\PES\PES-MTECH\Data\Customer_Churn.csv')

#print(df.head())
#print(df.shape)

df=df.groupby('Churn')['tenure'].mean()
print(df)

