import argparse
from colorama import Fore, Style
from .api import fetch_current_weather, fetch_forecast
from .favorites import add_favorite, load_favorites
from .utils import WeatherError


def display_current(data):
    name = data["name"]
    temp = data["main"]["temp"]
    cond = data["weather"][0]["description"]

    print(Fore.CYAN + f"\nCurrent Weather in {name}" + Style.RESET_ALL)
    print(f"Temperature: {temp}°F")
    print(f"Conditions: {cond}\n")


def display_forecast(data):
    print(Fore.GREEN + "\n5-Day Forecast" + Style.RESET_ALL)

    for entry in data["list"][:5]:
        dt = entry["dt_txt"]
        temp = entry["main"]["temp"]
        cond = entry["weather"][0]["description"]
        print(f"{dt}: {temp}°F — {cond}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="WeatherWise — Command-line Weather Dashboard"
    )

    subparsers = parser.add_subparsers(dest="command")

    # CURRENT
    current_cmd = subparsers.add_parser("current")
    current_cmd.add_argument("city", type=str)

    # FORECAST
    forecast_cmd = subparsers.add_parser("forecast")
    forecast_cmd.add_argument("city", type=str)

    # ADD FAVORITE
    fav_add = subparsers.add_parser("fav-add")
    fav_add.add_argument("city", type=str)

    # LIST FAVORITES
    subparsers.add_parser("fav-list")

    args = parser.parse_args()

    try:
        if args.command == "current":
            data = fetch_current_weather(args.city)
            display_current(data)

        elif args.command == "forecast":
            data = fetch_forecast(args.city)
            display_forecast(data)

        elif args.command == "fav-add":
            favs = add_favorite(args.city)
            print(f"\nAdded! Favorites now: {favs}\n")

        elif args.command == "fav-list":
            favs = load_favorites()
            print("\nFavorite Cities:")
            for c in favs:
                print("-", c)
            print()

        else:
            parser.print_help()

    except WeatherError as e:
        print(Fore.RED + f"\nError: {e}\n" + Style.RESET_ALL)