import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
plt.figure(figsize=(9,15))
# Select data folder
data_folder = 'data/'
# Created by (Mahmoud Alnabih)
# Created by (Mahmoud Alnabih)

# import folder to pandas dataFarame
file = data_folder+'customer_temp.csv'
df = pd.read_csv(file)


'''
g = sns.FacetGrid(df, row="Education",col='Kidhome')
g.map(sns.boxplot, "MntMeatProducts")
'''
#sns.boxplot(df['MntMeatProducts'],df['Education'])
#sns.violinplot(df['MntMeatProducts'],df['Education'])
#sns.boxplot(df['MntMeatProducts'],df['Education'],hue=df['Kidhome'])

# vLookUp
#df = pd.merge(df,guide)

#pivot table
#n = pd.groupby(['col1','col2'])['values'].agg
#n = pd.pivot_table(index='col',values=['col2'],aggfunc=[])
#n = pd.crosstab(index_col,col_name_col,values_col,aggfunc=[])


# convert to datetime
#n = pd.to_datetime(col1,format='https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes')
# df.resample('https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes').agg
def delete_list(list1,list2):
    temp = list1[:]
    for i in temp:
        if i in list2:
            list1.remove(i)
    return list1

def object_data(column,values):
    print(column.describe())
    if len(column.unique())<=15 :
        col_group = df.groupby([column])[values].agg('count','min','max','mean','std','sum')
        print(col_group)
    
def numeric_detials(column):
    # INPUT: column that you want to analytic it 
    # OUTPUT1: Outlier values in column
    # OUTPUT2: boxplot for column
    print(column.describe())
    col_val = list(column.unique())
    if len(col_val) <=  15:
        print(col_val)
    
    # Outlier values
    q1 = column.quantile(0.25)
    q3 = column.quantile(0.75)
    min_avalable_value = q1-(1.5*(q3-q1))
    max_avalable_value = q3+(1.5*(q3-q1))
    print(f'Range of avalable value is: ({min_avalable_value}) and ({max_avalable_value})')
    high_lier_value = column.loc[column>max_avalable_value].count()
    low_lier_value = column.loc[column<min_avalable_value].count()
    lier_value = high_lier_value + low_lier_value
    print(f'Low lier value is: ({low_lier_value})')
    print(f'High lier value is: ({high_lier_value})')
    print(f'lier value is: ({lier_value})')
    print(sns.boxplot(column))
    input()
    
def check_data(dataFrame,col_count):
    colCount = list(dataFrame.columns)
    for i in colCount:
        print(dataFrame[i].describe())
        if len(dataFrame[i].unique())<=15 and dataFrame[i].dtype == 'object':
            print(dataFrame[i].unique() )
            show_detials = input('Do you want to change this values to numeric values? ANSWER(yes OR no): ')
            if show_detials.upper() in ['YES' ,'Y']:
                pass
                
        time.sleep(1)
    
    #numeric_data = df._get_numeric_data().columns
    #print(len(numeric_data))
#check_data(df,4)
nums = ['NumDealsPurchases', 'NumWebPurchases','NumCatalogPurchases', 
        'NumStorePurchases', 'NumWebVisitsMonth']
for i in df.columns:
    if i in df._get_numeric_data():
        pass
    else:
        pass
''' 
fig , splt = plt.subplots(1,2)

splt[0].boxplot(df['MntFruits'])
splt[1].violinplot(df['NumDealsPurchases'])

'''

def analyze_object(col_names,col_count,percentile={'q25':0.25,'q75':0.75}):
    grps = df.groupby(col_names)[col_count]
    groups = grps.agg(['count','min','max','mean','median','std','sum'])
    for i in percentile:
        groups[i] = grps.quantile(percentile[i])
    print('='*40,'\n',col_names,' | ',col_count,'\n','='*40)
    print(groups)
    fig , object_plot = plt.subplots(2,2)
    object_plot[0,0].pie(grps.count())
    object_plot[0,0].title.set_text('count')
    object_plot[0,1].title.set_text('mean')
    object_plot[1,0].title.set_text('sum')
    object_plot[0,1].pie(grps.mean())
    object_plot[1,0].pie(grps.sum())
    #object_plot[1,1].title.set_text('histogram')
    #object_plot[1,1].hist(df[col_name].sum())

     
    '''

    s = df.groupby(['Education','Marital_Status'])['Income']
    n = df.groupby(['Marital_Status'])['Income'].agg(['mean','std'])
    print(n)
    #object_data(df[i],df['MntFishProducts'])
    '''
