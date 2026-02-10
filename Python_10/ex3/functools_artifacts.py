from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    result = 0
    if not spells:
        return "Spell list cannot be empty"

    if operation == "add":
        result = reduce(operator.add, spells)
    elif operation == "multiply":
        result = reduce(operator.mul, spells)
    elif operation == "max":
        result = reduce(max, spells)
    elif operation == "min":
        result = reduce(min, spells)
    else:
        return f"Unsupported operation: {operation}"
    return result


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment,
                                power=50,
                                element='fire_enchant'),
        'ice_enchant': partial(base_enchantment,
                               power=50,
                               element='ice_enchant'),
        'lightning_enchant': partial(base_enchantment,
                                     power=50,
                                     element='lightning_enchant')
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher():
    @singledispatch
    def cast(spell):
        return f"Unknown spell type: {type(spell).__name__}"

    @cast.register(int)
    def _(damage: int):
        return f"Damage spell deals {damage} points!"

    @cast.register(str)
    def _(enchantment: str) -> str:
        return f"Enchantment spell: '{enchantment}'"

    @cast.register(list)
    def _(spells: list):
        results = [cast(s) for s in spells]
        total = ""
        for result in results:
            total += result + "\n"
        return total

    return cast


def main():

    print("\nTesting spell reducer...")
    spells = [2, 3, 4]
    print("Sum:", spell_reducer(spells, "add"))
    print("Mul:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))

    print("\nTesting partial enchanter...")

    def base_enchantment(*, power: int, element: str, target: str) -> str:
        return f"{element} enchant applied to {target} with power {power}"

    enchants = partial_enchanter(base_enchantment)
    actions = [
        ("fire_enchant", "Goblin"),
        ("ice_enchant", "Orc"),
        ("lightning_enchant", "Dragon")
    ]
    for enchant_name, target in actions:
        print(enchants[enchant_name](target=target))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    caster = spell_dispatcher()
    print(caster(50))
    print(caster("Flaming Sword"))
    print(caster([20, "Frost Shield", "Dragon pil"]))


if __name__ == "__main__":
    main()
