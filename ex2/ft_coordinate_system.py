#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coords_given = input("Enter new coordinates as floats in"
                             " format 'x,y,z': ")
        coord_list = coords_given.split(",")

        if len(coord_list) != 3:
            print("Invalid syntax")
            continue

        coords: list[float] = []
        for value in coord_list:
            try:
                coords.append(float(value))
            except ValueError as e:
                print(f"Error on parameter '{value}': {e}")
                break

        if len(coords) == 3:
            return (coords[0], coords[1], coords[2])


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    first_tuple = get_player_pos()
    print(f"Got a first tuple: {first_tuple}")
    x1 = first_tuple[0]
    y1 = first_tuple[1]
    z1 = first_tuple[2]
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dis_center = math.sqrt((0-x1)**2 + (0-y1)**2 + (0-z1)**2)
    print(f"Distance to center: {round(dis_center, 4)}")
    print()
    print("Get a second set of coordinates")
    second_tuple = get_player_pos()
    x2 = second_tuple[0]
    y2 = second_tuple[1]
    z2 = second_tuple[2]
    dis_coords = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates:"
          f"{round(dis_coords, 4)}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("/nProgram interrupted")
