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

# df1 = pd.read_csv(r'D:\PES\PES-MTECH\Data\lds1.csv')

# df1 = df1.Sector.replace({'Pub':'Public','Prvt':'Private'}) # replace values in 'Sector' column
# print(df1)


# Plotting of data 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df1= pd.read_csv(r'D:\PES\PES-MTECH\Data\lds41.csv')
print(df1.shape)

# Line Plot 


# x1 = np.arange(1,6)
# y1=x1*2
# y2 = x1 ** 2
# plt.plot(x1,y1, label='y=2x', marker='o',linestyle='--',color='red')
# plt.plot(x1,y2, label='y=x^2', marker='o',linestyle='--',color='blue')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')    
# plt.title('Line Plot')
# print(plt.gcf())
# plt.legend()
# plt.xticks(np.linspace(1,5,10))
# plt.yticks(np.linspace(-6,25,13))
# plt.show()

# plt.plot(x1,y1,marker="*",linestyle='-',color='green',label='y=2x')
# plt.text(x=3,y=6,s='Linear Plot', fontsize=15, color='green')
# for xc,yc in list(zip(x1,y1)):
#     plt.text(x=xc,y=yc,s=f'({xc},{yc})', fontsize=10, color='red')
# #plt.show()

# df1.sort_values(by='wt', inplace=True)
# plt.plot(df1.wt, df1.mpg, marker='o', linestyle='-', color='purple')
# plt.xlabel('weight')       
# plt.ylabel('mpg')
# plt.title('Weight vs MPG')
# plt.show()
# print(df1)

print(df1.wt.mean())

# Scatter Plot


# x1 = np.arange(1,6)
# y1 = x1*2 #+ np.random.normal(0,2,size=5)
# plt.scatter(x1,y1, label='y=2x with noise', marker='o',color='orange')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Scatter Plot')
# plt.legend()
# plt.xticks(np.linspace(1,5,10))
# plt.yticks(np.linspace(0,12,13))
# plt.show()


# plt.scatter(df1.gear, df1.mpg,  s= df1.cyl*10,c=df1.am+10)
# plt.xlabel('Gear')
# plt.ylabel('MPG')   
# plt.title('Gear vs MPG')
# #plt.colorbar(label='AM')
# plt.show()

# Pie Plot

vc = df1.gear.value_counts()
print(vc)
# plt.pie(vc, labels=vc.index, autopct='%1.1f%%')
# plt.title('Distribution of Gears')
# plt.show()

# vc.plot(kind='pie', autopct='%1.1f%%')
# plt.title('Distribution of Gears')
# plt.show()

# vc = df1.carb.value_counts()
# print(vc)
# plt.pie(x=vc.values, labels=vc.index, autopct='%1.1f%%')
# plt.title('Distribution of Carburetors')
# plt.show()

# Explode wedge

# vc = df1.carb.value_counts()
# plt.pie(x=vc.values, labels=vc.index, autopct='%1.1f%%',radius=1, explode=[0.1 if i==4 else 0 for i in vc.index])
# plt.title('Distribution of Carburetors')
# plt.show()

# Histogram


# np.random.seed(23)
# n100=np.random.randint(low=0,high=101,size=100)
# plt.xticks(np.linspace(n100.min(), n100.max(), 11))
# count,bins,patches=plt.hist(n100, bins=10, edgecolor='black',rwidth=0.9,facecolor='cyan',align='mid')
# colors = plt.cm.tab10(np.arange(len(patches)))  # tab10 colormap
# for patch, color in zip(patches, colors):
#     patch.set_facecolor(color)
# plt.show()

# Bar Chart

# c1count = ['Tata','Birla','Wipro','Infosys','HCL']
# e1count = [200,100,300,400,250]
# e2count = [150,80,250,350,200]
# #plt.bar(c1count,height=e1count)
# plt.bar(c1count,height=e2count, bottom=e1count, color='orange')
# plt.show()

# c1count = ['Tata','Birla','Wipro','Infosys','HCL']
# e1count = [200,100,300,400,250]
# e2count = [150,80,250,350,200]
# #plt.bar(c1count,height=e1count)
# xpos = np.arange(len(c1count))
# plt.bar(xpos, height=e1count, width=0.4, label='E1', color='blue')
# plt.bar(xpos+0.4, height=e2count, width=0.4, label='E2', color='orange')
# plt.xticks(xpos + 0.2, c1count)
#plt.show()

# plt.bar(x=df1.model, height=df1.mpg, color='grey')
# #plt.xticks(rotation=90)
# plt.xlabel('Model') 
# plt.ylabel('MPG')
# plt.title('Model vs MPG')
# plt.xticks(rotation=75)
# plt.show()

# Box Plot

# v1 = list(range(200,300))
# v1.append(10)
# v1.append(20)
# v1.append(400)
# #plt.boxplot(x=v1,orientation='horizontal')
# plt.boxplot([df1.hp,df1.disp])
# plt.show()

# sns.boxplot(data=df1,x='hp')
# plt.show()

# df1.mpg.plot(kind='kde')
# plt.show()

# sns.violinplot(data=df1,x='cyl',y='mpg')
# plt.show()

# sns.boxenplot(data=df1,x='cyl',y='mpg')
# plt.show()


# x = 10
# def mf1():
#     x=x+20
# mf1()

for i in range(3):
    for j in range(3):
        if i==j:
            break
        print(i,j)