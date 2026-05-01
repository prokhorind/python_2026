import requests
from dto.character import CharacterDTO
from dto.planet import PlanetDTO
from utils.filters import is_known_height, is_populated


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


class StarWarsService:
    BASE_URL = "https://swapi.py4e.com/api"

    def search_characters(self, name):
        data = requests.get(f"{self.BASE_URL}/people/?search={name}").json()

        chars = list(map(to_character_dto, data["results"]))
        return list(filter(is_known_height, chars))

    def search_planets(self, name):
        data = requests.get(f"{self.BASE_URL}/planets/?search={name}").json()

        planets = list(map(to_planet_dto, data["results"]))
        return list(filter(is_populated, planets))