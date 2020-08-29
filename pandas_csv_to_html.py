#Data Munging
import pandas as pd 
s=pd.read_csv('business-price-statistics.csv',index_col=0) #index_col=0 makes no index present in this
s.to_html('business-price-statistics.html')