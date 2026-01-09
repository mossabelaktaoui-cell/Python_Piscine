
data = {
    'players': {
        'alice': {
            'items': {
                'pixel_sword': 1, 'code_bow': 1, 'health_byte': 1,
                'quantum_ring': 3
            },
            'total_value': 1875, 'item_count': 6
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


def display_inventory(data, player):
    """Displays the inventory details of a player."""
    weapon = 0
    consumable = 0
    armor = 0
    player_data = data['players'][player]

    print(f"\n=== {player.capitalize()}'s Inventory ===")

    for item in player_data['items'].keys():
        print(f"{item} ({data['catalog'][item]['type']}, "
              f"{data['catalog'][item]['rarity']}): "
              f"{player_data['items'][item]}x @ "
              f"{data['catalog'][item]['value']}"
              " gold each = "
              f"{player_data['items'][item] * data['catalog'][item]['value']}")

        if data['catalog'][item]['type'] == 'weapon':
            weapon += 1
        elif data['catalog'][item]['type'] == 'consumable':
            consumable += 1
        elif data['catalog'][item]['type'] == 'armor':
            armor += 1

    print(f"\nInventory value: {player_data['total_value']} gold")
    print(f"Item count: {player_data['item_count']} items")
    print(f"Categories: weapon({weapon}), "
          f"consumable({consumable}), armor({armor})")


def transe_weapons(data, sender, receiver, weapon, quantity):
    """Transfers weapons between two players."""
    print(f"\n=== Transaction: {sender.capitalize()} gives "
          f"{receiver.capitalize()} {quantity} {weapon} ===")
    sender_data = data['players'][sender]
    receiver_data = data['players'][receiver]

    if sender_data['items'][weapon] < quantity:
        print("Transaction failed!")
        return

    sender_data['items'][weapon] -= quantity
    if weapon not in receiver_data['items'].keys():
        receiver_data['items'].update({weapon: quantity})
    else:
        receiver_data['items'][weapon] += quantity

    print("Transaction successful!")
    print("\n=== Updated Inventories ===")
    print(f"{sender.capitalize()} {weapon}: {sender_data['items'][weapon]}")
    print(f"{receiver.capitalize()} {weapon}: "
          f"{receiver_data['items'][weapon]}")


def inventory_analytics(data, player):
    """Analyzes and displays inventory statistics for a player."""
    player_data = data['players'][player]
    i = 0

    print("\n=== Inventory Analytics ===")
    print(f"Most valuable player: {player.capitalize()} "
          f"({player_data['total_value']} gold)")
    print(f"Most items: {player.capitalize()} "
          f"({player_data['item_count']} items)")
    print("Rasest items: ", end='')
    for item in player_data['items'].keys():
        if i != 0:
            print(", ", end='')
        if data['catalog'][item]['rarity'] == 'rare':
            print(f"{item}", end='')
            i += 1
    print()


if __name__ == "__main__":
    display_inventory(data, 'alice')
    transe_weapons(data, 'alice', 'bob', 'quantum_ring', 2)
    inventory_analytics(data, 'alice')
