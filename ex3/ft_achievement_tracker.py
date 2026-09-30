#!/usr/bin/env python3
import random

achievements = [
    "First Follower", "Deal with the Devil", "Preacher of Truth",
    "The First Death", "Death to Non-Believers", "The Flock Grows",
    "Flock of Many", "Flock of All", "See No Evil", "Speak No Evil",
    "Hear No Evil", "Think No Evil", "Do No Evil", "Order", "Sate",
    "Cure", "Peace", "Keeper of Secrets", "Leader of the Crusade",
    "Bringer of Light", "Full Flock", "Full Deck", "Teach a Lamb to Fish",
    "Crosser of Thresholds", "Sacrificial Beast", "Weigher of Souls",
    "Hoarder of Wealth", "Weapons of Plenty", "Curses of Plenty",
    "Devotion", "Transform", "Transmute", "Gospel", "Game of Chance",
    "Master of Chance", "Godhood"
]


def get_player_achievements() -> set[str]:
    achievement_list = random.sample(achievements, random.randint(12, 22))
    achievement_set = set(achievement_list)
    return achievement_set


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    alice = get_player_achievements()
    bob = get_player_achievements()
    charlie = get_player_achievements()
    dylan = get_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    everyone = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {everyone}")
    print()
    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}")
    only_alice = alice.difference(bob, charlie, dylan)
    only_bob = bob.difference(alice, charlie, dylan)
    only_charlie = charlie.difference(alice, bob, dylan)
    only_dylan = dylan.difference(alice, bob, charlie)
    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")
    print()
    full = set(achievements)
    print(f"Alice is missing: {full.difference(alice)}")
    print(f"Bob is missing: {full.difference(bob)}")
    print(f"Charlie is missing: {full.difference(charlie)}")
    print(f"Dylan is missing: {full.difference(dylan)}")


if __name__ == "__main__":
    main()
