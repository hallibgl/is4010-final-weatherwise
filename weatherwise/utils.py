import os


class WeatherError(Exception):
    """Custom exception for weather-related errors."""
    pass


def get_api_key():
    """Retrieve API key from environment variable."""
    key = os.getenv("OPENWEATHER_API_KEY")
    if not key:
        raise WeatherError(
            "Missing API key. Set OPENWEATHER_API_KEY as an environment variable."
        )
    return key
