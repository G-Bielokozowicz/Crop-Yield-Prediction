import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("crop-yield-data.xlsx")
#print(df.head())
#print(df.shape)
#print(df.dtypes)

df=df.rename(columns={"Temperatue":"Temperature"})

# Temperature needs to be converted to float
#print(df['Temperature'].unique())
df = df[df['Temperature'] != ':']
df['Temperature'] = df['Temperature'].astype(float)


print(df.isnull().sum())

# Replacing nulls with medians

columns = [df.columns]
for col in columns:
    df[col] = df[col].fillna(df[col].median())

print(df.isnull().sum())