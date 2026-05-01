"""
SWAPI + DTO + Questionary
+ Functional Programming (map, filter)
+ Early Returns + Dispatch Pattern
"""

import requests
import questionary
from rich.console import Console
from rich.table import Table

console = Console()


# --- DTO ---
class CharacterDTO:
    def __init__(self, name, height, gender):
        self.name = name
        self.height = height
        self.gender = gender


class PlanetDTO:
    def __init__(self, name, climate, population):
        self.name = name
        self.climate = climate
        self.population = population


# --- Functional Helpers ---
def to_character_dto(item):
    return CharacterDTO(
        item.get("name"),
        item.get("height"),
        item.get("gender")
    )


def to_planet_dto(item):
    return PlanetDTO(
        item.get("name"),
        item.get("climate"),
        item.get("population")
    )


def is_known_height(c):
    return c.height != "unknown"


def is_populated(p):
    return (
        p.population != "unknown"
        and p.population.isdigit()
        and int(p.population) > 0
    )


# --- Service ---
class StarWarsService:
    BASE_URL = "https://swapi.py4e.com/api"

    def search_characters(self, name):
        data = requests.get(f"{self.BASE_URL}/people/?search={name}").json()

        chars = list(map(to_character_dto, data["results"]))
        chars = list(filter(is_known_height, chars))

        return chars

    def search_planets(self, name):
        data = requests.get(f"{self.BASE_URL}/planets/?search={name}").json()

        planets = list(map(to_planet_dto, data["results"]))
        planets = list(filter(is_populated, planets))

        return planets


# --- UI ---
def show_characters(chars):
    table = Table(title="Characters")
    table.add_column("Name")
    table.add_column("Height")
    table.add_column("Gender")

    for c in chars:
        table.add_row(c.name, str(c.height), c.gender)

    console.print(table)


def show_planets(planets):
    table = Table(title="Planets")
    table.add_column("Name")
    table.add_column("Climate")
    table.add_column("Population")

    for p in planets:
        table.add_row(p.name, p.climate, str(p.population))

    console.print(table)


# --- Handlers (Early Return style) ---
def handle_search_character(service):
    name = questionary.text("Enter character name:").ask()
    result = service.search_characters(name)

    if not result:
        console.print("[red]No results[/red]")
        return

    show_characters(result)


def handle_search_planet(service):
    name = questionary.text("Enter planet name:").ask()
    result = service.search_planets(name)

    if not result:
        console.print("[red]No results[/red]")
        return

    show_planets(result)


# --- MAIN ---
def main():
    service = StarWarsService()

    actions = {
        "Search character": handle_search_character,
        "Search planet": handle_search_planet,
        "Exit": None
    }

    while True:
        choice = questionary.select(
            "Choose action:",
            choices=list(actions.keys())
        ).ask()

        if choice == "Exit":
            console.print("Goodbye 👋")
            return  # early exit

        action = actions.get(choice)

        if not action:
            console.print("[red]Invalid choice[/red]")
            return  # guard clause

        action(service)


if __name__ == "__main__":
    main()