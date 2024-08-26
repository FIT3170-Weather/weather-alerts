import requests

from config import WEATHER_API_URL, SUBSCRIPTIONS_API_URL


def fetch_weather_warnings(limit: int = 1) -> list[dict[str, str | None | dict[str, str | None]]]:
    """
    Fetch weather warnings from the weather API.

    :param limit: The number of warnings to fetch.
    :return: A list of warnings.
    """
    response = requests.get(f"{WEATHER_API_URL}?limit={limit}")
    response.raise_for_status()
    return response.json()


def fetch_subscribed_users() -> dict[str, list[list[str, list[str]]] | bool]:
    """
    Fetch users and their city subscriptions from the subscription API.

    :return: A dictionary containing user email and their subscribed cities.
    """
    response = requests.get(SUBSCRIPTIONS_API_URL)
    response.raise_for_status()
    return response.json()
