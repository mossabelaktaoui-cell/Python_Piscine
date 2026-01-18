from alchemy.elements import create_fire, create_earth


def lead_to_gold():
    return (f"Lead transmuted to gold using"
            f" {create_fire()}")


def stone_to_gem():
    return (f"Stone transmuted to gem using"
            f" {create_earth()}")
