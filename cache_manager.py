import json

from config import CACHE_FILE


def load_cache() -> list[dict[str, str | None | dict[str, str | None]]]:
    """
    Load cached weather warnings from the file system.

    :return: A list of cached warnings.
    """
    try:
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_cache(data: list[dict[str, str | None | dict[str, str | None]]]) -> None:
    """
    Save weather warnings to the cache.

    :param data: A list of warnings to cache.
    """
    with open(CACHE_FILE, 'w') as f:
        json.dump(data, f)
