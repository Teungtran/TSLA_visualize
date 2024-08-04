import math 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
# get the stock
df =  pd.read_csv('TSLA.csv',parse_dates = ["Date"], index_col = "Date")
print(df)
# visulize the closeing price
plt.figure(figsize =(16,8))
plt.title('TSLA CLOSE PRICE FROM 2019-2024')
plt.plot(df['Close'],'r')
plt.xlabel('DATE', fontsize = 20)
plt.ylabel('PRICE', fontsize = 22)
plt.show()
#visulize volume
plt.title('TSLA Volume FROM 2019-2024')
fig = df['Volume'].plot(legend = True, kind ='line', xlabel = "Years", ylabel = "Volume").figure
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)   
plt.figure(figsize = (10,5))    
plt.show()  
