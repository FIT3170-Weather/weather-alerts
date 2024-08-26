def warning_is_new(warning: dict[str, str | None | dict[str, str | None]],
                   cache: list[dict[str, str | None | dict[str, str | None]]]) -> bool:
    """
    Determine if a warning is new by checking if it exists in the cache.

    :param warning: The current warning to check.
    :param cache: The list of cached warnings.
    :return: True if the warning is new, False otherwise.
    """
    for cached_warning in cache:
        if warning["warning_issue"]["issued"] == cached_warning["warning_issue"]["issued"]:
            return False
    return True


def get_state_name(city: str) -> str | None:
    """
    Get the state name in lower case based on the city name.

    :param city: The city name.
    :return: The state name.
    """
    states = {
        "johor-bahru": "johor",
        "kuala-lumpur": "kuala lumpur",
        "ipoh": "perak",
        "subang-jaya": "selangor",
        "petaling-jaya": "selangor",
        "george-town": "penang",  # TODO: remove this line (not in our list of models)
    }
    return states.get(city)
