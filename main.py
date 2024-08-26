import time

from api_client import fetch_weather_warnings, fetch_subscribed_users
from cache_manager import load_cache, save_cache
from config import CHECK_INTERVAL
from email_sender import send_email
from utils import warning_is_new, get_state_name


def main() -> None:
    """
    Main function to periodically check weather warnings and notify users.
    """
    while True:
        print("Checking for new weather warnings...")
        warnings = fetch_weather_warnings()
        cache = load_cache()

        new_warnings = [w for w in warnings if warning_is_new(w, cache)]

        if new_warnings:
            print(f"Found {len(new_warnings)} new warnings.")
            subscribed_users = fetch_subscribed_users().get('data', [])
            for warning in new_warnings:
                for email, cities in subscribed_users:
                    if any(get_state_name(city.lower()).lower() in warning['text_en'].lower() for city in cities):
                        send_email(
                            to_email=email,
                            subject=f"CliMate Warning: {warning['heading_en']}",
                            body=warning['text_en']
                        )
            save_cache(warnings)
        else:
            print("No new warnings.")

        print(f"Sleeping for {CHECK_INTERVAL} seconds...")
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
