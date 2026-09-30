#!/usr/bin/env python3
import typing #generator is from typing
import random #random is a module

# these are lists
names = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(names), random.choice(actions))


# a list, whose elements are tuples, each holding two strings
def consume_event(events: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]: #why do we use list and tuple
    while len(events) != 0:
        element = random.choice(events) #choose something from event list and remove?
        events.remove(element)
        yield element



def main() -> None:
    print("=== Game Data Stream Processor ===")
    generating = gen_event()
    for i in range(1000):
        player, action = next(generating) #tuple unpacking
        print(f"Event {i}: Player {player} did action {action}")
    
    event_list = [] #make a new list
    for i in range(10):
        event_list.append(next(generating)) # building a list with append
    print(f"Built list of 10 events: {event_list}")
    
    for one_event in consume_event(event_list):
        print(f"Got event from list: {one_event}")
        print(f"Remains in list: {event_list}") #do we keep calling until event_list is empty?



if __name__ == "__main__":
    main()
