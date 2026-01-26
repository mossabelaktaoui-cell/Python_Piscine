import sys


def inventory_system_analysis(player_items: dict) -> None:

    unique_types = []
    for item in player_items.keys():
        unique_types += [item]
    unique_types = len(set(unique_types))

    total_items = 0
    for item in player_items:
        total_items += int(player_items[item])
    
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")


def current_inventory(player_items: dict) -> None:
    print("\n=== Current Inventory ===")

    total_count = 0
    for item in player_items:
        total_count += int(player_items[item])

    for item, quantity in player_items.items():
        percentage = (quantity / total_count) * 100
        print(f"{item}: {quantity} units ({percentage:.1f}%)")


def inventory_statistics(player_items: dict) -> None:
    most_abundant = ""
    least_abundant = ""

    for item, quantity in player_items.items():
        if most_abundant == "" or least_abundant == "":
            most_abundant = item
            least_abundant = item

        if player_items[most_abundant] < quantity:
            most_abundant = item
        if player_items[least_abundant] > quantity:
            least_abundant = item


    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant} "
          f"({player_items[most_abundant]} units)")
    print(f"Least abundant: {least_abundant} "
          f"({player_items[least_abundant]} units)")


def item_categories(player_items: dict) -> None:
    moderate = {}
    scarce = {}

    for type_, quantity in player_items.items():
        if player_items[type_] >= 5:
            moderate.update({type_: quantity})
        else:
            scarce.update({type_: quantity})

    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def management_suggestions(player_items: dict) -> None:
    restock_needed = []

    for type_, quantity in player_items.items():
        if quantity <= 1:
            restock_needed += [type_]

    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock_needed}")


def dictionary_properties_demo(player_items: dict) -> None:
    keys = []
    values = []

    for key in player_items.keys():
        keys += [key]
    for value in player_items.values():
        values += [value]

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")
    print("Sample lookup - ", end="")
    if keys[0] in player_items.keys():
        print(f"'{keys[0]}' in inventory: True")
    else:
        print(f"'{keys[0]}' in inventory: False")


def main():
    if len(sys.argv) < 2:
        print("No arguments provided. please provide item "
              "data in the format 'type_name:quantity'.")
        return

    for arg in sys.argv[1:]:
        if ':' not in arg or len(arg.split(':')) != 2:
            print(f"Invalid argument format: {arg}. "
                  "Expected format is 'type_name:quantity'.")
            return
        type_name, quantity = arg.split(':')
        if not quantity.isdigit() or int(quantity) < 0:
            print(f"Invalid quantity for item '{type_name}': {quantity}. "
                  "Quantity should be a non-negative integer.")
            return

    player_items = {item.split(':')[0]: int(item.split(':')[1])
                    for item in sys.argv[1:]}

    inventory_system_analysis(player_items)
    current_inventory(player_items)
    inventory_statistics(player_items)
    item_categories(player_items)
    management_suggestions(player_items)
    dictionary_properties_demo(player_items)

if __name__ == "__main__":
    main()
