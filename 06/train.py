import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Charger les données
data = pd.read_csv('data.csv')

# Séparer les caractéristiques (X) et la cible (y)
X = data.drop('price', axis=1)
y = data['price']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer le modèle
model = LinearRegression()

# Entraîner le modèle
model.fit(X_train, y_train)

# Sauvegarder le modèle entraîné
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
