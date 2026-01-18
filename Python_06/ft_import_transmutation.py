def ft_import_transmutation():
    print("\n=== Import Transmutation Mastery ===\n")

    import alchemy.elements
    print("Method 1: Full module import:")
    print("alchemy.elements.create_fire(): "
        f"{alchemy.elements.create_fire()}")

    from alchemy.elements import create_fire, create_fire, create_water
    print("\nMethod 2: Specific function import:")
    print("create_water(): "f"{create_water()}")

    from alchemy.potions import healing_potion as heal
    print("\nMethod 3: Aliased import:")
    print("heal(): "f"{heal()}")

    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion
    print("\nMethod 4: Multiple import:")
    print("create_earth(): "f"{create_earth()}")
    print("create_fire(): "f"{create_fire()}")
    print("strength_potion(): "f"{strength_potion()}")

    print("\nAll import transmutations methods mastered!")
