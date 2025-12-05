import os
import pytest
from weatherwise.utils import get_api_key, WeatherError


def test_missing_api_key(monkeypatch):
    monkeypatch.delenv("OPENWEATHER_API_KEY", raising=False)
    with pytest.raises(WeatherError):
        get_api_key()


def test_api_key_present(monkeypatch):
    monkeypatch.setenv("OPENWEATHER_API_KEY", "TEST123")
    assert get_api_key() == "TEST123"
