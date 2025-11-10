# ue19-lab-05 : Générateur de Citations

Cette application Python interroge l'API publique [Quotable](https://api.quotable.io/) pour récupérer une citation aléatoire et l'afficher dans la console.

Le projet est conçu pour être exécuté dans un conteneur Docker.

## Comment l'installer et le lancer (How-to)

Vous devez avoir Docker d'installé sur votre machine.

1.  **Clonez ce dépôt :**
    ```bash
    git clone [https://github.com/t-stbp/ue19-lab-05.git](https://github.com/t-stbp/ue19-lab-05.git)
    cd ue19-lab-05
    ```

2.  **Construisez l'image Docker :**
    Cette commande lit le `Dockerfile` et crée une image locale nommée `app-citation`.
    ```bash
    docker build -t app-citation .
    ```

3.  **Lancez le conteneur :**
    Cette commande exécute l'image `app-citation`. L'option `--rm` nettoie et supprime le conteneur après son exécution.
    ```bash
    docker run --rm app-citation
    ```

Une citation devrait alors s'afficher dans votre terminal.