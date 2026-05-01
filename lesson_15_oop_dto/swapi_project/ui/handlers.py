import questionary
from ui.display import show_characters, show_planets
from rich.console import Console

console = Console()


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