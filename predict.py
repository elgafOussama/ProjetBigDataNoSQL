#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:54:15 2019

@author: mehdi olivier oussama fabien
"""

from sklearn.externals import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.preprocessing import MaxAbsScaler



# load the model from disk
model = joblib.load('predict')
data_clients = pd.read_csv('datasetOut.csv')
#

data_clients = data_clients.drop(data_clients.columns[data_clients.columns.str.contains('unnamed',case = False)],axis = 1)
dataset = data_clients.drop(data_clients.columns[data_clients.columns.str.contains('unnamed',case = False)],axis = 1)

data_clients.NAME_TYPE_SUITE = data_clients.NAME_TYPE_SUITE.astype(str)
data_clients.NAME_INCOME_TYPE = data_clients.NAME_INCOME_TYPE.astype(str)
data_clients.OCCUPATION_TYPE = data_clients.OCCUPATION_TYPE.astype(str)

labelencoder = LabelEncoder()
data_clients.NAME_CONTRACT_TYPE = labelencoder.fit_transform(data_clients.NAME_CONTRACT_TYPE)
data_clients.FLAG_OWN_CAR = labelencoder.fit_transform(data_clients.FLAG_OWN_CAR)
data_clients.CODE_GENDER = labelencoder.fit_transform(data_clients.CODE_GENDER)
data_clients.FLAG_OWN_CAR = labelencoder.fit_transform(data_clients.FLAG_OWN_CAR)
data_clients.FLAG_OWN_REALTY = labelencoder.fit_transform(data_clients.FLAG_OWN_REALTY)
data_clients.NAME_TYPE_SUITE = labelencoder.fit_transform(data_clients.NAME_TYPE_SUITE)
data_clients.NAME_INCOME_TYPE = labelencoder.fit_transform(data_clients.NAME_INCOME_TYPE)
data_clients.NAME_EDUCATION_TYPE =labelencoder.fit_transform(data_clients.NAME_EDUCATION_TYPE)
data_clients.NAME_FAMILY_STATUS =labelencoder.fit_transform(data_clients.NAME_FAMILY_STATUS)
data_clients.NAME_HOUSING_TYPE =labelencoder.fit_transform(data_clients.NAME_HOUSING_TYPE)
data_clients.OCCUPATION_TYPE =labelencoder.fit_transform(data_clients.OCCUPATION_TYPE)
data_clients.WEEKDAY_APPR_PROCESS_START = labelencoder.fit_transform(data_clients.WEEKDAY_APPR_PROCESS_START)
data_clients.ORGANIZATION_TYPE = labelencoder.fit_transform(data_clients.ORGANIZATION_TYPE)


scaler_maxabs = MaxAbsScaler()
data = scaler_maxabs.fit_transform(data_clients)
X_train = PCA(n_components=40).fit_transform(data)

resultat =  model.predict(X_train)

dataset['TARGET_p'] =  resultat.tolist()
    
dataset.to_csv('predict.csv')