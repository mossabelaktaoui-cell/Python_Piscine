def validate_ingredients(ingredients: str) -> str:
    allowed = ["fire", "water", "earth", "air"]
    for ingredient in ingredients.split(' '):
        if ingredient in allowed:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
