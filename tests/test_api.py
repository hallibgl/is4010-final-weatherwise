import pytest
from weatherwise.api import fetch_current_weather
from weatherwise.utils import WeatherError

def test_bad_city_name():
    with pytest.raises(WeatherError):
        fetch_current_weather("CITY_NAME_THAT_DOES_NOT_EXIST_123456")
