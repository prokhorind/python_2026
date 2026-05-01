def is_known_height(c):
    return c.height != "unknown"


def is_populated(p):
    return (
        p.population != "unknown"
        and p.population.isdigit()
        and int(p.population) > 0
    )