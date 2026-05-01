import questionary
from services.starwars_service import StarWarsService
from ui.handlers import handle_search_character, handle_search_planet
from rich.console import Console

console = Console()


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
            return

        action = actions.get(choice)

        if not action:
            console.print("[red]Invalid choice[/red]")
            return

        action(service)


if __name__ == "__main__":
    main()