import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("crop-yield-data.xlsx")
#print(df.head())
#print(df.shape)
#print(df.dtypes)

df=df.rename(columns={"Temperatue":"Temperature"})
df=df.rename(columns={"Yeild (Q/acre)":"Yield (Q/acre)"})

# Temperature needs to be converted to float
#print(df['Temperature'].unique())
df = df[df['Temperature'] != ':']
df['Temperature'] = df['Temperature'].astype(float)


#print(df.isnull().sum())

# Replacing nulls with medians
columns = [df.columns]
for col in columns:
    df[col] = df[col].fillna(df[col].median())

#print(df.isnull().sum())

#------EDA-----------------------------

# figure, ax = plt.subplots(1,3,figsize=(15, 5))
# sns.histplot(x = "Rain Fall (mm)", data = df, kde = True, ax = ax[0])
# sns.histplot(x = "Fertilizer", data = df, kde = True, ax = ax[1])
# sns.histplot(x = "Temperature", data = df, kde = True, ax = ax[2])

# figure, ax = plt.subplots(1,3,figsize=(15, 5))
# sns.histplot(x = "Nitrogen (N)", data = df, kde = True, ax = ax[0])
# sns.histplot(x = "Phosphorus (P)", data = df, kde = True, ax = ax[1])
# sns.histplot(x = "Potassium (K)", data = df, kde = True, ax = ax[2])


# figure, ax = plt.subplots(1,3,figsize=(15, 5))
# sns.scatterplot(x = 'Rain Fall (mm)', y = 'Yield (Q/acre)', data = df, ax = ax[0])
# sns.scatterplot(x = 'Fertilizer', y = 'Yield (Q/acre)', data = df, ax = ax[1])
# sns.scatterplot(x = 'Temperature', y = 'Yield (Q/acre)', data = df, ax = ax[2])


# figure, ax = plt.subplots(1,3,figsize=(15, 5))
# sns.regplot(x = 'Nitrogen (N)', y = 'Yield (Q/acre)', data = df, ax = ax[0])
# sns.regplot(x = 'Phosphorus (P)', y = 'Yield (Q/acre)', data = df, ax = ax[1])
# sns.regplot(x = 'Potassium (K)', y = 'Yield (Q/acre)', data = df, ax = ax[2])

plt.figure()
sns.heatmap(df.corr(), annot = True)
plt.show()