#qntile = {'q05':0.05,'q25':0.25,'q75':0.75,'q95':0.95}
#analyze_object(['Education','Marital_Status'],'MntFruits')
'''
del df['Unnamed: 0']
del df['Z_CostContact']
del df['Z_Revenue']
'''
'''
for i in df.columns:
    print(df[i].describe())
    print(df[i].unique())
    input('enter anythiing to next')
'''
#df = pd.Series(df['Education'])
#print(df.columns)
#print(df.loc[(df.ID>6000)|(df.ID == 5700)].rolling(Window=5).mean())
#print(df['Education','Marital_Status'].unique,"mahmoud")


# salary avarege
# min , max salary
# the max job repeat 
# the max buyer in a year
# the max job salaries
# ==== ==== ====
# person buys (data)
# 
'''
avarage = df.NumCatalogPurchases.describe()
n = 0
maxPurchase = df.loc[df.NumCatalogPurchases==df.NumCatalogPurchases.max()].ID
##print(maxPurchase)
##print(n)

for i in range(1850,2011,5):
    fish = df[(df['Year_Birth'] >= i)&(df['Year_Birth']<i+5)].MntFishProducts.mean()
    fishc = df[(df['Year_Birth'] >= i)&(df['Year_Birth']<i+5)].MntFishProducts.count()
    fishs = df[(df['Year_Birth'] >= i)&(df['Year_Birth']<i+5)].MntFishProducts.sum()
    if fish > 0:
        ##print(i,i+5,fishc,fishs,fish)
        pass
print('====================')
tfish = df.MntFishProducts.mean()
##print(tfish)

fish = df.groupby(('Education')and('Year_Birth')).MntFishProducts.count()
##print(fish)

n = df.corr()
##print(n)
fish = df['Education'].value_counts()[:2]
##print(fish)
'''


'''
n = (df[['Education', 'Marital_Status', 'Income', 'Kidhome',
       'Dt_Customer', 'MntWines', 'MntFruits',
       'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts',
       'MntGoldProds', 'NumWebPurchases',
       'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth'
       ]])
#sns.heatmap(n.corr())

'''


'''
##print('mahmoud'.count('m'))
col = ['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Income', 'Kidhome',
       'Teenhome', 'Dt_Customer', 'Recency', 'MntWines', 'MntFruits',
       'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts',
       'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases',
       'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth',
       'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1',
       'AcceptedCmp2', 'Complain', 'Response']

edu = {'Graduation':3 , 'PhD':5, 'Master':4, 'Basic':1, '2n Cycle':2}
myedu = lambda x : edu[x]
df['edu'] = list(map(myedu,df['Education']))

status = ['Single', 'Together', 'Married', 'Divorced', 'Widow', 'Alone', 'Absurd', 'YOLO']

##print('status count is: ',len(status))
imprtant_cols = ['Year_Birth','Education','Marital_Status','Income','Kidhome',
                 'Teenhome','Dt_Customer','Recency']
mounts_cols = ['MntWines', 'MntFruits',
                'MntMeatProducts', 'MntFishProducts',
               'MntSweetProducts','MntGoldProds']
nums = ['NumDealsPurchases', 'NumWebPurchases','NumCatalogPurchases', 
        'NumStorePurchases', 'NumWebVisitsMonth']
accepted = ['AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2']

'''
'''
for i in accepted:
    print(df[i].unique())
    input()
'''


'''
print(df['edu'].unique())
def check(colgroup,cols):
    for i in cols:
        if i[-9:] == 'Products':
            n = i[3:-9]
        else:
            n = i[3:]
        print('\n\n',n,'\n',df[i].groupby(df[colgroup]).agg(['quantile','count','sum','min','max','mean','median','std']))
        

#check('Marital_Status',mounts_cols)

#print(df.describe(include='object'))

##print(df['Marital_Status'].value_counts(normalize=True))
##print(df['Marital_Status'].value_counts())
'''


'''
#n = df.groupby(['edu','Marital_Status'])['Income'].mean()
#n = df.groupby(['Education'])['Marital_Status'].value_counts().unstack().plot.bar()
n = df.groupby(['Education'])['Marital_Status'].value_counts().unstack()
for i in df.columns:
    n = sns.boxplot(df[i])
    print(n)
    n =0
    input()
'''


'''
n = df._get_numeric_data()
print(n.describe)
n = 0
for i in col:
    for j in imprtant_cols:
        if j == i:
            n = 1
            break
    if n == 1:
        col.drop(0)
        n = 0
    
        
print(col)

'''






















