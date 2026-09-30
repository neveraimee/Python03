#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {} #keys with a value
    for arg in sys.argv[1:]:
        parts = arg.split(":")
        if len(parts) != 2: #it should be item and quantity
            print(f"Error - invalid parameter '{arg}'")
            continue #to look at other parameters
        name = parts[0] 
        quantity = parts[1]
        if name in inventory: #preventing repeats
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            inventory[name] = int(quantity) # convert quanity to int and store is sword[1]
        except ValueError as e:
            print(f"Quantity error for '{name}': as '{e}'") 

    if len(inventory) == 0: #how to check if its empty?
        print("Inventory is empty!")
        return
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}") #list dict key names
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    for item in inventory.keys(): #i dont understand .keys()
        percent = inventory[item] / total * 100
        print(f"Item {item} represents {round(percent, 1)}%")
    most_item = ""
    most_quantity = 0
    for item in inventory.keys():  
        if inventory[item] > most_quantity:
            most_item = item
            most_quantity = inventory[item]
    print(f"Item most abundant: {most_item} with quantity {most_quantity}")
    least_item = ""
    least_quantity = total
    for item in inventory.keys():
        if inventory[item] < least_quantity:
            least_item = item
            least_quantity = inventory[item]
    print(f"Item least abundant: {least_item} with quantity {least_quantity}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()