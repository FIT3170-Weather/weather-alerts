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
