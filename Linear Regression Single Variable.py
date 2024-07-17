import pandas as pd
import numpy as np
from sklearn import linear_model 
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Kshit\Downloads\homeprices.csv')
print(df)


plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,colour='red',markers='+')
