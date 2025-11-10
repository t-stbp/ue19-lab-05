import requests
import sys


def get_activity():
    """
    Interroge l' API BoredAPI pour une activité aléatoire
    et l'affiche.
    """
    try:
        # La nouvelle URL qui fonctionne :
        url = "https://bored-api.appbrewery.com/random"
        response = requests.get(url)

        # Lève une exception si le statut HTTP n'est pas 200 (OK)
        response.raise_for_status()

        data = response.json()

        # La structure du JSON est la même, "activity" est la clé
        if data and "activity" in data:
            print("\n--- Idée d'activité ---")
            print(f"{data['activity']}.")
            print("-------------------------\n")
        else:
            print("Erreur : Données de l'API mal formatées.", file=sys.stderr)

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion à l'API : {e}", file=sys.stderr)


if __name__ == "__main__":
    get_activity()