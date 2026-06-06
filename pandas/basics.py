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
#print(df_csv.head())

#print(pd.__version__)

#df_csv.info()
#print(df_csv.describe(include='object'))
#print(df_csv.head())
#df_csv.to_csv(r'D:\PES\PES-MTECH\Data\output_lds1.csv', index=True)

# df_csv_read = pd.read_csv(r'D:\PES\PES-MTECH\Data\output_lds1.csv',index_col=0)
# print(df_csv_read.head())

# DIY zipfile , xml module to read and write data in zip and xml formats respectively.


# Access data from dataframe
'''
Direct access 
integer location based access
label based access

df_csv['column_name'] or df_csv.column_name # direct access
df_csv[['column1','column2']] # direct access multiple columns
df_csv['starting_row_index': 'ending_row_index', 'step'] # direct access rows

df_csv.iloc[row_index, column_index] # integer location based access
df_csv.loc[row_label, column_label] # label based access
'''
#print(df_csv[['Rev','Exp','Vol']])

#print(df_csv.iloc[2:5, 2:7])
#print(df_csv.iloc[[1,-1,2,-2]])

#print(df_csv.iloc[[0,1,4,-2,-1], [2,3,-1]])

# Lable based access
#print(df_csv.loc[0:5, 'Rev':'Vol'])
#print(df_csv.index)
# print(df_csv.loc['Kolkata_FMCG' : 'NCR_Leagles'])
# print(df_csv.loc[['Kolkata_FMCG' , 'NCR_Leagles']])

# Conditional access

#print(df_csv.Sector.value_counts())
# mask1 = df_csv.Sector == 'Pub'
# print(mask1)

# df_cond = df_csv[(df_csv.Sector == 'Pub') & (df_csv.GST == 'Goods')] # conditional access with multiple conditions
# print(df_cond)

# df_avg =  df_csv[df_csv.Rev > df_csv.Rev.mean()] # conditional access with mean value
# print(df_avg)

# df_show = df_csv[df_csv.Rev > df_csv.Rev.mean()].loc[:,['Vol', 'Exp','HQ']]
# print(df_show)

# Sorting data 

# df_csv_sorted= df_csv.sort_index(axis=0, ascending=True,inplace=False) # sort by index in descending order

# print(df_csv_sorted.head())

# df_csv_sorted1= df_csv.sort_index(axis=1, ascending=True,inplace=False)
# print(df_csv_sorted1.head())

# df_csv_sorted2= df_csv.sort_values(by=['Vol','Rev'], ascending=(True,False),inplace=False) # sort by column values in descending order
# print(df_csv_sorted2)

#print(df_csv.select_dtypes(include='Int64').head()) # select only integer columns

#print(df_csv.select_dtypes(include=['Int64']))

# def keycheck(series):
#     print(type(series))
#     print(series)
#     return series.apply(lambda x: len(str(x)))
# df_csv_sorted3 = df_csv.sort_values(by='Deccan_Sporting', axis=1, ascending=False, inplace=False,key=keycheck) # sort by column values in descending order
# print(df_csv_sorted3)


# df_csv['df_csv_vrankavg'] = df_csv.Vol.rank(method='average',  ascending=True,axis=0)
#df_csv['df_csv_vrankdense'] = df_csv.rank(method='dense', numeric_only=True, ascending=False)
# print(df_csv)

# Rename of Labels

# df_ranme_csv=df_csv.rename(columns={'Vol':'Sales','Sector':'Group'},
#               index={'Kolkata_FMCG':'Palmolive','Bombay_Finance':'NSE','Bangalore_Breweries':'UB'},inplace=False)
# print(df_ranme_csv)

#Concatination of dataframes

# df_csv11 = pd.read_csv(r'D:\PES\PES-MTECH\Data\lds11.csv')
# df_csv12 = pd.read_csv(r'D:\PES\PES-MTECH\Data\lds12.csv')
# df_csv13 = pd.read_csv(r'D:\PES\PES-MTECH\Data\lds13.csv')

# #print(df_csv11,df_csv12,df_csv13)
# df_concatenated = pd.concat([df_csv11, df_csv12, df_csv13], axis=1,join='inner' ,keys=['Dataset1', 'Dataset2', 'Dataset3']) # concatination of dataframes along rows
# print(df_concatenated)

# Merging of dataframes

df_csv21 = pd.read_csv(r'D:\PES\PES-MTECH\Data\lds21.csv')
df_csv22= pd.read_csv(r'D:\PES\PES-MTECH\Data\lds22.csv')
df_csv23 = pd.read_csv(r'D:\PES\PES-MTECH\Data\lds23.csv')
# print(df_csv21);
# print(df_csv22);
#print(df_csv23);

# df_merged = pd.merge(df_csv21, df_csv22,how='cross' , on=None, indicator=True) # merging of dataframes on common column 'ID' with inner join
# print(df_merged)

# df_merged1 = pd.merge(df_csv21, df_csv22, how='inner', left_on='stock_id',right_on='stock_name', indicator=True) # merging of dataframes on common column 'ID' with inner join
# print(df_merged1)

# df_merged1 = pd.merge(df_csv21, df_csv22, how='inner', left_index=True,right_index=True, indicator=True) # merging of dataframes on common column 'ID' with inner join
# print(df_merged1)

# Duplicate Observations Handling
df_dup = pd.read_csv(r'D:\PES\PES-MTECH\Data\lds33.csv')
#df_dup=df_dup.duplicated(subset=None,keep='last') # check for duplicate rows
# print(df_dup)
#df_dup= df_dup.duplicated(subset=['City','Temperature'], keep='first') # check for duplicate rows based on specific columns
# df_dropped = df_dup.drop_duplicates(subset=['City','Temperature'], keep='last') # drop duplicate rows based on specific columns
# print(df_dropped)

# NaN values handling
df_nan = pd.read_csv(r'D:\PES\PES-MTECH\Data\lds0.csv')
#print(df_nan.isna().sum().sum()) # check for NaN values in each column
#df_nan.rev = df_nan.Rev.fillna(df_nan.Rev.mean()) # fill NaN values in 'Rev' column with mean value
#print(df_nan)
# df_nan = df_nan.Sector.ffill() # fill NaN values in 'Sector' column with forward fill method
# print(df_nan)

# Stack and Unstack
# import numpy as np
# np.random.seed(23)
# n84 = np.random.randint(low=10,high=100,size=(8,4))
# col_0_labels = [2022,2023]
# col_1_labels =['Q1','Q2']
# row_0_labels = ['Tata','Birla','Wipro','Infosys']
# row_1_labels = ['FMCG','Tech']
# col_Lables = pd.MultiIndex.from_product([col_0_labels,col_1_labels])
# row_Lables = pd.MultiIndex.from_product([row_0_labels,row_1_labels])
# df_multi = pd.DataFrame(n84, index=row_Lables, columns=col_Lables)
# df_multi_stacked = df_multi.stack(level=0) # stack the dataframe
# df_multi_unstacked = df_multi_stacked.unstack(level=0).stack(level=0).unstack(level=1) # unstack the dataframe
# print(df_multi_unstacked)


# Replace of Values

df1 = pd.read_csv(r'D:\PES\PES-MTECH\Data\lds1.csv')

df1 = df1.Sector.replace({'Pub':'Public','Prvt':'Private'}) # replace values in 'Sector' column
print(df1)


