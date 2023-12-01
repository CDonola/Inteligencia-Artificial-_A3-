# -*- coding: utf-8 -*-
"""KNN_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mXZDF1TwZhRJNpH7Ea9cfRsJAfIc4YYi
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Carregar o arquivo CSV
data = pd.read_csv('salary_data.csv')

# Visualizar distribuição da variável target ('median_salary')
sns.histplot(data['median_salary'], bins=20, kde=True)
plt.title('Distribuição da Variável Target (median_salary)')
plt.show()

# Separar as features (atributos) e a variável target ('median_salary')
X = data[['wage_span', 'average_salary', 'lowest_salary', 'highest_salary']]
y = data['median_salary']

# Converter dados categóricos em numéricos (se necessário)
X = pd.get_dummies(X, columns=['wage_span'])

# Dividir os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Criar o regressor k-NN
knn_regressor = KNeighborsRegressor(n_neighbors=3)

# Treinar o modelo
knn_regressor.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = knn_regressor.predict(X_test)

# Avaliar o desempenho do modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'R-squared (R2): {r2:.2f}')

# Visualizar as previsões vs. os valores reais
plt.scatter(y_test, y_pred)
plt.xlabel('Valores Reais')
plt.ylabel('Previsões')
plt.title('Previsões vs. Valores Reais')
plt.show()