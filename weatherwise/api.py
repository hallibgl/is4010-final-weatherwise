import requests
from .utils import WeatherError, get_api_key

BASE_URL = "https://api.openweathermap.org/data/2.5"


def fetch_current_weather(city):
    """Fetch current weather for a given city."""
    api_key = get_api_key()

    params = {"q": city, "appid": api_key, "units": "imperial"}

    try:
        response = requests.get(f"{BASE_URL}/weather", params=params, timeout=5)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException:
        raise WeatherError("Network error while fetching current weather.")
    except ValueError:
        raise WeatherError("Invalid response received from API.")


def fetch_forecast(city):
    """Fetch 5-day forecast."""
    api_key = get_api_key()

    params = {"q": city, "appid": api_key, "units": "imperial"}

    try:
        response = requests.get(f"{BASE_URL}/forecast", params=params, timeout=5)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException:
        raise WeatherError("Network error while fetching forecast.")
    except ValueError:
        raise WeatherError("Invalid response received from API.")
