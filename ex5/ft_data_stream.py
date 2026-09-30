#!/usr/bin/env python3
import typing
import random

# these are lists
names = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(names), random.choice(actions))


def consume_event(events: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) != 0:
        element = random.choice(events)
        events.remove(element)
        yield element



def main() -> None:
    print("=== Game Data Stream Processor ===")
    generating = gen_event()
    for i in range(1000):
        player, action = next(generating) 
        print(f"Event {i}: Player {player} did action {action}")
    
    event_list = [] 
    for i in range(10):
        event_list.append(next(generating)) 
    print(f"Built list of 10 events: {event_list}")
    
    for one_event in consume_event(event_list):
        print(f"Got event from list: {one_event}")
        print(f"Remains in list: {event_list}")



if __name__ == "__main__":
    main()
