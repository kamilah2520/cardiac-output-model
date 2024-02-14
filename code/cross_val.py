#%% Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error,roc_auc_score
from sklearn.model_selection import cross_val_score, train_test_split

#%% Reading Data
data = pd.read_csv("../Data/DataRepo.csv")
y = data["CO picco"]
df=pd.DataFrame(data)
df["CO picco"] = y
df
# %% Drop unnecessary attributes
X = df.drop(columns=['ID',
                     'Gender',
                     'Eziologia',
                     'Causa interruzione test',
                     'AT',
                     'NYHA',
                     'iAT_',
                     'Unnamed: 77',
                     'Unnamed: 82',
                     'Unnamed: 83',
                     'Unnamed: 84']).fillna(0)
X.corr()
# %% Heatmap data
plt.figure(figsize = (30,27))
sns.heatmap(X[['Age',  
                'Weight',
                'Height',
                'BMI',
                'HR_perc_pred',
                'Polso_peak',
                'HR_peak',
                'CO basale',
                'SV basale',
                'SV picco',
                'PetCO2 @ AT',
                'Pet CO2_ peak',
                'CO picco',
                'CO peak % predetto',
                'Delta SV']].corr(),linewidth=.5,annot=True)
plt.show()
#%%Check Nan values and replace with zeros
y.isnull().values.any()
Y = y.fillna(0)
Y.isnull().values.any()
#%% Pairplot

sns.pairplot(X[['Age',  
                'Weight',
                'Height',
                'BMI',
                'HR_perc_pred',
                'Polso_peak',
                'HR_peak',
                'CO basale',
                'SV basale',
                'SV picco',
                'PetCO2 @ AT',
                'Pet CO2_ peak',
                'CO picco',
                'CO peak % predetto',
                'Delta SV']],diag_kind="kde")

#%%Decision Tree
regr=DecisionTreeRegressor(max_depth=3)
modelo=regr.fit(X,Y)
prediction = modelo.predict(X)
prediction

#%% Visualization of Regression model
fig=plt.figure(figsize=(25,20))
tree.plot_tree(modelo,feature_names=X.columns,filled=True)
plt.show()

#%%Decision Tree Training
Xtrain,Xtest,ytrain,ytest=train_test_split(X,Y,test_size=0.28)
regr=DecisionTreeRegressor(max_depth=3)
scores=cross_val_score(regr,Xtrain,ytrain,cv=10)
scores.mean(), scores.std()

#%%Random Forest
regr2=RandomForestRegressor(max_depth=3,n_estimators=500)
scores=cross_val_score(regr2,Xtrain,ytrain,cv=10)
print(scores.mean()), print(scores.std())
train_stats = Xtrain.describe()
print(train_stats)
