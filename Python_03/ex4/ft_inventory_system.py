data = {
    'players': {
        'alice': {
            'items': {
                'pixel_sword': 7, 'code_bow': 1, 'health_byte': 1,
                'quantum_ring': 3
            },
            'total_value': 1875, 'item_count': 12
        },
        'bob': {
            'items': {
                'code_bow': 3, 'pixel_sword': 2
            },
            'total_value': 900, 'item_count': 5
        },
        'charlie': {
            'items': {
                'pixel_sword': 1, 'code_bow': 1
            },
            'total_value': 350, 'item_count': 2
        },
        'diana': {
            'items': {
                'code_bow': 3, 'pixel_sword': 3, 'health_byte': 3,
                'data_crystal': 3
            },
            'total_value': 4125, 'item_count': 12
        }
    },
    'catalog': {
        'pixel_sword': {
            'type': 'weapon', 'value': 150, 'rarity': 'common'
        },
        'quantum_ring': {
            'type': 'accessory', 'value': 500, 'rarity': 'rare'
        },
        'health_byte': {
            'type': 'consumable', 'value': 25, 'rarity': 'common'
        },
        'data_crystal': {
            'type': 'material', 'value': 1000, 'rarity': 'legendary'
        },
        'code_bow': {
            'type': 'weapon', 'value': 200, 'rarity': 'uncommon'
        }
    }
}


def inventory_system_analysis(data: dict, player: str) -> None:
    unique_types = []
    total_items = data['players'][player]['item_count']

    for item in data['players'][player]['items'].keys():
        unique_types += [data['catalog'][item]['type']]
    unique_types = len(set(unique_types))

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")


def current_inventory(data: dict, player: str) -> None:
    print("\n=== Current Inventory ===")

    player_items = data['players'][player]['items']
    total_count = data['players'][player]['item_count']

    types_count = {}
    for item in player_items:
        item_type = data['catalog'][item]['type']
        if item_type in types_count.keys():
            types_count[item_type] += player_items[item]
        else:
            types_count[item_type] = player_items[item]

    for type_name, quantity in types_count.items():
        percentage = (quantity / total_count) * 100
        print(f"{type_name}: {quantity} units ({percentage:.1f}%)")


def inventory_statistics(data: dict, player: str) -> None:
    player_items = data['players'][player]['items']
    types_count = {}

    for item in player_items:
        item_type = data['catalog'][item]['type']

        if item_type in types_count.keys():
            types_count[item_type] += player_items[item]
        else:
            types_count[item_type] = player_items[item]

    most_abundant = ""
    least_abundant = ""

    for name, quantity in types_count.items():
        if most_abundant == "" or least_abundant == "":
            most_abundant = name
            least_abundant = name

        if types_count[most_abundant] < quantity:
            most_abundant = name
        if types_count[least_abundant] > quantity:
            least_abundant = name

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant} "
          f"({types_count[most_abundant]} units)")
    print(f"Least abundant: {least_abundant} "
          f"({types_count[least_abundant]} units)")


def item_categories(data: dict, player: str) -> None:
    player_items = data['players'][player]['items']
    types_count = {}
    moderate = {}
    scarce = {}

    for item in player_items:
        item_type = data['catalog'][item]['type']

        if item_type in types_count.keys():
            types_count[item_type] += player_items[item]
        else:
            types_count[item_type] = player_items[item]

    for type_, quantity in types_count.items():
        if types_count[type_] >= 5:
            moderate.update({type_: quantity})
        else:
            scarce.update({type_: quantity})

    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def management_suggestions(data: dict, player: str) -> None:
    player_items = data['players'][player]['items']
    types_count = {}
    restock_needed = []

    for item in player_items:
        item_type = data['catalog'][item]['type']

        if item_type in types_count.keys():
            types_count[item_type] += player_items[item]
        else:
            types_count[item_type] = player_items[item]

    for type_, quantity in types_count.items():
        if quantity <= 1:
            restock_needed += [type_]

    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock_needed}")


def dictionary_properties_demo(data: dict, player: str) -> None:
    player_items = data['players'][player]['items']
    types_count = {}
    keys = []
    values = []

    for item in player_items:
        item_type = data['catalog'][item]['type']

        if item_type in types_count.keys():
            types_count[item_type] += player_items[item]
        else:
            types_count[item_type] = player_items[item]

    for key in types_count.keys():
        keys += [key]
    for value in types_count.values():
        values += [value]

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")
    print("Sample lookup - ", end="")
    if keys[0] in types_count.keys():
        print(f"'{keys[0]}' in inventory: True")
    else:
        print(f"'{keys[0]}' in inventory: False")


if __name__ == "__main__":
    inventory_system_analysis(data, 'bob')
    current_inventory(data, 'alice')
    inventory_statistics(data, 'alice')
    item_categories(data, 'alice')
    management_suggestions(data, 'alice')
    dictionary_properties_demo(data, 'alice')
