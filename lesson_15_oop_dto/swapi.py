"""
SWAPI + DTO + Questionary (arrow menu that works in PyCharm)
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


# --- Service ---
class StarWarsService:

    BASE_URL = "https://swapi.py4e.com/api"

    def search_characters(self, name):
        data = requests.get(f"{self.BASE_URL}/people/?search={name}").json()

        return [
            CharacterDTO(
                item.get("name"),
                item.get("height"),
                item.get("gender")
            )
            for item in data["results"]
        ]

    def search_planets(self, name):
        data = requests.get(f"{self.BASE_URL}/planets/?search={name}").json()

        return [
            PlanetDTO(
                item.get("name"),
                item.get("climate"),
                item.get("population")
            )
            for item in data["results"]
        ]


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


# --- MAIN ---
def main():
    service = StarWarsService()

    while True:
        choice = questionary.select(
            "Choose action:",
            choices=[
                "Search character",
                "Search planet",
                "Exit"
            ]
        ).ask()

        if choice == "Search character":
            name = questionary.text("Enter character name:").ask()
            result = service.search_characters(name)

            if result:
                show_characters(result)
            else:
                console.print("[red]No results[/red]")

        elif choice == "Search planet":
            name = questionary.text("Enter planet name:").ask()
            result = service.search_planets(name)

            if result:
                show_planets(result)
            else:
                console.print("[red]No results[/red]")

        elif choice == "Exit":
            console.print("Goodbye 👋")
            break


if __name__ == "__main__":
    main()