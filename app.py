import requests
import sys


def get_quote():
    """
    Interroge l'API Quotable pour une citation aléatoire
    et l'affiche.
    """
    try:
        # L'endpoint pour une citation aléatoire
        url = "https://api.quotable.io/random"
        response = requests.get(url)

        # Lève une exception si le statut HTTP n'est pas 200 (OK)
        response.raise_for_status()

        data = response.json()

        if data and "content" in data and "author" in data:
            print("\n--- Citation du jour ---")
            print(f"\"{data['content']}\"")
            print(f"      - {data['author']}")
            print("--------------------------\n")
        else:
            print("Erreur : Données de l'API mal formatées.", file=sys.stderr)

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion à l'API : {e}", file=sys.stderr)


if __name__ == "__main__":
    get_quote()