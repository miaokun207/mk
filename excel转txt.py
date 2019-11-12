import pandas as pd
df=pd.read_excel('1.xlsx',header=None)
df.to_csv('2.txt',header=None,sep=',',index=False)