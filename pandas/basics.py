import pandas as pd
m1= [200,100,300,400,250]
labels = ['Tata','Birla','Wipro','Infosys','HCL']
ps1= pd.Series(m1, index=labels)
#print(ps1)

md1= {'Tata':200, 'Birla':100, 'Wipro':300, 'Infosys':400, 'HCL':250}
# ps2= pd.Series(md1) 
# print(ps2)
# print(ps2.count())
# print(ps2.shape)
# print(ps2.value_counts())

m43 =[
[10,5,'Mumbai'],
[20,15,'Kolkata'],
[30,25,'Bangalore'],
[40,33,'Bangalore']
]
df = pd.DataFrame(m43)
# print(df.columns)
# print(df.ndim)

row_lables =['Tata','Birla','Wipro','Infosys']
# column_lables = ['Revenue','Expenses','City']
# df1 = pd.DataFrame(m43, index=row_lables, columns=column_lables)
# print(df1)


md2= {
    'Revenue':[10,20,30,40],
    'Expenses':[5,15,25,33],
    'City':['Mumbai','Kolkata','Bangalore','Bangalore']
}
df2 = pd.DataFrame(md2,index=row_lables)
#print(df2)

df_csv = pd.read_csv(r'D:\PES\PES-MTECH\Data\lds1.csv')
print(df_csv)