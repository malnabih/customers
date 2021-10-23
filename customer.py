# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 07:07:13 2021

@author: hp
"""
data_folder = 'data/'
import pandas as pd

df = pd.read_csv(data_folder+'customer_.csv')
del df['Unnamed: 0']
del df['Z_CostContact']
del df['Z_Revenue']

'''
for i in df.columns:
    print(df[i].describe())
    print(df[i].unique())
    input('enter anythiing to next')
'''
#df = pd.Series(df['Education'])
print(df.columns)
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
avarage = df.NumCatalogPurchases.describe()
n = 0
maxPurchase = df.loc[df.NumCatalogPurchases==df.NumCatalogPurchases.max()].ID
print(maxPurchase)
print(n)

for i in range(1850,2011,5):
    fish = df[(df['Year_Birth'] >= i)&(df['Year_Birth']<i+5)].MntFishProducts.mean()
    fishc = df[(df['Year_Birth'] >= i)&(df['Year_Birth']<i+5)].MntFishProducts.count()
    fishs = df[(df['Year_Birth'] >= i)&(df['Year_Birth']<i+5)].MntFishProducts.sum()
    if fish > 0:
        print(i,i+5,fishc,fishs,fish)
print('====================')
tfish = df.MntFishProducts.mean()
print(tfish)

fish = df.groupby(('Education')and('Year_Birth')).MntFishProducts.count()
print(fish)

n = df.corr()
print(n)
fish = df['Education'].value_counts()[:2]
print(fish)




DESKTOP-NBKQB4M MINGW64 /e/python/projects/data analysis/01 customers (master)















