import json

with open("suspects.json", "r") as file:
    data = json.load(file)

suspects = data["suspects"]

for suspect in suspects:
    if suspect["alibi"] == False and suspect["logged_in"]:
        print(suspect["name"])


