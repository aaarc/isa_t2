# -*- coding: utf-8 -*-
"""lvl3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gD0jovpxTbLhJjGivUGZvCfxzIknaZU_
"""

import pandas as pd
import numpy as np

df=pd.read_csv('/content/weatherAUS (1).csv')

df

avgs=df.mean(axis=0)
avgtem_max=avgs['MaxTemp']
avgtem_max=avgs['MinTemp']

print("maximum temp average:",avgtemp)

f=df['Location']=='Cobar'
dd=df.loc[f]

avg2=dd.mean(axis=0)
cobar_m_T=avg2['MaxTemp']

print('avg max temp at cobar is:',cobar_m_T)

z=df['Evaporation']
zz=df['Sunshine']

f2=z.isna()
f3=zz.isna()
f2_a=f2.value_counts()
f3_a=f3.value_counts()

t1=f3_a[True]

t2=f2_a[True]

print('number of Null in sunshine and evaporation is',t1+t2)

#task 3

df

def get_details(a):
  df=pd.read_csv('/content/weatherAUS (1).csv')
  f=df['Location']==a
  dd=df.loc[f]
  print(dd)

get_details('Albury')