#single dim- series object
#multidimensional- Data-frame

import pandas as pd
print(pd.Series([1,2,3,4,5])) #series object using list
print(type(pd.Series([1,2,3,4,5])))
print(pd.Series([1,2,3,4,5], index=['A','B','C','D','E']))

d1=pd.Series({'a':1,'b':2,'c':3,'d':4,'e':5})#series obect as dictionary,#without quotes, a is treated as var NameError: name 'a' is not defined
print(d1)  
print(type(d1)) 

s1=pd.Series([1,2,3,4,5,6,7,8,9])
print(s1[3])
print(s1[-3:])
print(s1[:3])
print(s1[3:])
# print(s1[-3])# return error
print(s1+5) # adding 5 scalar values to 'series' object
s1= pd.Series([10,10,10])
print(s1+5)
s1= pd.Series([10,10,20,20])
print(s1+5)
s1= pd.Series(['A','B','C','D','E'])
print(s1)
# print(s1+5) throws an error
s1= pd.Series([10,20,30,40,50,60,70,80,90])
s2= pd.Series([10,20,30,40,50,60,70,80,90])
print(s1+s2)
print(s1/20) #type will be float

#Data-frame
D1=pd.DataFrame({'Name':['Ankan','Bitan'],'Marks':[100,20]})
print(D1);print(type(D1))
# D1=pd.DataFrame({['Ankan','Bitan'],[100,20]});print(D1) #print(D1) error-unhashable list

# print(pd.read_csv('business-price-statistics.csv'))
csv=pd.read_csv('business-price-statistics.csv')
print(csv.tail(5))
print(csv.shape)
print(csv.describe())
print(csv.iloc[5:11,2:])
print(csv.loc[1:11,('Description')])
print(csv.drop('Description',axis=1))
print(csv.drop([1,2,3],axis=0))
print(csv.mean())
print(csv.median())
print(csv.min())
print(csv.max())

def half(s):
    s*0.5
s=csv[['Revised']].apply(half) # as dtype: object, operation cant be performed.
print(s)

print(csv['Description'].value_counts())

print(csv.sort_values(by='Revised'))