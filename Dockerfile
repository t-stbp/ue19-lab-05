# 1. Partir d'une image Python officielle
FROM python:3

# 2. Définir le dossier de travail dans le conteneur
WORKDIR /usr/src/app

# 3. Copier le fichier des dépendances
COPY requirements.txt ./

# 4. Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier le script Python dans le conteneur
COPY app.py ./

# 6. La commande à exécuter quand le conteneur démarre
CMD [ "python", "./app.py" ]