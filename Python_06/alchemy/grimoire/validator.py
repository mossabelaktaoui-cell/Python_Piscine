def validate_ingredients(ingredients: str) -> str:
    allowed = ["fire", "water", "earth", "air"]
    for ingredient in ingredients.split():
        if ingredient not in allowed:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
