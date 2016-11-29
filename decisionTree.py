# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:51:34 2016

@author: kassio
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/JWarmenhoven/ISLR-python/master/Notebooks/Data/Hitters.csv'
df = pd.read_csv(url,index_col=0,parse_dates=[0])
print df.head(5)

# removendo NA da variável 'Salary':
data = df[np.isfinite(df['Salary'])]
data['Salary'] = np.log(data['Salary']) # convertendo para log(salarios)

# subset: Years < 4.5 
A1 = data.query('Years < 4.5')
np.exp(np.mean(A1['Salary']))

# subset: Years > 4.5 
A2 = data.query('Years > 4.5')
B1 = A2.query('Hits < 117.5')
B2 = A2.query('Hits > 117.5')

np.exp(np.mean(B1['Salary']))
np.exp(np.mean(B2['Salary']))

# grafico:
plt.plot(data['Years'], data['Hits'], 'ro')
plt.xlabel('Years')
plt.ylabel('Hits')
plt.annotate('R1', xy=(1, 250), xytext=(1,250), fontsize=20)
plt.annotate('R2', xy=(15, 250), xytext=(15,250), fontsize=20)
plt.annotate('R3', xy=(25,50), xytext=(25,50), fontsize=20)
plt.plot((4.5, 4.5), (0, 300), 'k-', linewidth=3)
plt.plot((4.5, 30), (117.5, 117.5), 'k-',linewidth=3)
