"""Simple-reflex two-room vacuum agent and interactive simulation."""

import random


def simple_reflex_agent(percept):
    print("Perception Received: " + str(percept))
    location, status = percept

    if status == "Dirty":
        return "Suck"
    if location == "A":
        return "Right"
    return "Left"


def simulate():
    location = random.choice(["A", "B"])
    condition = random.choice(["Clean", "Dirty"])

    while True:
        action = simple_reflex_agent((location, condition))
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
