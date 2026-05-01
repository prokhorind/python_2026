from rich.console import Console
from rich.table import Table

console = Console()


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