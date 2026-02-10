def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    power_total = initial_power

    def inner(power: int) -> int:
        nonlocal power_total
        power_total += power
        return power_total
    return inner


def enchantment_factory(enchantment_type: str) -> callable:

    def inner(item_name: str):
        return f"{enchantment_type} {item_name}"
    return inner


def memory_vault() -> dict:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main():
    print("Testing mage counter...")
    counter = mage_counter()
    print(counter(), end=', ')
    print(counter(), end=', ')
    print(counter())

    print("\nTesting spell accumulator...")
    accumulate = spell_accumulator(10)
    print(accumulate(5), end=', ')
    print(accumulate(20), end=', ')
    print(accumulate(3))

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"), end=', ')
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()

    store = vault["store"]
    recall = vault["recall"]

    store("spell", "Fireball")
    store("power", 9001)
    store("mage", "Gandalf")

    print("spell:", recall("spell"))
    print("power:", recall("power"))
    print("mage:", recall("mage"))
    print("dragon:", recall("dragon"))


if __name__ == "__main__":
    main()
