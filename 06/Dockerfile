# Utiliser une image de base Python
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans l'image
COPY requirements.txt .
COPY app.py .
COPY train.py .
COPY data.csv .
COPY model.pkl .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exécuter le script d'entraînement pour générer le modèle
RUN python train.py

# Exposer le port sur lequel l'application Flask sera disponible
EXPOSE 5000

# Démarrer l'application Flask
CMD ["python", "app.py"]
