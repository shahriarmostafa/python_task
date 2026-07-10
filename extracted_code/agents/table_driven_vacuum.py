"""Table-driven two-room vacuum agent and interactive simulation."""

import random

TABLE = {
    ("A", "Clean"): "Right",
    ("A", "Dirty"): "Suck",
    ("B", "Clean"): "Left",
    ("B", "Dirty"): "Suck",
}

percepts = []


def lookup(percept, table):
    return table[percept]


def table_driven_agent(percept):
    print("Perception Received: " + str(percept))
    percepts.append(percept)
    return lookup(percept, TABLE)


def simulate():
    location = random.choice(["A", "B"])
    condition = random.choice(["Clean", "Dirty"])

    while True:
        action = table_driven_agent((location, condition))
        print("Action Performed: " + action)
        if input("Get Perception (yes/no): ") != "yes":
            break

        if action == "Right":
            location = "B"
            condition = random.choice(["Clean", "Dirty"])
        elif action == "Left":
            location = "A"
            condition = random.choice(["Clean", "Dirty"])
        else:
            condition = "Clean"


if __name__ == "__main__":
    simulate()
