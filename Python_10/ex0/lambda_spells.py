def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda item: item['power'], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))

def mage_stats(mages: list[dict]) -> dict:
    powers = [mage['power'] for mage in mages]
    return {
        'max_power': max(mages, key=lambda mage: mage['power']),
        'min_power': min(mages, key=lambda mage: mage['power']),
        'avg_power': sum(powers) / len(powers) if powers else 0
    }


def main():
    mages = [
        {"name": "Merlin", "power": 80},
        {"name": "Rincewind", "power": 20},
    ]
    artifacts = [
        {'name': "Crystal Orb", 'power': 85, 'element': 'element'},
        {'name': "Fire Staff", 'power': 92, 'element': 'element'}
    ]
    spells = ["fireball", "heal", "shield"]

    print("\nTesting artifact sorter...")
    artifacts = artifact_sorter(artifacts)
    print(f"{artifacts[0]['name']} ({artifacts[0]['power']} power)", end='')
    print(" comes before ", end='')
    print(f"{artifacts[1]['name']} ({artifacts[1]['power']} power)")

    print("\nTesting power filter")
    strong_mages = power_filter(mages, min_power=50)
    print("Mages with power >= 50:")
    for mage in strong_mages:
        print(f"{mage['name']} (Power: {mage['power']})")

    print("\nTesting spell transformer...")
    for spell in spell_transformer(spells):
        print(f"{spell} ", end='')

    print("\n\nTesting mage stats...")
    stats = mage_stats(mages)
    print("Mage stats:")
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Average power: {stats['avg_power']:.2f}")



if __name__ == "__main__":
    main()