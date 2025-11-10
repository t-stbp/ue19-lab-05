# ue19-lab-05 : Générateur d'Activités

Cette application Python interroge l'API publique "Bored API" (version App Brewery) pour récupérer une activité aléatoire et l'afficher dans la console.

Le projet est conçu pour être exécuté dans un conteneur Docker.

## Comment l'installer et le lancer (How-to)

Vous devez avoir Docker d'installé sur votre machine.

1.  **Clonez ce dépôt :**
    ```bash
    git clone [https://github.com/t-stbp/ue19-lab-05.git](https://github.com/t-stbp/ue19-lab-05.git)
    cd ue19-lab-05
    ```

2.  **Construisez l'image Docker :**
    Cette commande lit le `Dockerfile` et crée une image locale nommée `app-activite`.
    ```bash
    docker build -t app-activite .
    ```

3.  **Lancez le conteneur :**
    Cette commande exécute l'image `app-activite`. L'option `--rm` nettoie et supprime le conteneur après son exécution.
    ```bash
    docker run --rm app-activite
    ```

Une idée d'activité devrait alors s'afficher dans votre terminal.