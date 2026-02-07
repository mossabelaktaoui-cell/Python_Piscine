def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda arg: [spell1(arg), spell2(arg)]


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda: base_spell() * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return (lambda *args, **kwargs: spell(*args, **kwargs)
            if condition(*args, **kwargs) else "Spell fizzled")


def spell_sequence(spells: list[callable]) -> callable:
    return lambda *args, **kwargs: [spell(*args, **kwargs) for spell in spells]


def main():
    returned_func = spell_combiner(lambda x: "Fireball hits Dragon",
                                   lambda x: "Heals Dragon")
    print("\nTesting spell combiner...")
    print("Combined spell result: ", end='')
    print(f"{returned_func(1)[0]}, {returned_func(1)[1]}")

    returned_func = power_amplifier(lambda: 10, 3)
    print("\nTesting power amplifier...")
    print(f"Original: 10, Amplified: {returned_func()}")

    returned_func = conditional_caster(lambda x: x, lambda x: "Spell applied")
    print("\nTesting conditional caster...")
    print(f"Spell status: {returned_func(1)}")

    returned_func = spell_sequence([lambda x: x,
                                    lambda x: x * 2,
                                    lambda x: x * 3])
    print("\nTesting spell sequence...")
    for i, result in enumerate(returned_func(5)):
        print(f"spell {i + 1} result: {result}")


if __name__ == "__main__":
    main()
