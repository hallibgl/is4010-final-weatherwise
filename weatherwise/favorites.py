import json
import os

FAV_PATH = "favorites.json"


def load_favorites():
    """Load favorites list from JSON file."""
    if not os.path.exists(FAV_PATH):
        return []

    try:
        with open(FAV_PATH, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_favorites(favs):
    """Save favorites list to JSON file."""
    try:
        with open(FAV_PATH, "w") as f:
            json.dump(favs, f, indent=2)
    except IOError:
        raise Exception("Could not save favorites to file.")


def add_favorite(city):
    """Add a city to favorites."""
    favs = load_favorites()
    if city not in favs:
        favs.append(city)
        save_favorites(favs)
    return favs
