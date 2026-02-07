def mage_counter() -> callable:
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def spell_accumulator(initial_power: int) -> callable:
    power_total = 0
    def inner():
        nonlocal power_total
        power_total += initial_power
        return power_total
    return inner

def enchantment_factory(enchantment_type: str) -> callable:
    pass

def memory_vault() -> dict[str, callable]:
    pass


first = mage_counter()
print(first())
print(first())
print(first())
print(first())