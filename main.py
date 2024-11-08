import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

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

# plt.figure()
# sns.heatmap(df.corr(), annot = True)
# plt.show()

# --------------------------------------------------------------------------------

# Creating train/test split
X_train, X_test, y_train, y_test = train_test_split(df.drop('Yield (Q/acre)', axis = 1), df['Yield (Q/acre)'], test_size = 0.2)

rfr = RandomForestRegressor()
# Parameters for grid search
# parameters = {
#     "n_estimators": [100,200,300],
#     "min_samples_split": [2,4,6,8],
#     "min_samples_leaf": [2,4,6,8],
#     "random_state": [0,42],
#     "max_depth": [2,4,6,8],
# }

# grid = GridSearchCV(rfr, parameters, cv = 5, n_jobs = -1, verbose = 1)
# grid.fit(X_train, y_train)
# print(grid.best_params_) # {'max_depth': 8, 'min_samples_leaf': 2, 'min_samples_split': 2, 'n_estimators': 300, 'random_state': 42}

best_rfr = RandomForestRegressor(max_depth=4, min_samples_leaf=2, min_samples_split=6,n_estimators=100, random_state=42)
best_rfr.fit(X_train, y_train)
print(best_rfr.score(X_train, y_train))


